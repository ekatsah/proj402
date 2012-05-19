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
	$('#overlay_title').html('');
	$('#overlay_content').html('');
	$('#grey').css('width', '100%');
	$('#grey').css('height', '100%');
}

function overlay_title(title) {	$('#overlay_title').html(title); }
function overlay_content(thing) { $('#overlay_content').html(thing); }
function overlay_append(thing) { $('#overlay_content').append(thing); }
function overlay_prepend(thing) { $('#overlay_content').prepend(thing); }

function overlay_form() {
	$(arguments).each(function (idx, form) {
		var hform = document.createElement('form');
		hform.id = form["id"];
		hform.method = 'post';
		if (form['enctype'])
			hform.enctype = form['enctype'];
		hform.action = form['url'];
		$(hform).append('<input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken"/>');
		$(hform).append('<table class="vtop">'+ form['content'] +'</table>');
		$(hform).append('<center><input type="submit" value="' + form['submit'] + '" id="' +
		               form['id'] + '_submit"/></center>');
		overlay_append('<div id="' + form["id"] + '_pre">');
		overlay_append(hform);
		overlay_append('<div id="' + form["id"] + '_app">');
	});
}
