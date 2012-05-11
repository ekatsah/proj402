Found {{ threads|length }} thread{% if threads|length > 1 %}s{% endif %}.<br><br>

{% if threads %}
<table class="thread_list" >
<tr><th></th><th>Subject</th><th>Poster</th><th>Date</th></tr>
{% for t in threads %}
<tr id="thread_row{{ t.id }}">
  <td class="min"><small>
    <span onclick="preview_thread({{ t.id }}, 'thread_row{{ t.id }}')">view</span>
  </small></td>
  <td style="min-width: 300px;"><a href="{% url view_thread t.id %}" onclick="return Iload('{% url view_thread t.id %}');">{{ t.subject }}</a></td>
  <td>{{ t.poster.username }}</td>
  {% with post=t.msgs.all|first %}
  <td>{{ post.date|date:"d/m/y H:i" }}</td>
  {% endwith %}
</tr>
{% endfor %}
</table>
{% endif %}
