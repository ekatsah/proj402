{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

{% include "course_show.js" %}

<span id="follow" class="download_but" style="float: right">
{% if object in user.get_profile.get_follow %}
  unfollow
{% else %}
  follow
{% endif %}
</span>

<h1>{{ object.name }}</h1>

<h2>{% trans "Available documents" %}</h2>

<table id="documents" class="sortable">
  <thead>
    <tr>
      <th></th>
      <th style="min-width: 200px">{% trans "Name" %}</th>
      <th>{% trans "Poster" %}</th>
      <th>{% trans "Type" %}</th>
      <th>{% trans "Pages" %}</th>
      <th class="sorting_desc">{% trans "Score" %}</th>
      <th style="display: none">{% trans "RealScore" %}</th>
      <th style="display: none">{% trans "RealSize" %}</th>
    </tr>
  </thead>

  <tbody>
  </tbody>
</table>

<p>
  <input type="button" onclick="upload_file();" value="{% trans "upload file" %}"/>
</p>

<h2>{% trans "Discussions" %}</h2>

<table id="threads" class="sortable">
  <thead>
    <tr>
      <th style="min-width: 200px">{% trans "Subject" %}</th>
      <th>{% trans "Poster" %}</th>
      <th>{% trans "#post" %}</th>
      <th>{% trans "Last Activity" %}</th>
    </tr>
  </thead>

  <tbody>
  </tbody>
</table>

<p>
  <input type="button" onclick="thread_new();" value="{% trans "new thread" %}">
</p>
