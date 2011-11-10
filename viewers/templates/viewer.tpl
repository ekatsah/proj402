{% extends "base.tpl" %}

{% block scripts %}

$(document).ready(function() {
  $('#pages').height($(window).height() - 150);
});

{% endblock %}

{% block content %}

<p>view {{ object.name }}.</p>

<div id="pages">
{% for p in object.pages.all %}
    <img class="page" src="{% url download_page object.id p.num %}" 
        width="p.width" height="p.height"><br>
{% endfor %}
</div>
{% endblock %}
