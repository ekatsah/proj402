{% extends "base.tpl" %}

{% block scripts %}

{% endblock %}

{% block content %}

<p>view {{ object.name }}.</p>

{% for p in object.pages.all %}
    <img class="page" src="{% url download_page object.id p.num %}" width="p.width" height="p.height"><br>
{% endfor %}
{% endblock %}