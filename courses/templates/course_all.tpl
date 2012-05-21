{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<h1>{% trans "Courses list" %}</h1>
<p>{% trans "List of all courses. The blue ones are the courses you follow.<br>
   Click on the others to follow new one" %}</p>

{% if object_list %}
<ul>
  {% for course in object_list|dictsort:"slug" %}
  <li id="li_course_{{course.id}}" class="a_course_li"><div id="course_{{course.id}}"
                          class="a_course_div" onclick="follow({{course.id}}, '{{course.slug}}');">
      <strong>{{ course.slug }}</strong> : {{ course.name }}
  </div></li>
  {% endfor %}
</ul>
{% else %}
<p><i>{% trans "No courses available yet." %}</i></p>
{% endif %}

<script langage="javascript">
{% for cf in user.profile.courses.all %}
$('#course_{{cf.course.id}}').addClass('followed_course_div');
$('#li_course_{{cf.course.id}}').addClass('followed_course_li').append(' <span class="following" style="color: green;"><i>following</i></span>');
{% endfor %}

function follow(id, slug) {
	$.post('{% url user_follow %}', {'courses': slug}, function(data) {
		if (data == 'ok') {
			$('#course_' + id).addClass('followed_course_div');
			$('#li_course_' + id).addClass('followed_course_li');
		}
	});
}

</script>
