// compute the layout's positions 
function overlay_refresh() {
	var l, t;
	l = $(window).width() / 2 - $('#overlay_box').width() / 2;
	if (l < 0)
		l = 3;
	t = $(window).height() / 2 - $('#overlay_box').height() / 2;
	if (t < 0)
		t = 3;
	$('#overlay_box').css('top', t);
	$('#overlay_box').css('left', l);
    	if ($('#overlay_box').width() > $('#grey').width())
    		$('#grey').width($('#overlay_box').width() + 6);
	if ($('#overlay_box').height() > $('#grey').height())
    		$('#grey').height($('#overlay_box').height() + 6);
}

$(window).resize(function() {
	if ($('#front').css('display') == 'block')
		overlay_refresh();
});

function overlay_escape(e) {
	if (e.keyCode == 27)
		overlay_close();
}

// show the overlay layout
function overlay_show() {
	overlay_refresh();
	$('#front').css('display', 'block');
	$(document).keypress(overlay_escape);
}

// close the overlay layout
function overlay_close() {
	$('#front').css('display', 'none');
	$(document).unbind('keypress', overlay_escape);
}

function overlay_reset() {
	$('#overlay_title').html(' ');
	$('#overlay_content').html('loading..');
	$('#grey').css('width', '100%');
	$('#grey').css('height', '100%');
}

function overlay_title(title) {
	$('#overlay_title').html(title);
}
