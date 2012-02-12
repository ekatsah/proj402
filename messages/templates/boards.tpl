{% for s in params.set.contains.all %}
	<h2>{{ s.name }}</h2>
	<div id="course{{ s.id }}" style="margin-bottom: 10px;">loading..</div>
	<div><input type="button" onclick="new_thread_box({{ s.id }}, 0, 0);" value="new thread"></div>
	<script type="text/javascript">
		$('#course{{ s.id }}').load('{% url list_thread s.id 0 0 %}'); 
	</script>
{% endfor %}