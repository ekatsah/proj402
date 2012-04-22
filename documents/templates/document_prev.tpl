<p>{% if object.description %}{{ object.description }}{% else %}No description{% endif %}</p>
<p><small>
   [ <a href="{% url download_file object.id %}">download file</a> ]
   [ <span onclick="$('#tr_doc_{{ object.id }}').remove();">close</a> ]
</small></p>
