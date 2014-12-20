gShortener
==========
gShortener is a  lightweight and simple URL shortener written in Python, using Flask and Redis.

Instructions to install it to the gShortener directory :

    pip install redis Flask
    wget https://github.com/Gnomino/gShortener/archive/master.tar.gz -O gShortener.tar.gz
    tar xzvf gShortener.tar.gz
    mv gShortener-master gShortener

You'll probably want to edit config.json to set up Redis.

When everything is set up, you can either launch it directly :

    python app.py
Or use a popular HTTP server with uWSGI, for example.

This program is distributed under the MIT License :

    The MIT License (MIT)
    Copyright (c) 2014
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.