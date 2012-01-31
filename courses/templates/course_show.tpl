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

</script>

<p>Welcome to <strong>{{ object.name }}</strong>.</p>
<p><input type="button" onclick="upload_file();" value="upload file"/></p>

{% if object.documents.all %}
<h1>Availible ressources</h1>
<ol>
{% for d in object.documents.all %}
<li><a href="{% url download_file d.id %}">{{ d.name }}</a> - 
    <a href="#{% url view_file d.id %}" onclick="return Iload('{% url view_file d.id %}');">view</a></li>
{% endfor %}
</ol>
{% else %}
<h1>No ressources availible</h1>
{% endif %}