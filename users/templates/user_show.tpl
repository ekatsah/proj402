<script type="text/javascript">

function join_course(slug) {
    $.get('/user/join/' + slug, function(data) {
        if (data == 'ok') 
            alert("ok");
    });
}

function view_course_box() {
    overlay_reset();
    overlay_title("View course");
    overlay_show();
    
    $.getJSON('{% url courses_all %}', function(data) {
        var items = [];

        $.each(data, function(key, val) {
            S = val.slug;
            // HARD_URL
            items.push('<li><a href="/course/s/' + S + '" onclick="return Iload(\'/course/s/' + S + '\');">' + S + '</a> : ' + 
                val.name + ' <a onclick="join_course(\'' + S + 
                '\');">join</a></li>');
        });

        $('#overlay_content').html($('<ul/>', {
            'class': 'course_list',
            html: items.join('')
        }));
        
        overlay_refresh();
    });
}
</script>

<h1>Hello, {{ user.first_name }} {{ user.last_name }}</h1>

{% if user.profile.welcome %}
<h2>Welcome!</h2>
<p>First time, right? Basic rule : Don't panic.<br><br>

This joint is a mean for student to exchange documents and messages. You can 
see a course with the menu in the top left corner. By clicking on it you will
load some sub categories and courses and by repeting the process you will
eventually find something interesting. You can come back on this page with the
<i>home</i> button (the head of the menu).<br><br>

You should join the courses you want to follow on a daily basis with the
application below. If you want more information, you would probably want to read
<a href="{% url help %}" onclick="return Iload('{% url help %}');">help</a><br><br>

If you want to mask this message, 
<a href="{% url mask_welcome %}" onclick="return Iload('{% url mask_welcome %}');">click here</a></p>
{% endif %}

<p>welcome {{ user.username }}.<br>
You are in {{ user.profile.section }} w/ reg = {{ user.profile.registration }}</p>
<p><input type="button" onclick="view_course_box();" value="view courses"/></p>

