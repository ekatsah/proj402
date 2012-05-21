{% load i18n %}
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
<div id="board{{s.id}}" style="margin-bottom: 10px;">{% trans "loading.." %}</div>
<div><input type="button" onclick="board_thread({{s.id}})" value="{% trans "new thread" %}"></div>

{% endfor %}

<script type="text/javascript">

function board_thread_show(id) {
	$.getJSON('{% url thread_list "'+id+'" 0 0 %}', function(data) {
		$('#board'+id).html('<table id="comtable'+id+'" class="sortable"><thead><tr><th>Subject</th><th>Poster</th><th>#post</th><th>Last Activity</th></tr></thead></table>');
		$('#comtable'+id).dataTable({
			"bPaginate": false,
			"bFilter": false,
			"bAutoWidth" : false,
		});
		$.each(data, function(key, obj) {
			$('#comtable'+id).dataTable().fnAddData([
			    '<a href="{% url thread_view "'+obj.id+'" %}"' +
				' onclick="return Iload(\'{% url thread_view "'+obj.id+'" %}\');">' + 
				obj.subject + '</a>',
				obj.owner_name, 
				'<center>' + obj.length + '</center>',
				obj.date_max
			]);
		});
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
