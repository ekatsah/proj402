{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<script type="text/javascript">

function add_perm(uid) {
	var perm = $('#sel' + uid).val()
	$.post('{% url user_add_perm %}', {"user_id": uid, "permission": perm}, function(data) {
		 if (data == "ok")
		 	$('#sel' + uid).before('<div id="p' + uid + '_' + perm + '">' + perm + 
		 			' <span class="action_link" onclick="rm_perm(' + uid + ',\'' +
		 			perm + '\');">rm</span></div>');
	});
}

function rm_perm(uid, perm) {
	$.post('{% url user_remove_perm %}', {"user_id": uid, "permission": perm}, function(data) {
		if (data == "ok")
			$('#p' + uid + '_' + perm).remove();
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

<h1>{% trans "Users" %}</h1>

<table id="users" class="sortable">
  <thead>
    <tr>
      <th>{% trans "#id" %}</th>
      <th>{% trans "username" %}</th>
      <th>{% trans "name" %}</th>
      <th>{% trans "last visit" %}</th>
      <th>{% trans "permissions" %}</th>
    </tr>
  </thead>
 
  <tbody>
{% for u in object_list %}
    <tr>
        <td>{{ u.id }}</td>
        <td>{{ u.username }}</td>
        <td>{{ u.first_name }} {{ u.last_name }}</td>
        <td>{{ u.last_login }}</td>
        <td>
        {% for p in u.profile.global_perm %}
        	<div id="p{{u.id}}_{{p.name}}">
        		{{ p.name }} <span class="action_link" onclick="rm_perm({{u.id}}, '{{p.name}}');">rm</span>
        	</div>
        {% endfor %}
        <select id="sel{{u.id}}">{% for p in perms %}<option>{{ p }}</option>{% endfor %}</select>
        <input type="button" value="add" onclick="add_perm({{u.id}});"/>
      </td>
    </tr>
{% endfor %}
  </tbody>
</table>

<input type="button" value="{% trans "create user" %}" onclick="create_user();"/>
