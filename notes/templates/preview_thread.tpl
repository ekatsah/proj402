{% with first=object.notes.all|first %}
<!-- FIXME add truncate -->
<p>{{ first.text|escape }}<br><small>
   <a href="{% url view_thread object.id %}" onclick="return Iload('{% url view_thread object.id %}');">view full thread</a></small></p>
{% endwith %}