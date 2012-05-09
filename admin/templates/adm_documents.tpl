<h1>Documents</h1>

<table class="thread_list">
<tr><th>#id</th><th>course</th><th>document</th><th>owner</th></tr>
{% for d in object_list %}
<tr><td>{{ d.id }}</td><td>{{ d.refer.slug }}</td><td>{{ d.name }}</td>
    <td>{{ d.owner.username }}</td></tr>
{% endfor %}
</table>
