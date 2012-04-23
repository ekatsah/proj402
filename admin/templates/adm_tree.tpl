<script type="text/javascript">

function cat_add(node) {
	val = $('#n'+node).val();
	if (node != val)
		$.get('{% url adm_tree_add "'+node+'" "'+val" %}, function(data) {
			if (data == "ok")
				build();
			else
				alert("error! + data");
		});
	else
		alert("no node in node");
}

function cat_new(node) {
	val = $('#t'+node).val();
	$.get('{% url adm_tree_new "'+node+'" "'+val" %}, function(data) {
		if (data == "ok")
			build();
		else
			alert("error! + data");
	});
}

function cat_rm(node, pnode) {
	$.get('{% url adm_tree_rm "'+node+'" "'+pnode" %}, function(data) {
		if (data == "ok")
			build();
		else
			alert("error! + data");
	});
}

function grow_tree(node, depth, pnode) {
	if (depth > 10) // anti loop
		return;

	$('#tree').append('<span style="margin-left: ' + (depth*30) + 'px;"> - ' + categories[node].name);
	$('#tree').append(' <select id="n' + node + '">' + options);
	$('#tree').append('</select><input type="button" value="add" onclick="cat_add('+node+');">');
	if (depth != 0)
		$('#tree').append('<input type="button" value="rm" onclick="cat_rm('+node+', '+pnode+');">');
	$('#tree').append('<br>');
	for (var n in categories[node].holds)
		grow_tree(categories[node].holds[n], depth + 1, node);
	$('#tree').append('<span style="margin-left: ' + ((depth+1)*30) + 'px;"> - <input value="new category" id="t'+node+'"><input type="button" value="add" onclick="cat_new('+node+');"></span><br>');
	$('#tree').append('</span><br>');
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

		grow_tree(1, 0, 1);
	});
}

$(document).ready(build);
</script>

<h1>Category Tree</h1>
<p id="tree"></p>

<h1>All categories</h1>
<ol id="list"></ol>
