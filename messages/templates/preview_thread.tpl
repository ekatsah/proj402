{% with first=object.msgs.all|first %}
<!-- FIXME add truncate -->
<p>{{ first.text|escape }}</p>
<p><small>
   [ <a href="{% url view_thread object.id %}" onclick="return Iload('{% url view_thread object.id %}');">view full thread</a> ]
   [ <span onclick="$('#tr_thread_{{ object.id }}').remove();">close</a> ]
</small></p>
{% endwith %}