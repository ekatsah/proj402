{% if user.get_profile.moderate %}
<img style="margin-top: -1px; float: left" src="/static/edit.png" id="edit_but"/>
{% endif %}
<h1>{{ object.name }}</h1>
<p>Document uploaded by {{ object.owner.username }} on {{ object.date|date:"d/m/y H:i" }}<br>
This document is classed in {{ object.points.full_category }}<br><br>
{{ object.description }}</p>
 
<script langage="javascript">

$('#edit_but').click(function(event) {
	overlay_reset();
	overlay_title("Edit Document");
	overlay_show();
	$.get('{% url document_edit object.id %}', function(data) {
		$('#overlay_content').html(data);
		overlay_refresh();
	});
});

</script>
