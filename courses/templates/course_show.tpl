{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

{% include "course_show.js" %}

<h1>{{ object.name }}</h1>

<h2>Available documents</h2>

<table id="documents" class="sortable">
  <thead>
    <tr>
      <th></th>
      <th style="min-width: 200px">Name</th>
      <th>Poster</th>
      <th>Type</th>
      <th>Pages</th>
      <th>Score</th>
      <th style="display: none">RealScore</th>
    </tr>
  </thead>

  <tbody>
  </tbody>
</table>

<p>
  <input type="button" onclick="upload_file();" value="upload file"/>
</p>

<h2>Discussions</h2>

<table id="threads" class="sortable">
  <thead>
    <tr>
      <th style="min-width: 200px">Subject</th>
      <th>Poster</th>
      <th>#post</th>
      <th>Last Activity</th>
    </tr>
  </thead>

  <tbody>
  </tbody>
</table>

<p>
  <input type="button" onclick="thread_new();" value="new thread">
</p>
