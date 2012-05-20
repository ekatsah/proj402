{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<script src="/static/jquery.cookie.js" type="text/javascript"></script>
<script src="/static/jquery.treeview.js" type="text/javascript"></script>
<link rel="stylesheet" href="/static/jquery.treeview.css" />

<script type="text/javascript">

function add_click(node, pnode) {
	overlay_reset();
	overlay_title("Add");
	$('#overlay_content').html('Create new category : <input id="new_cat_name"/>');
	$('#overlay_content').append('<input id="NCbut" type="button" value="insert" onclick="cat_new('+node+');"/><br>');
	$('#overlay_content').append('Use existing category : <select id="exist_cat"/></select>');
	$('#overlay_content').append('<input id="ECbut" type="button" value="insert" onclick="cat_app('+node+');"/><br>');
	$('#overlay_content').append('Add course : <input id="new_course_slug" value="hell-x-666"/>');
	$('#overlay_content').append('<input id="NCSbut" type="button" value="insert" onclick="course_attach('+node+');"/><br>');
	$('#overlay_content').append('<input type="button" value="create course" onclick="course_new('+node+');"/><br>');
	$('#exist_cat').html(options);
	$('#new_cat_name').keypress(function(e) { if (e.which == 13) cat_new(node); });
	$('#exist_cat').keypress(function(e) { if (e.which == 13) cat_app(node); });
	$('#new_course_slug').keypress(function(e) { if (e.which == 13) course_attach(node); });
	overlay_show();
	overlay_refresh();
}

function course_new(node) {
	overlay_reset();
	overlay_title("Create course");
	overlay_form({"id": "course_new", "url": "{% url course_new %}",
	              "content": '{{ nform.as_table|escapejs }}', "submit": "create"});
	overlay_show();
	overlay_refresh();
	$('#course_new').submit(function() {
		var slug = $('#id_slug').val().toLowerCase();
		Pload('course_new', '{% url course_new %}', function() {
			course_attach(node, slug);
		});
		return false;
	});
}

function cat_new(node) {
	var cname = $('#new_cat_name').val();
	overlay_reset();
	overlay_title("Create category");
	overlay_form({"id": "category_new", "url": "{% url category_new %}",
	              "content": '{{ cform.as_table|escapejs }}', "submit": "create"});
	$('#id_name').val(cname);
	overlay_show();
	overlay_refresh();
	$('#category_new').submit(function() {
		Pload('category_new', '{% url category_new %}', function(data) {
			cat_id = data.substr(3);
			Gload('{% url category_attach "'+node+'" "'+cat_id" %}, load_cc);
		});
		return false;
	});
}

function cat_del(n, pn) {
	Gload('{% url category_detach "'+n+'" "'+pn" %}, load_cc);
}

function cat_app(node) {
	val = $('#exist_cat').val();
	if (node != val)
		Gload('{% url category_attach "'+node+'" "'+val" %}, function() {
			overlay_close();
			load_cc();
		});
	else
		alert("no node in node");
}

function cat_rm(id) {
	Gload('{% url category_del "'+id" %}, load_cc);
}

function cat_edit(id) {
	alert("NYI");
}

function course_detach(id, node) {
	Gload('{% url cat_course_del "'+node+'" "'+courses[id].slug" %}, load_cc);
}

function course_attach(node, prev_slug) {
	var slug = $("#new_course_slug").val();
	if (prev_slug != undefined)
		slug = prev_slug;

	Gload('{% url cat_course_add "'+node+'" "'+slug" %}, load_cc);
}

function grow_tree(node, depth, pnode) {
	if (depth > 10) // anti loop
		return;

	var elem = $(document.createElement('ul'));
	
	for (var n in categories[node].holds) {
		var cid = categories[node].holds[n]
		var li = $(document.createElement('li'));
		li.append("<span>&nbsp;<small>" + cid + '</small>) '+ categories[cid].name + '</span>');
		li.append('&nbsp;<span class="rem" onclick="cat_del('+cid+','+node+')">[detach]</span>');
		li.append(grow_tree(cid, depth + 1, node));
		elem.append(li);
	}

	for (var n in categories[node].contains) {
		var li = $(document.createElement('li'));
		var cid = categories[node].contains[n]
		li.append('&nbsp;' + courses[cid].slug + ' : ' + courses[cid].name);
		li.append('&nbsp;<span class="rem" onclick="course_detach('+cid+','+node+')">[detach]</span>');
		elem.append(li);
	}

	var add = $(document.createElement('li'))
	$(add).html('&nbsp;add');
	$(add).addClass("add_but");
	$(add).click(function() {add_click(node, pnode);});
	$(elem).append(add);	

	return elem;
}

function links(id) {
	if (id > 2)
		return '<small>[<span class="action_link" onclick="cat_edit(' + 
		       id + ');">edit</span>, <span class="action_link" \
		       onclick="cat_rm(' + id + ');">remove</span>]</small> ';
	else
		return '';
}

function load_cc() {
	$('#tree').html('loading..');
	$('#list').html('loading..');

	ready_course = 0;
	ready_category = 0;

	$.getJSON('{% url categories_all %}', function(data) {
		ready_category = 1;
		$('#list').html('');
		categories = Array();
		n2id = Array();
		options = "";

		$.each(data, function(key, obj) {
			categories[obj.id] = obj;
			n2id[obj.name] = obj.id;
			$('#list').append('<li>'+ obj.id + ') ' + links(obj.id) + 
			           obj.name + ' : ' + obj.description + '</li>');
			options += '<option value="' + obj.id + '">' + obj.name + '</option>';
		});
		build();
	});

	$.getJSON('{% url courses_all %}', function(data) {
		ready_course = 1;
		$('#courses_list').html('');
		courses = Array();

		$.each(data, function(key, obj) {
			courses[obj.id] = obj;
			$('#courses_list').append('<li>'+ obj.slug + ' : ' + obj.name + ', ' + obj.description + '</li>');
		});
		build();
	});
}

function build() {
	// not all data are here
	if (ready_course == 0 || ready_category == 0)
		return;
	 
	$('#tree').html('');
	var e = grow_tree(1, 0, 1);
	$('#tree').append(e);
	$(e).treeview({
	//	control: "#treecontrol",
		persist: "cookie",
		cookieId: "adm-tree-catcourses"
	});
}

$(document).ready(load_cc);
</script>

<h1>Category Tree</h1>
<p id="tree"></p>

<h1>All categories</h1>
<ul id="list"></ul>

<h1>All courses</h1>
<ul id="courses_list"></ul>
