#!/usr/bin/python3
from flask import Flask, render_template, url_for, redirect,Response,request,flash,abort
from random import choice
from urllib.parse import urlparse
import redis
import json
CONFIG_FILE = 'config.json'
with open(CONFIG_FILE, 'r') as f:
	config = json.loads(f.read())
r = redis.Redis(host=config['redis']['host'], port=config['redis']['port'],charset=config['redis']['charset'],password=config['redis']['password'])
app = Flask(__name__)
def generate_uid():
	return "".join(choice(config['chars']) for i in range(config['id_length']))
def save_url(url):
	uid = generate_uid()
	while r.get("url:" + uid) != None:
		uid = generate_uid()
	r.set("url:"+uid, url)
	return uid
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/shorten', methods=['POST'])
def shorten():
	url = request.form['url']
	parsed = urlparse(url)
	if len(parsed.netloc) > 0 and len(parsed.scheme) > 3:
		return redirect(url_for('success_page', uid=save_url(url)))
	else:
		return redirect(url_for('index'))
@app.route('/success/<uid>')
def success_page(uid):
	return render_template('index.html', uid=uid)
# The following route MUST be the previous one + .json ( used by the JavaScript client )
@app.route('/shorten.json', methods=['POST'])
def shorten_json():
	data = {}
	url = request.form['url']
	parsed = urlparse(url)
	data['long_url'] = url
	if len(parsed.netloc) > 0 and len(parsed.scheme) > 3:
		data['status'] = 'success'
		data['short_url'] = request.url_root + save_url(url)
	else:
		data['status'] = 'failure'
		data['error'] = 'INVALID_URL'
	print(data)
	return Response(json.dumps(data), mimetype='application/json')
@app.route('/<uid>')
def short_url(uid):
	url = r.get('url:' + uid)
	if url == None:
		return abort(404)
	else:
		return redirect(url.decode("utf-8"))
app.debug = True
if __name__ == '__main__':
	if config['ssl']['enable']:
		app.run(host=config['host'], port=config['port'], ssl_context=(config['ssl']['cert'],config['ssl']['key']))
	app.run(host=config['host'], port=config['port'])