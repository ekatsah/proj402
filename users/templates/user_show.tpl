<script type="text/javascript">

function join_course(slug) {
    $.get('/user/join/' + slug, function(data) {
        if (data == 'ok') 
            alert("ok");
    });
}

function add_course_box() {
    overlay_reset();
    overlay_title("Add course");overlay_refresh();
    $.get('{% url user_courses %}', function(data) {
		$('#overlay_content').html(data);
		overlay_refresh();
    });
    overlay_show();
}

function mask_welcome() {
	Gload('{% url mask_welcome %}', function() {
		$('#welcome_msg').css('display', 'none');
	});
	return false;
}

</script>

<h1>Hello, {{ user.first_name }} {{ user.last_name }}</h1>

{% if user.profile.welcome %}
<div id="welcome_msg">
<h2>First time, right? </h2>
<p>Basic rules : 
<ol><li>Don't panic.</li>
    <li>This project is still highly experimental</li></ol>


This website is a mean for student to exchange documents and messages. You can 
see a course with the menu in the top left corner. By clicking on it you will
load some sub categories and courses and by repeting the process you will
eventually find something interesting. You can come back on this page with the
<i>home</i> button (the head of the menu).<br><br>

You should join the courses you want to follow on a daily basis with the
application below. If you want more information, you would probably want to read
<a href="{% url help %}" onclick="return Iload('{% url help %}');">help</a><br><br>

If you want to mask this message, 
<a href="{% url mask_welcome %}" onclick="return mask_welcome();">click here</a></p>
</div>
{% endif %}

<h2>Courses followed</h2>
{% with courses=user.profile.courses.all %}
{% if courses %}

<table style="border-collapse: collapse;">
<tr><th style="padding: 5px;">Course</th><th style="padding: 5px;">Activity</th></tr>

{% for follow in courses %}
<tr><td style="padding: 5px; text-align: center; border-top: 1px solid black; border-right: 1px solid black">
    <a href="{% url course_show follow.course.slug %}" 
    	onclick="return Iload('{% url course_show follow.course.slug %}');">
    	{{ follow.course.slug }} - {{ follow.course.name }}</a></td>
    <td style="border-top: 1px solid black; padding: 8px"><center>-</center></td></tr>
{% endfor %}
</table>
 
<p>Want to add some courses? <input type="button" onclick="add_course_box();" value="click here"/></p>
{% else %}
<p>You don't follow any courses yet. You sould 
<input type="button" onclick="add_course_box();" value="add some"/></p>
{% endif %}
{% endwith %}

<h2>Profile</h2>
<p>User {{ user.username }}.<br>
You are in {{ user.profile.section }} w/ reg = {{ user.profile.registration }}</p>
