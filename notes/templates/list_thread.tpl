Found {{ threads|length }} thread{% if threads|length > 1 %}s{% endif %}.<br><br>

{% if threads %}
<table class="thread_list" >
<tr><th></th><th>Subject</th><th>Poster</th></tr>
{% for t in threads %}
<tr id="thread_row{{ forloop.counter }}">
  <td class="min"><small>
    <span onclick="preview_thread({{ t.id }}, 'thread_row{{ forloop.counter }}')">view</span>
  </small></td>
  <td style="min-width: 300px;">{{ t.subject }}</td>
  <td>{{ t.poster.username }}</td>
</tr>
{% endfor %}
</table>
{% endif %}