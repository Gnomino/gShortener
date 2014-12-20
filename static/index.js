$('#shorten_form').submit(function() {
	$('#shorten_form').addClass('loading');
	$.post($('#shorten_form').attr('action') + '.json', {"url": $('#url').val()}, function(data) {
		if(data.status == 'success') {
			$('#message_place').addClass('ui positive message');
			$('#message_place').text('Here is your short URL : ').append($('<span>').addClass("ui purple label").text(data['short_url']));
		}
		else {
			$('#message_place').addClass('ui negative message');
			$('#message_place').text('There was an error while shortening your URL : ' + data.error)
		}
		$('#shorten_form').removeClass('loading');
	}, 'json');
	return false;
});