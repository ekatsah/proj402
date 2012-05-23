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
        </div>

        <div id="content">
        {% block content %}
        {% blocktrans %}
            <p>Project-402 is an attempt to make the next-gen student application
            for the (applied) sciences faculty.<br>
            You should <a href="https://www.ulb.ac.be/intranet/p402">login</a></p>
        {% endblocktrans %}
        <!--[if IE]>
        <p style="background-color: #FFC285; padding: 10px; padding-left:15px; border: 2px solid red;">
        {% blocktrans %}
		Warning ! We know that there are some problems with Internet Explorer,
		this website might be unusable.<br>
		Please choose an decent/real web browser like :
		{% endblocktrans %}
		<a href="https://www.mozilla.org/fr/firefox/new/">FireFox</a>, <a href="https://www.google.com/chrome?hl=fr">Google Chrome</a>, <a href="http://www.opera.com/">Opera</a>.
		{% trans "Thanks" %} !
		</p><![endif]-->
        {% endblock %}
        </div>

        {% block overlay %}
        {% endblock %}
    </body>
</html>
