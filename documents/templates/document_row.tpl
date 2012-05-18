{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
{% load can_vote %}

{% if object.size != object.done %}
{% if object.done %}
    <td class="min"><div>
      <div style="float: left; margin-top: 0px"><img src="/static/loading.gif"></div>
      <div style="float: left; margin-left: 7px; font-size: 11px; margin-top: 2px;">{% widthratio object.done object.size 100 %}%</div>
    </div></td>
    <td style="min-width: 300px;">{{ object.name }}</td>
    <td><center>{{ object.owner.username }}</center></td>
    <td><center>{{ object.points.full_category }}</center></td>
    <td><center>{{ object.size }}</center></td>
    <td><center>-</center></td>
{% else %}
    <td class="min">waiting</td>
    <td style="min-width: 300px;">{{ object.name }}</td>
    <td><center>{{ object.owner.username }}</center></td>
    <td><center>{{ object.points.full_category }}</center></td>
    <td><center>-</center></td>
    <td><center>-</center></td>
{% endif %}

<script type="text/javascript">
  window.setTimeout(function() {
    $('#doc_row{{ object.id }}').load('{% url row_info object.id %}');
  }, 5000);
</script>

{% else %}
    <td class="min"><small><span onclick="preview_doc({{ object.id }}, 'doc_row{{ object.id }}');">info</span></small></td>
    <td style="min-width: 300px;"><a href="{% url view_file object.id %}" onclick="return Iload('{% url view_file object.id %}');">{{ object.name }}</a></td>
    <td><center>{{ object.owner.username }}</center></td>
    <td><center>{{ object.points.full_category }}</center></td>
    <td><center>{{ object.size }}</center></td>
    <td><center>{{ object.points.score }} 
    	{% if user|can_voteD:object %}
    	   ( <span onclick="Dupvote({{ object.id }}, '{{ object.category }}');">+</span>
    	   | <span onclick="Ddownvote({{ object.id }}, '{{ object.category }}');">-</span>
    	   ){% endif %}</center></td>
{% endif %}