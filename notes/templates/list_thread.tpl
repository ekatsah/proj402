There is {{ threads|length }} thread.<br><br>

<table class="thread_list">
<tr><th>Subject</th><th>Poster</th></tr>
{% for t in threads %}
<tr><td style="min-width: 300px;">{{ t.subject }}</td><td>{{ t.poster.username }}</td></tr>
{% endfor %}
</table>