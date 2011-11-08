{% extends "base.tpl" %}

{% block scripts %}

function upload_file() {
    course_box = Box(100, 100);
    course_box._title.innerHTML = "Upload File";
    course_box._content.innerHTML = 'loading...';
    course_box._content.id = "upload_box";
    document.body.appendChild(course_box);
    
    $.get('/upload/get', function(data) {
        $('#upload_box').html(data);
        $('#upload_form').attr('action', '{% url upload_file object.slug %}');
    });
}

{% endblock %}

{% block content %}

<p>Welcome to <strong>{{ object.name }}</strong>.</p>
<p><input type="button" onclick="upload_file();" value="upload file"/></p>

<h1>Availible ressources</h1>
<ol>
{% for d in object.documents.all %}
<li><a href="{% url download_file d.id %}">{{ d.name }}</a></li>
{% endfor %}
</ol>
{% endblock %}