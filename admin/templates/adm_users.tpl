<script type="text/javascript">

function unset_modo(uid) {
	Gload('{% url user_unset_modo "'+uid" %}, function() {
		$("#pu"+uid).html('<span class="action_link" onclick="set_modo('+uid+');">set</span>');
	});
}

function set_modo(uid) {
	Gload('{% url user_set_modo "'+uid" %}, function() {
		$("#pu"+uid).html('MODO <span class="action_link" onclick="unset_modo('+uid+');">unset</span>');
	});
}

function create_user() {
	overlay_reset();
	overlay_title("Create User");
	var form = document.createElement('form');
	form.id = 'create_user_form';
	form.method = 'post';
	form.action = '{% url user_new %}';
	$(form).append('<input type="hidden" value="{{ csrf_token }} name="csrfmiddlewaretoken"/>');
	$(form).append('<table class="vtop">{{ uform.as_table|escapejs }}</table>');
	$(form).append('<center><input type="submit" value="create" id="create_user"/></center>');
	$('#overlay_content').html(form);
	$('#id_comment').val('Please comment here why you added this user, when, who he is etc');
	overlay_show();
	overlay_refresh();
	$(form).submit(function() {
		Pload('create_user_form', '{% url user_new %}', function() {
			Iload('{% url admin_users %}');
		});
		return false;
	});
}

</script>

<h1>Users</h1>

<table class="thread_list">
<tr><th>#id</th><th>username</th><th>name</th><th>last visit</th><th>moderator</th></tr>
{% for u in object_list %}
<tr><td><center>{{ u.id }}</center></td><td>{{ u.username }}</td><td>{{ u.first_name }} 
        {{ u.last_name }}</td><td>{{ u.last_login }}</td>
    <td><center id="pu{{u.id}}">{% if u.get_profile.moderate %}
    MODO <span class="action_link" onclick="unset_modo({{u.id}});">unset</span>
    {% else %}
    <span class="action_link" onclick="set_modo({{u.id}});">set</span>
    {% endif %}</center></td>
    </tr>
{% endfor %}
</table>

<input type="button" value="create user" onclick="create_user();"/>