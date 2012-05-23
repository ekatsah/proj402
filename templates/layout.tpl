{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
{% load i18n %}
<html>
    <head>
        <title>PROJ-402</title>
        <script src="/static/jquery-1.7.min.js"></script>
        <link href="/static/header.css" rel="stylesheet" type="text/css">
        <link href="/static/overlay.css" rel="stylesheet" type="text/css">
        <link href="/static/proj402.css" rel="stylesheet" type="text/css">
        {% block header %}{% endblock %}
    </head>

    <body>
        <div id="top">
            <h1 id="big_title">P402 <small>alpha</small><p id="slogan">{% trans "Bring back real collaboration between students!" %}</p></h1>
            {% block links %}
            {% endblock %}
            <form action="/i18n/setlang/" method="post">
            {% csrf_token %}
            <input name="next" type="hidden" value="{{ redirect_to }}" />
            <select name="language">
            {% get_language_info_list for LANGUAGES as languages %}
            {% for language in languages %}
            <option value="{{ language.code }}">{{ language.name_local }} ({{ language.code }})</option>
            {% endfor %}
            </select>
            <input type="submit" value="Go" />
            </form>
        </div>

        <div id="content">
        {% block content %}
        {% blocktrans %}
            <p>Project-402 is an attempt to make the next-gen student application
            for the (applied) sciences faculty.<br>
            You should <a href="https://www.ulb.ac.be/intranet/p402">login</a></p>
        {% endblocktrans %}
        {% endblock %}
        </div>

        {% block overlay %}
        {% endblock %}
    </body>
</html>
