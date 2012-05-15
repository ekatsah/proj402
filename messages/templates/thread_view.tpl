{% with first=object.msgs.all|first %}

<div>
  <div id="op_info">
    <strong>{{ first.owner.first_name }} {{ first.owner.last_name }}</strong><br>
    Other stats.<br><br>
    <input type="button" value="reply" onclick="reply();"/>
  </div>

  <div id="outer_post">
    <small>Posted in
      <a href="{% url course_show object.referc.slug %}" 
         onclick="return Iload('{% url course_show object.referc.slug %}');">
        {{ object.referc.name }}
      </a>
      {% if object.referd %} :: 
        <a href="{% url view_file object.referd.id %}" 
           onclick="return Iload('{% url view_file object.referd.id %}');">
          {{ object.referd.name }}
        </a>
      {% endif %}
    </small>

    <h2>{{ object.subject }}</h2>

    {% if object.referp %}
    	<div id="left_post">
    	  <div id="inner_post">{{ first.text }}</div>
    	</div>
    	
    	<div id="right_post">
    	  About page<br>
	  <img id="page_image" src="{% url download_mpage object.referp.id %}"/> 
	</div>
    {% else %}
	<div id="inner_post" class="real_inner_post">{{ first.text }}</div>
    {% endif %}
  </div>
</div>

{% if object.referp %}
<script type="text/javascript">
	var h = Math.max($('#left_post').height(), $('#right_post').height());
	$('#left_post').height(h);
	$('#right_post').height(h);
</script>
{% endif %}

<div style="clear: both; margin-top: 10px; padding-top: 10px;">
  <hr class="hr_view"/>
</div>

{% endwith %}
