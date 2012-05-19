{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

{% for s in params.set.contains.all %}

<h2>{{ s.name }}</h2>
<div id="board{{s.id}}" style="margin-bottom: 10px;">loading..</div>
<div><input type="button" onclick="board_thread({{s.id}})" value="new thread"></div>

{% endfor %}

<script type="text/javascript">

function board_thread_show(id) {
	$.getJSON('{% url thread_list "'+id+'" 0 0 %}', function(data) {
		$('#board'+id).html('<table id="comtable'+id+'" class="thread_list"><tr><th>Subject</th><th>Poster</th><th>#post</th><th>Last Activity</th></tr></table>');
		var found = 0;

		$.each(data, function(key, obj) {
			found = 1;
			var td = '<tr><td><a href="{% url thread_view "'+obj.id+'" %}"';
			td += ' onclick="return Iload(\'{% url thread_view "'+obj.id+'" %}\');">';
			td += obj.subject + '</a></td><td>' + obj.owner_name + '</td><td><center>';
			td += obj.length + '</center></td><td>' + obj.date_max + '</td></tr>';
			$('#comtable'+id).append(td);
		});

		if (found == 0)
			 $('#board'+id).html('No thread found');
	});
}

function board_thread(id) {
	overlay_reset();
	overlay_title("New Thread");
	overlay_form({"id": "new_thread", "url": "{% url thread_post %}",
				  "content": '{{ tform.as_table|escapejs }}', "submit": "post"});
	$('#id_course').val(id);
	$('#id_document').val(0);
	$('#id_page').val(0);
	overlay_show();
	overlay_refresh();
	$('#new_thread').submit(function() {
		Pload('new_thread', '{% url thread_post %}', function() {
			$('#board'+id).html('reloading..');
			board_thread_show(id);
		});
		return false;
	});
}

{% for s in params.set.contains.all %}
board_thread_show({{s.id}});
{% endfor %}

</script>