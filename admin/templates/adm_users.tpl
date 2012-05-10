<script type="text/javascript">

function mcall(url) {
	$.get(url, function(data) {
		if (data != "ok")
			alert("error! " + data);
	});
}

function unset_modo(uid) {
	mcall('{% url user_unset_modo "'+uid" %});
}

function set_modo(uid) {
	mcall('{% url user_set_modo "'+uid" %});
}

</script>

<h1>Users</h1>

<table class="thread_list">
<tr><th>#id</th><th>username</th><th>name</th><th>last visit</th><th>moderator</th></tr>
{% for u in object_list %}
<tr><td><center>{{ u.id }}</center></td><td>{{ u.username }}</td><td>{{ u.first_name }} 
        {{ u.last_name }}</td><td>{{ u.last_login }}</td>
    <td><center>{% if u.get_profile.moderate %}
    MODO <span class="action_link" onclick="unset_modo({{u.id}});">unset</span>
    {% else %}
    <span class="action_link" onclick="set_modo({{u.id}});">set</span>
    {% endif %}</center></td>
    </tr>
{% endfor %}
</table>
