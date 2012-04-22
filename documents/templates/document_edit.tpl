{% with form=object.edit_form %}

<form method="post" action="" id="edit_form">
    {% csrf_token %}   
    <table>
        {{ form.as_table }}
    </table><br>
    <center><input type="submit" value="edit" id="edit" /></center>
</form>

<script langage="javascript">

$("#edit_form").submit(function(event) {
	event.preventDefault(); 
	data = $("form").serialize();
	$.post('{% url edit_post object.id %}', data, function(resp) {
		if (resp == "ok") {
			overlay_close();
			$('#pseudop').html('refreshing..');
			$('#pseudopage').load('{% url document_desc object.id %}');
		} else {
			$('#overlay_content').html(resp);
			overlay_refresh();
		}
	});
});

</script>
{% endwith %}