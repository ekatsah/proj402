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


{% endwith %}