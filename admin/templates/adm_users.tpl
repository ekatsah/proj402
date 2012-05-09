<h1>Users</h1>

<table class="thread_list">
<tr><th>#id</th><th>username</th><th>name</th><th>last visit</th></tr>
{% for u in object_list %}
<tr><td>{{ u.id }}</td><td>{{ u.username }}</td><td>{{ u.first_name }} 
        {{ u.last_name }}</td><td>{{ u.last_login }}</td></tr>
{% endfor %}
</table>
