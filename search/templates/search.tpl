<p><strong>This feature is not yet functionnal!</strong></p>

{% if msg %}
<p>{{ msg }}</p>

{% else %}

{% if rejected %}
<p><strong>Rejected</strong> : {{ rejected|join:', ' }}</p>
{% endif %}

<table style="border-collapse:collapse;">
<tr><th style="width: 100px;">Word</th><th>Present in</th></tr>

{% for word, docs in word_list %}
<tr><td style="text-align: center; border-top: 1px solid black; border-right: 1px solid black">{{ word }}</td>
    <td style="border-top: 1px solid black; padding: 8px">{% for id, count, wsize, score in docs %}
          Doc #{{id}}, score = {{ score }}, {{ count }}/{{ wsize }}<br>
        {% endfor %}</td></tr>
{% endfor %}
</table>

{% endif %}
