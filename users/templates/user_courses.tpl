{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
{% load i18n %}
<script langage="javascript">
var courses_list = new Object;

function course_search(e) {
	if ((e.keyCode || e.which) == 13) { // On enter key
		searched = $('#mnemo').val();
		$('#mn_result').html('{% trans "searching.." %}');

		$.getJSON('{% url course_get "'+searched+'" %}', function(data) {
			var but = '<input class="course_add_but" type="button" value="{% trans "add" %}" onclick="course_add(\''+data.slug+'\');"/>';
			if (data.description != '')
				var desc = ': ' + data.description;
			else
				var desc = '';
			$('#mn_result').html(but + data.slug + ' ' + data.name + desc);
			overlay_refresh();
		}).error(function(obj) {
			$('#mn_result').html('{% trans "Course not found" %}');
			overlay_refresh();
		});
	}
}

function clist_refresh() {
	var text = '';
	var empty = 1;
	for (var course in courses_list) {
		if (!empty)
			text += ',';
		text += ' ' + course + ' <input style="margin-bottom: 3px; mar';
		text += 'gin-right: 0px" class="course_add_but" type="button" ';
		text += 'value="del" onclick="course_del(\''+course+'\');"/> ';
		empty = 0;
	}
	if (!empty) {
		$('#c_list_box').css('display', 'block');
		$('#c_list').html(text);
	} else {
		$('#c_list_box').css('display', 'none');
	}
	overlay_refresh();
}

function course_add(c) {
	courses_list[c] = 1;
	clist_refresh();
}

function course_del(c) {
	delete courses_list[c];
	clist_refresh();
}

function submit_courses() {
	var text = '';
	var empty = 1;
	for (var course in courses_list) {
		if (!empty)
			text += '+';
		text += course;
		empty = 0;
	}
	if (!empty) {
		$.post('{% url user_follow %}', {'courses': text}, function(data) {
			if (data == 'ok') {
				courses_list = new Object;
				overlay_close();
				Iload('{% url profile %}');
			} else alert('{% trans "error" %} : ' + data);
		});
	}
}

</script>

{% if guess %}
<p><strong>{% trans "Your fellows in" %} <i>{{ user.profile.section }}</i> {% trans "have chosen" %} : </strong><br>
{{ guess }}</p>
{% endif %}

<p><a href="{% url course_view_all %}" onclick="return Iload('{% url course_view_all %}');">
   {% trans "View all courses" %}</a></p>

<p><strong>{% trans "You can add a course by mnemonic" %} : </strong>
<input id="mnemo" type="text" size="10" onkeypress="course_search(event);"/></p>

<p id="mn_result" style="margin-top: 4px; margin-bottom: 4px;"></p>

<p style="display: none" id="c_list_box"><strong>{% trans "Selected courses" %} : </strong><br><br>
<span id="c_list"></span><br><br><input type="button" value="{% trans "follow courses" %}" onclick="submit_courses();"/></p>