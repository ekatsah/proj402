{% if object.size != object.done %}
    <td class="min"><div>
      <div style="float: left; margin-top: 0px"><img src="/static/loading.gif"></div>
      <div style="float: left; margin-left: 7px; font-size: 11px; margin-top: 2px;">{% widthratio object.done object.size 100 %}%</div>
      <script type="text/javascript">
	window.setTimeout(function() {
	  $('#doc_row{{ object.id }}').load('{% url row_info object.id %}');
	}, 5000);
      </script>
    </div></td>
    <td style="min-width: 300px;">{{ object.name }}</td>
    <td><center>{{ object.owner.username }}</center></td>
    <td><center>{{ object.points.full_category }}</center></td>
    <td><center>{{ object.size }}</center></td>
{% else %}
    <td class="min"><small><span onclick="preview_doc({{ object.id }}, 'doc_row{{ object.id }}');">info</span></small></td>
    <td style="min-width: 300px;"><a href="{% url view_file object.id %}" onclick="return Iload('{% url view_file object.id %}');">{{ object.name }}</a></td>
    <td><center>{{ object.owner.username }}</center></td>
    <td><center>{{ object.points.full_category }}</center></td>
    <td><center>{{ object.size }}</center></td>
{% endif %}