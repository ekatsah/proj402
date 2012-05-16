{% with docs=object.get_docs %}

<script type="text/javascript">

function upload_file() {
	overlay_reset();
	overlay_title("New Document");

	var uform = document.createElement('form');
	uform.id = 'upload_file_form';
	uform.method = 'post';
	uform.enctype = 'multipart/form-data';
	uform.action = '{% url upload_file object.slug %}';
	$(uform).append('<input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken"/>');
	$(uform).append('<table class="vtop">{{ uform.as_table|escapejs }}</table>');
	$(uform).append('<center><input type="submit" value="upload file" id="upload_file"/></center>');

	var hform = document.createElement('form');
	hform.id = 'upload_http_form';
	hform.method = 'post';
	hform.action = '{% url upload_http_file object.slug %}';
	$(hform).append('<input type="hidden" value="{{ csrf_token }}" name="csrfmiddlewaretoken"/>');
	$(hform).append('<table class="vtop">{{ hform.as_table|escapejs }}</table>');
	$(hform).append('<center><input type="submit" value="upload url" id="upload_file"/></center>');

	$('#overlay_content').html("<h1>Upload File</h1>").append(uform);
	$('#overlay_content').append('<hr><h1>Upload From URL</h1>').append(hform);
	overlay_show();
	overlay_refresh();

	$(hform).submit(function() {
		Pload('upload_http_form', '{% url upload_http_file object.slug%}', function(data) {
			Iload('{% url course_show object.slug %}');
		});
		return false;
	});
}


function preview_doc(id, place) {
	if ($('#dprev' + id).length > 0)
		return;
	$('#' + place).after('<tr id="tr_doc_' + id + '"><td class="min2"></td><td colspan=5><div id="dprev'+id+'">loading..</div></td></tr>');
	$('#dprev' + id).load('{% url document_preview 0 %}' + id, function() {});
}

$(document).ready(function() {
	{% for d in docs %}
	$('#doc_row{{ d.id }}').load('{% url row_info d.id %}');
	{% endfor %}

	$.getJSON('{% url thread_list object.id 0 0 %}', function(data) {
		$('#course_forums').html('<table id="comtable" class="thread_list"><tr><th>Subject</th><th>Poster</th><th>#post</th><th>Last Activity</th></tr></table>');
		var found = 0;

		$.each(data, function(key, obj) {
			found = 1;
			var td = '<tr><td><a href="{% url thread_view "'+obj.id+'" %}"';
			td += ' onclick="return Iload(\'{% url thread_view "'+obj.id+'" %}\');">';
			td += obj.subject + '</a></td><td>' + obj.owner_name + '</td><td><center>';
			td += obj.length + '</center></td><td>' + obj.date_max + '</td></tr>';
			$('#comtable').append(td);
		});

		if (found == 0)
			 $('#course_forums').html('No thread found');
	});
});

function send_vote(s, t) {
	var c = $('#v_category').val();
	var id = $('#v_id').val();
	overlay_reset();
	overlay_title("Upvote");
	overlay_refresh();
	$.get('/vote/' + t + '/' + id + '/' + c + '/' + s, function(data) {
		if (data == 'ok') {
			overlay_close();
			$('#doc_row' + id).html('reloading..');
			$('#doc_row' + id).load('{% url row_info 0 %}' + id);
		} else {
			$('#overlay_content').html(data);
			overlay_refresh();
		}
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

</script>

<h1>{{ object.name }}</h1>

{% if docs %}
<h2>Available documents</h2>
<table class="thread_list">
<tr><th></th><th>Name</th><th>Poster</th><th>Type</th><th>Pages</th><th>Score</th></tr>
{% for d in docs %}
<tr id="doc_row{{ d.id }}">
    <td colspan="5"><div>
      <div style="float: left; margin-top: 0px"><img src="/static/loading.gif"></div>
      <div style="float: left; margin-left: 7px; font-size: 11px; margin-top: 2px;"> loading..</div>
    </div></td>
</tr>
{% endfor %}
</table>
{% else %}
<h2>No ressources availible</h2>
{% endif %}

<p><input type="button" onclick="upload_file();" value="upload file"/></p>

<h2>Discussions</h2>
<div id="course_forums" style="margin-bottom: 10px;">loading..</div>
<div><input type="button" onclick="" value="new thread"></div>
<script type="text/javascript">
</script>

{% endwith %}
