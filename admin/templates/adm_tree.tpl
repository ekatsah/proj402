<script src="/static/jquery.cookie.js" type="text/javascript"></script>
<script src="/static/jquery.treeview.js" type="text/javascript"></script>
<link rel="stylesheet" href="/static/jquery.treeview.css" />

<div id="boxes" style="display:none">
<input id="add_node" type="hidden"/>
<input id="add_pnode" type="hidden"/>

<div id="add_box">
Create new category : <input id="new_cat_name"/><input type="button" value="insert" onclick="cat_new()"/><br>

Use existing category : <select id="exist_cat"/></select><input type="button" value="insert"/><br>

Create course : <input id="new_course_slug" value="hell-x-666"/><input type="button" value="insert"/><br>
</div>
</div>
<script type="text/javascript">

function add_click(node, pnode) {
	overlay_reset();
	overlay_title("Add");
	$('#overlay_content').html($('#add_box'));
	$('#add_node').val(node);
	$('#add_pnode').val(pnode);
	overlay_show();
	overlay_refresh();
}

function cat_new() {
	var val = $('#new_cat_name').val();
	var node = $('#add_node').val();

	$.get('{% url adm_tree_new "'+node+'" "'+val" %}, function(data) {
		if (data == "ok") {
			build();
			overlay_close();
		} else
			alert("error! + data");
	});
}

function grow_tree(node, depth, pnode) {
	if (depth > 10) // anti loop
		return;

	var elem = $(document.createElement('ul'));
	
	for (var n in categories[node].holds) {
		var li = $(document.createElement('li'));
		li.append("<span>&nbsp;" + categories[categories[node].holds[n]].name + "</span>");
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

		$("#exist_cat").html(options);

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
