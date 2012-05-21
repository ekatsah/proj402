{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<p><strong>{% trans "This feature is not yet functionnal!" %}</strong></p>

{% if msg %}
<p>{{ msg }}</p>

{% else %}

{% if rejected %}
<p><strong>{% trans "Rejected" %}</strong> : {{ rejected|join:', ' }}</p>
{% endif %}

<table style="border-collapse:collapse;">
<tr><th style="width: 100px;">{% trans "Word" %}</th><th>{% trans "Present in" %}</th></tr>

{% for word, docs in word_list %}
<tr><td style="text-align: center; border-top: 1px solid black; border-right: 1px solid black">{{ word }}</td>
    <td style="border-top: 1px solid black; padding: 8px">{% for id, count, wsize, score in docs %}
          Doc #{{id}}, score = {{ score }}, {{ count }}/{{ wsize }}<br>
        {% endfor %}</td></tr>
{% endfor %}
</table>

{% endif %}
