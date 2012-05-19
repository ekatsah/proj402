{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
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
	overlay_form({"id": "create_user", "url": "{% url user_new %}",
	              "content": '{{ uform.as_table|escapejs }}', "submit": "create"});
	$('#id_comment').val('Please comment here why you added this user, when, who he is etc');
	overlay_show();
	overlay_refresh();
	$('#create_user').submit(function() {
		Pload('create_user', '{% url user_new %}', function() {
			Iload('{% url admin_users %}');
		});
		return false;
	});
}

$(document).ready(function() {
	$('#users').dataTable({
		"bPaginate": false,
		"bFilter": false,
		"aaSorting": [[ 0, "asc" ]],
		"bAutoWidth" : false,
		"aoColumns": [ {"sType":'numeric'}, null, null, null, null ]
	});
});
</script>

<h1>Users</h1>

<table id="users" class="sortable">
  <thead>
    <tr>
      <th>#id</th>
      <th>username</th>
      <th>name</th>
      <th>last visit</th>
      <th>moderator</th>
    </tr>
  </thead>
 
  <tbody>
{% for u in object_list %}
    <tr>
        <td>{{ u.id }}</td>
        <td>{{ u.username }}</td>
        <td>{{ u.first_name }} {{ u.last_name }}</td>
        <td>{{ u.last_login }}</td>
        <td><center id="pu{{u.id}}">
          {% if u.get_profile.moderate %}
            MODO <span class="action_link" onclick="unset_modo({{u.id}});">unset</span>
          {% else %}
            <span class="action_link" onclick="set_modo({{u.id}});">set</span>
          {% endif %}</center>
      </td>
    </tr>
{% endfor %}
  </tbody>
</table>

<input type="button" value="create user" onclick="create_user();"/>