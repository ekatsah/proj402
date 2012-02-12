<script type="text/javascript">
	function reply() {
		overlay_reset();
		overlay_title("Reply");
		overlay_show();
		$('#overlay_content').load('{% url new_message object.id %}', overlay_refresh);
	}
</script>

{% with first=object.msgs.all|first %}
<div>
  <div style="margin-top: 10px; float: left; width: 100px;">
    <strong>{{ first.owner.username }}</strong><br>Other stats.
  </div>

  <div style="float: left; margin-left: 10px;">
    <h2 style="margin-top: 2px;">{{ object.subject }}</h2><div>
    <div style="border: 1px #bbb solid; border-radius: 10px; padding: 15px">{{ first.text }}</div>
  </div>
  
  {% if object.referp %}
  <div style="float: left; margin-left: 10px;">
    This thread is about the page <img src="{% url download_page object.referp.id %}" 
                        width="{{ p.width }}" height="{{ p.height }}">
  </div>
  {% endif %}
</div>

<div style="clear: both; padding: 10px;">
  <input type="button" value="reply" onclick="reply();"/>
</div>

{% for m in object.msgs.all %}{% if not forloop.first %}
<div style="border: 1px #ccc solid; padding: 15px; border-radius: 3px; margin: 3px;">
<p style="margin: 0px"><strong>On {{ m.date|date:"d/m/y H:i" }}, {{ m.owner.username }} wrote : </strong><br>
{{ m.text }}</p>
</div>
{% endif %}{% endfor %}

{% endwith %}