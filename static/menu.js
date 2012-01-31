
tmpvars = Array();
/* Drop down menu */
function mshow(name) {
	if (tmpvars[name] == undefined)
		tmpvars[name] = function(){};
	tmpvars[name].m1 = 1;
	$('#'+name).css('display', 'block');
	$('#'+name).css('opacity', '1');
	$('#'+name).css('height', 'auto');
}

function mhide_real(name) {
	var o = $('#'+name);
	if (tmpvars[name].m1 == 0 && tmpvars[name].m2 == 0)
		o.slideUp(100);
}

function mhide(name) {
	tmpvars[name].m1 = 0;
	$('#'+name)._t = setTimeout(function() {mhide_real(name)}, 200);
}

function mshow2(name) {
	tmpvars[name].m2 = 1;
}

function mhide2(name) {
	tmpvars[name].m2 = 0;
	$('#'+name)._t = setTimeout(function() {mhide_real(name)}, 200);
}

/* courses show */

Mcategories = Array();
Mcategories[1] = {'name' : 'Science'};

function mmake(i, catid) {
	var base;
	document.body.removeChild
	for (var it = i; $('#ml' + it).length > 0; ++it) 
		$('#links').get(0).removeChild($('#ml' + it).get(0));

	base  = '<dl class="menu" id="ml' + i + '"><dt onmouseover="mshow(\'mv' + i + '\')" ';
	base += 'onmouseout="mhide(\'mv' + i + '\')"><a href="#" id="mt' + i + '">loading..</a></dt>';
	base += '<dd id="mv' + i + '" onmouseover="mshow2(\'mv' + i + '\')" ';
	base += 'onmouseout="mhide2(\'mv' + i + '\')"></dd></dl>';
	$('#links').append(base);

	$.getJSON(URL_CAT_SUB + catid, function(data) {
		ul = document.createElement("ul");
		$('#mt' + i).html(Mcategories[catid].name);
		$.each(data, function(key, obj) {
			Mcategories[obj.id] = {'name' : obj.name};
			$(ul).prepend('<li><span onclick="mmake('+(i+1)+', '+obj.id+');">'+obj.name+'</span></li>');
		});
		$('#mv' + i).append(ul)
	});

	$.getJSON(URL_COURSES_CAT + catid, function(data) {
		ul = document.createElement("ul");
		$('#mt' + i).html(Mcategories[catid].name);
		$.each(data, function(key, obj) {
			// HARD_URL
			$(ul).append('<li class="light"><a href="#/course/s/' + obj.slug + '" onclick="return Iload(\'/course/s/'+obj.slug+'\');">'+obj.name+'</a></li>');
		});
		$('#mv' + i).append(ul)
	});
}
