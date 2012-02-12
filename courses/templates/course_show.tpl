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

</script>

<h1>{{ object.name }}</h1>

{% if object.documents.all %}
<h2>Available documents</h2>
<table class="thread_list">
<tr><th></th><th>Name</th><th>Poster</th></tr>
{% for d in object.documents.all %}
<tr id="doc_row{{ d.id }}">
    <td class="min"><small><span onclick="preview_doc({{ d.id }}, 'doc_row{{ d.id }}');">info</span></small></td>
    <td style="min-width: 300px;"><a href="{% url view_file d.id %}" onclick="return Iload('{% url view_file d.id %}');">{{ d.name }}</a></td>
    <td>{{ d.owner.username }}</td>
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
