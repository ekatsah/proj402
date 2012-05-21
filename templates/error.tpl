{% extends "layout.tpl" %}
{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

{% block content %}
<h1>{% trans "A wild error appears!" %}</h1>

<p>
{% blocktrans %}
We are sorry for the inconvenience. Please send an email to 
<a href="mailto:p402@cerkinfo.be">p402@cerkinfo.be</a> describing 
your error. <br>
Don't forget to add your broswer information, the url of the 
error page and all useful informations. Thx!<br><br>
{% endblocktrans %}
{% if msg %}
{% trans "Would you be kind and append this text to your email?" %}<br>
<pre>{{msg}}</pre>
{% endif %}
</p>
{% endblock %}

