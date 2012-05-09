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
	$('#overlay_content').append('Create course : <input id="new_course_slug" value="hell-x-666"/>');
	$('#overlay_content').append('<input type="button" value="insert"/><br>');
	$('#exist_cat').html(options);
	overlay_show();
	overlay_refresh();
}

function cat_new(node) {
	var val = $('#new_cat_name').val();

	$.get('{% url adm_tree_new "'+node+'" "'+val" %}, function(data) {
		if (data == "ok") {
			overlay_close();
			build();
		} else
			alert("error! + data");
	});
}

function cat_del(n, pn) {
	$.get('{% url adm_tree_rm "'+n+'" "'+pn" %}, function(data) {
		if (data == "ok")
			build();
		else
			alert("error! + data");
	});
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

	var add = $(document.createElement('li'))
	$(add).html('&nbsp;&nbsp;add');
	$(add).addClass("add_but");
	$(add).click(function() {add_click(node, pnode);});
	$(elem).append(add);	

	return elem;
}

function build() {
	$('#tree').html('loading..');
	$('#list').html('loading..');
	$.getJSON('{% url category_all %}', function(data) {
		$('#tree').html('');
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

		var e = grow_tree(1, 0, 1);
		$('#tree').append(e);
		$(e).treeview({
		//	control: "#treecontrol",
			persist: "cookie",
			cookieId: "adm-tree-catcourses"
		});
	});
}

$(document).ready(build);
</script>

<h1>Category Tree</h1>
<p id="tree"></p>

<h1>All categories</h1>
<ol id="list"></ol>
