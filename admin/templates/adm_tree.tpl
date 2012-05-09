<script src="/static/jquery.cookie.js" type="text/javascript"></script>
<script src="/static/jquery.treeview.js" type="text/javascript"></script>
<link rel="stylesheet" href="/static/jquery.treeview.css" />

<script type="text/javascript">

function add_click(node, pnode) {
	overlay_reset();
	overlay_title("Add");
	$('#overlay_content').html('Create new category : <input id="new_cat_name"/>');
	$('#overlay_content').append('<input type="button" value="insert" onclick="cat_new('+node+');"/><br>');
	$('#overlay_content').append('Use existing category : <select id="exist_cat"/></select>');
	$('#overlay_content').append('<input type="button" value="insert" onclick="cat_app('+node+');"/><br>');
	$('#overlay_content').append('Add course : <input id="new_course_slug" value="hell-x-666"/>');
	$('#overlay_content').append('<input type="button" value="insert"/><br>');
	$('#overlay_content').append('<input type="button" value="create course" onclick="course_new('+node+');"/><br>');
	$('#exist_cat').html(options);
	overlay_show();
	overlay_refresh();
}

function course_new(node) {
	overlay_reset();
	overlay_title("Create course");
	var form = document.createElement('form');
	form.id = 'course_new_form';
	form.method = 'post';
	form.action = '{% url course_new %}';
	$(form).append(''+<div><![CDATA[{% csrf_token %}]]></div>);
	$(form).append(''+<div><![CDATA[<table class="vtop">{{ nform.as_table }}</table>]]></div>);
	$(form).append('<center><input type="submit" value="create" id="fcreate_course"/></center>');
	$('#overlay_content').html(form);
	overlay_show();
	overlay_refresh();
	$(form).submit(function() {
		var slug = $('#id_slug').val();
		Pload('course_new_form', '{% url course_new %}', function() {
			$.get('{% url adm_tree_c_add "'+node+'" "'+slug" %}, function(data) {
				if (data == 'ok')
					build();
				else
					alert("error! " + data);
			});
		});
		return false;
	});
}

function cat_new(node) {
	var val = $('#new_cat_name').val();

	$.get('{% url adm_tree_new "'+node+'" "'+val" %}, function(data) {
		if (data == "ok") {
			overlay_close();
			build();
		} else
			alert("error! " + data);
	});
}

function cat_del(n, pn) {
	$.get('{% url adm_tree_rm "'+n+'" "'+pn" %}, function(data) {
		if (data == "ok")
			build();
		else
			alert("error! " + data);
	});
}

function cat_app(node) {
	val = $('#exist_cat').val();
	if (node != val)
		$.get('{% url adm_tree_add "'+node+'" "'+val" %}, function(data) {
			if (data == "ok") {
				overlay_close();
				build();
			} else
				alert("error! " + data);
		});
	else
		alert("no node in node");
}

function grow_tree(node, depth, pnode) {
	if (depth > 10) // anti loop
		return;

	var elem = $(document.createElement('ul'));
	
	for (var n in categories[node].holds) {
		var li = $(document.createElement('li'));
		li.append("<span>&nbsp;" + categories[categories[node].holds[n]].name + '</span>');
		li.append('&nbsp;<span class="rem" onclick="cat_del('+categories[node].holds[n]+','+node+')">detach</span>');
		li.append(grow_tree(categories[node].holds[n], depth + 1, node));
		elem.append(li);
	}

	for (var n in categories[node].contains) {
		var li = $(document.createElement('li'));
		li.append('&nbsp;' + courses[categories[node].contains[n]].slug + ' : ' + courses[categories[node].contains[n]].name);
		elem.append(li);
	}

	var add = $(document.createElement('li'))
	$(add).html('&nbsp;add');
	$(add).addClass("add_but");
	$(add).click(function() {add_click(node, pnode);});
	$(elem).append(add);	

	return elem;
}

function load_cc() {
	$('#tree').html('loading..');
	$('#list').html('loading..');

	ready_course = 0;
	ready_category = 0;

	$.getJSON('{% url category_all %}', function(data) {
		ready_category = 1;
		$('#list').html('');
		categories = Array();
		n2id = Array();
		options = "";

		$.each(data, function(key, obj) {
			categories[obj.id] = obj;
			n2id[obj.name] = obj.id;
			$('#list').append('<li>'+ obj.name + ' : ' + obj.description + '</li>');
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
<ol id="list"></ol>

<h1>All courses</h1>
<ol id="courses_list"></ol>
