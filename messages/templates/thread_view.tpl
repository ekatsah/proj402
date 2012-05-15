{% with first=object.msgs.all|first %}

<div>
  <div id="op_info">
    <strong>{{ first.owner.first_name }} {{ first.owner.last_name }}</strong><br>
    Other stats.<br><br>
    <input type="button" value="reply" onclick="reply({{ first.id }});"/>
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

messages = {
{% for m in object.msgs.all %}
"{{ m.id }}": {"user": "{{ m.owner.first_name }} {{ m.owner.last_name }}",
               "date": "{{ m.date|date:"d/m/y H:i" }}",
               "content": "{{ m.text|escapejs }}"},
{% endfor %}
};

function reply(id) {
	overlay_reset();
	overlay_title("Reply");
	var form = document.createElement('form');
	form.id = 'reply_form';
	form.method = 'post';
	form.action = '{% url message_post %}';
	$(form).append('<input type="hidden" value="{{ csrf_token }} name="csrfmiddlewaretoken"/>');
	$(form).append('<table class="vtop">{{ mform.as_table|escapejs }}</table>');
	$(form).append('<center><input type="submit" value="post" id="fnew_msg"/></center>');
	$(form).append('<p><strong>Reply of the message from '+messages[id].user+'</strong><br>'+messages[id].content+'</p>');
	$('#overlay_content').html(form);
	$('#id_thread').val({{ object.id }});
	$('#id_reference').val(id);
	overlay_show();
	overlay_refresh();
	$(form).submit(function() {
		Pload('reply_form', '{% url message_post %}', function() {
			Iload('{% url thread_view object.id %}');
		});
		return false;
	});
}


</script>
{% endif %}

<div style="clear: both; margin-top: 10px; padding-top: 10px;">
  <hr class="hr_view"/>
</div>

{% endwith %}
