{% extends "base.tpl" %}

{% block scripts %}

function join_course(slug) {
    $.get('/user/join/' + slug, function(data) {
        if (data == 'ok') 
            alert("ok");
    });
}

function add_course_box() {
    course_box = Box(100, 100);
    course_box._title.innerHTML = "Add course";
    course_box._content.innerHTML = "loading..";
    course_box._content.id = "course_box";
    document.body.appendChild(course_box);
    
    $.getJSON('/course/all', function(data) {
        var items = [];

        $.each(data, function(key, val) {
            S = val.fields.slug;
            items.push('<li><a href="/course/s/' + S + '">' + S + '</a> : ' + 
                val.fields.name + ' <a onclick="join_course(\'' + S + 
                '\');">join</a></li>');
        });

        $('#course_box').html($('<ul/>', {
            'class': 'course_list',
            html: items.join('')
        }));
    });
}
{% endblock %}

{% block content %}

<p>welcome {{ user.username }}.</p>
<p><input type="button" onclick="add_course_box();" value="add course"/></p>

{% endblock %}