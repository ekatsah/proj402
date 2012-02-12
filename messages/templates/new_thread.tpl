<script type="text/javascript">
function post_thread() {
	return Pload('new_thread_form', '{% url post_thread %}', function() {
		// Course present on the page (ref: boards)
		if ($('#course{{ course.id }}').length == 1)
			$('#course{{ course.id }}').load('{% url list_thread course.id 0 0 %}');
 
		// Present on a page of a doc
		if ($('#pseethread{{ page.id }}').length == 0 && $('#pbut{{ page.id }}').length == 1)
			$('#pbut{{ page.id }}').prepend(
				'<span class="see_threads" onclick="list_thread({{ course.id }}, {% if document %}{{ doc.id }}{% else %}0{% endif %}, {% if doc %}{{ page.id }}{% else %}0{% endif %});">C</span><br>');
	});
}
</script>
<form method="post" action="{% url post_thread %}" id="new_thread_form">
    {% csrf_token %}   
    <table>
        {{ form.as_table }}
    </table><br>
    <center>
      <input type="submit" value="send" id="send" 
          onclick="return post_thread();"/>
    </center>
    <script type="text/javascript">
    $("#id_course").val({{ course.id }});
    $("#id_document").val({% if document %}{{ document.id }}{% else %}0{% endif %});
    $("#id_page").val({% if page %}{{ page.id }}{% else %}0{% endif %});
    </script>
</form>

{% if page %}
<p>This thread is about the page : </p>
<img style="margin-left: 30px; margin-right: 30px; background-color: white"
     src="{% url download_page page.id %}">
{% endif %}
