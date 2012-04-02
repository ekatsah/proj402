{% with docs=object.documents.all %}

<script type="text/javascript">

function upload_file() {
	overlay_reset();
	overlay_title("Upload File");
	overlay_show();
	$.get('{% url upload_form %}', function(data) {
		$('#overlay_content').html(data);
		$('#upload_form').attr('action', '{% url upload_file object.slug %}');
		overlay_refresh();
    	});
}

function preview_doc(id, place) {
	if ($('#dprev' + id).length > 0)
		return;
	$('#' + place).after('<tr id="tr_doc_' + id + '"><td class="min2"></td><td colspan=2><div id="dprev'+id+'">loading..</div></td></tr>');
	$('#dprev' + id).load('{% url preview_doc 0 %}' + id, function() {});
}

$(document).ready(function() {
	{% for d in docs %}
	$('#doc_row{{ d.id }}').load('{% url row_info d.id %}');
	{% endfor %}
});

</script>

<h1>{{ object.name }}</h1>

{% if docs %}
<h2>Available documents</h2>
<table class="thread_list">
<tr><th></th><th>Name</th><th>Poster</th><th>Type</th><th>Pages</th></tr>
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
<div id="course{{ object.id }}" style="margin-bottom: 10px;">loading..</div>
<div><input type="button" onclick="new_thread_box({{ object.id }}, 0, 0);" value="new thread"></div>
<script type="text/javascript">
	$('#course{{ object.id }}').load('{% url list_thread object.id 0 0 %}'); 
</script>

{% endwith %}
