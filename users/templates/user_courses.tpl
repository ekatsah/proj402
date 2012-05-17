{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<script langage="javascript">
var courses_list = new Object;

function course_search(e) {
	if ((e.keyCode || e.which) == 13) { // On enter key
		searched = $('#mnemo').val();
		$('#mn_result').html('searching..');

		// HARD_LINK
		$.get('/course/get/' + searched, function(data) {
			but = '<input class="course_add_but" type="button" value="add" onclick="course_add();"/>';
			$('#mn_result').html(but + data);
			overlay_refresh();
		}).error(function(obj) {
			$('#mn_result').html('Course not found');
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

function course_add(e) {
	courses_list[searched] = 1;
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
			} else alert('error : ' + data);
		});
	}
}

</script>

{% if guess %}
<p><strong>Your fellows in <i>{{ user.profile.section }}</i> have chosen : </strong><br>
{{ guess }}</p>
{% endif %}

<p><a href="{% url course_view_all %}" onclick="return Iload('{% url course_view_all %}');">
   View all courses</a></p>

<p><strong>You can add a course by mnemonic : </strong>
<input id="mnemo" type="text" size="5" onkeypress="course_search(event);"/></p>

<p id="mn_result" style="margin-top: 4px; margin-bottom: 4px;"></p>

<p style="display: none" id="c_list_box"><strong>Selected courses : </strong><br><br>
<span id="c_list"></span><br><br><input type="button" value="follow courses" onclick="submit_courses();"/></p>