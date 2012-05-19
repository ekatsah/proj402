{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

{% load can_vote %}

<script type="text/javascript">

can_vote = { {% for doc in object.documents.all %} "{{ doc.id }}": "{{ user|can_voteD:doc }}", {% endfor %} };
documents = {};

function upload_file() {
	overlay_reset();
	overlay_title("New Document");
	overlay_form({"id": "upload_file", "url": "{% url upload_file object.slug %}",
	              "enctype": "multipart/form-data", "content": '{{ uform.as_table|escapejs }}',
	              "submit": "upload file"},
	             {"id": "upload_http", "url": "{% url upload_http_file object.slug %}",
	              "content": '{{ hform.as_table|escapejs }}', "submit": "upload url"});
	$('#upload_file_pre').html('<h1>Upload File</h1>');
	$('#upload_file_app').html('<hr/>');
	$('#upload_http_pre').html('<h1>Upload From URL</h1>');
	overlay_show();
	overlay_refresh();
	$('#upload_http').submit(function() {
		Pload('upload_http', '{% url upload_http_file object.slug %}', function(data) {
			Iload('{% url course_show object.slug %}');
		});
		return false;
	});
}

function document_row(obj) {
	var status = '';
	var points = '';
	var size = '<center>' + obj.size + '</center>';
	var name = '<a href="{% url view_file "'+obj.id+'" %}" onclick="return Iload(\'{% url view_file "'+obj.id+'" %}\');">' + obj.name + '</a>';

	if (obj.size != obj.done) {
		all_done = 0;
		name = obj.name;
		if (obj.size <= 1) {
			status = 'waiting';
			obj.size = '';
		} else {
			status = '<img src="/static/loading.gif"/>&nbsp';
			status += '<small>' + Math.round(100*obj.done/obj.size) + '%</small>'
		}
	} else {
		if (can_vote[obj.id] == "True")
			points = '<img src="/static/up.png" onclick="Dupvote(' + obj.id + ',\'' + obj.category + '\');"/>'
		           + ' <span id="points_' + obj.id + '">'  + obj['points.score'] + '</span> '
		       	   + '<img src="/static/down.png" onclick="Ddownvote(' + obj.id + ',\'' + obj.category + '\');"/>';
		else
			points = '<center>' + obj['points.score'] + '</center>';
	}
	
	return {"done": (obj.size == obj.done), "value" : [status, name, 
	        obj['owner.get_profile.real_name'], obj['points.full_category'], 
			size, points, obj['points.score'], obj['size']]};
}

function document_refresh() {
	$.getJSON('{% url document_pending object.slug %}', function(data) {
		$.each(data, function(key, obj) {
			documents[obj.id]["done"] = obj.done;
		});
		document_build();
	});
}

function document_build() {
    $('#documents').dataTable().fnClearTable(true);
	
	var all_done = 1;
	$.each(documents, function(key, obj) {
		format = document_row(obj);
		$('#documents').dataTable().fnAddData(format.value)
		if (!format.done)
			all_done = 0;
	});
		
	if (all_done == 0)
		setTimeout(document_refresh, 5000);
}

function document_show() {
	$.getJSON('{% url document_by_course object.slug %}', function(data) {
		$.each(data, function(key, obj) {
			documents[obj.id] = obj;
		});
		document_build();
	});
}

function send_vote(s, t) {
	var c = $('#v_category').val();
	var id = $('#v_id').val();
	overlay_reset();
	overlay_title("Upvote");
	overlay_refresh();
	Gload('/vote/' + t + '/' + id + '/' + c + '/' + s, function(data) {
		Iload('{% url course_show object.slug %}');
	});
}

Dcategories = {'R': 'Reference', 'O': 'Official Support',
               'S': 'Summary', 'E': 'Old Exam', 'P': 'Old Project',
               'L': 'Old Solutions', 'D': 'Others'};

function Dvote(id, cat, score, rscore, title) {
	var foo  = '<input type="hidden" id="v_id" value="' + id + '">';
	foo += '<select id="v_category">';
	for (var k in Dcategories)
		if (k == cat) 
			foo += '<option value="' + k + '" selected>' + Dcategories[k] + '</option>';
		else
			foo += '<option value="' + k + '">' + Dcategories[k] + '</option>';
	foo += '</select>';
	bar = '<center><div><input type="button" value="confirm '+score+'" onclick="send_vote('+rscore+', \'doc\');"></div></center>'; 
	overlay_reset();
	overlay_title(title);
	$('#overlay_content').html('This document is really in ' + foo + ' ?<br><br>' + bar);
	overlay_show();
	overlay_refresh();
}

function Dupvote(id, cat) {
	Dvote(id, cat, '+1', 1, 'Upvote');
}

function Ddownvote(id, cat) {
	Dvote(id, cat, '-1', -1, 'Downvote');
}

function thread_show() {
	$.getJSON('{% url thread_list object.id 0 0 %}', function(data) {
		$.each(data, function(key, obj) {
			$('#threads').dataTable().fnAddData([
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

function thread_new() {
	overlay_reset();
	overlay_title("New Thread");
	overlay_form({"id": "new_thread", "url": "{% url thread_post %}",
				  "content": '{{ tform.as_table|escapejs }}', "submit": "post"});
	$('#id_course').val('{{ object.id }}');
	$('#id_document').val(0);
	$('#id_page').val(0);
	overlay_show();
	overlay_refresh();
	$("#new_thread").submit(function() {
		Pload('new_thread', '{% url thread_post %}', function() {
			Iload('{% url course_show object.slug %}');
		});
		return false;
	});
}

$(document).ready(function() {
	$('#documents').dataTable({
		"bPaginate": false,
		"bFilter": false,
		"aaSorting": [[ 5, "desc" ]],
		"bAutoWidth" : false,
		"aoColumns": [ {"bSortable": false}, null, null, null, {"iDataSort": 7}, 
					   {"iDataSort": 6}, {"sType":'numeric', "bVisible":false},
					   {"sType":'numeric', "bVisible":false}]
	});

	$('#threads').dataTable({
		"bPaginate": false,
		"bFilter": false,
		"bAutoWidth" : false,
	});

	document_show();
	thread_show();
	
{% if object in user.get_profile.get_follow %}
	follow_state = 0;
{% else %}
	follow_state = 1;
{% endif %}

	$('#follow').click(function() {
		var url = ['{% url user_unfollow %}', '{% url user_follow %}'];
		var text = ['follow', 'unfollow'];
		$.post(url[follow_state], {'courses': '{{ object.slug }}'}, function(data) {
			if (data == 'ok') {
				$('#follow').html(text[follow_state]);
				follow_state = (follow_state + 1) % 2;
			} else
				alert(data);
		});
	});
});

</script>