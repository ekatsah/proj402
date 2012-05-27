{% load markup %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
<script type="text/javascript">

messages = {
{% for m in object.msgs.all %}
"{{ m.id }}": {"user": "{{ m.owner.first_name }} {{ m.owner.last_name }}",
               "date": "{{ m.date|date:"d/m/y H:i" }}",
               "content": "{{ m.text|escapejs }}",
               "rendered": "{{ m.text|markdown:'nl2br,smart_strong,headerid(level=3),'|escapejs }}"},
{% endfor %}
};

first_msg_id = {{ first.id }};

function reply(id) {
	overlay_reset();
	overlay_title("Reply");
	overlay_form({"id": "reply_form", "url": "{% url message_post %}",
				  "content": '{{ mform.as_table|escapejs }}', "submit": "post"});
	$('#reply_form_app').append('<p><strong>Reply of the message from '+messages[id].user+'</strong><br>'+messages[id].rendered+'</p>');
	$('#id_thread').val({{ object.id }});
	$('#id_reference').val(id);
	overlay_show();
	overlay_refresh();
	$('#reply_form').submit(function() {
		var content = $('#id_message').val();
		Pload('reply_form', '{% url message_post %}', function(data) {
			$.post('{% url markdown %}', {"string": content}, function (html) {
				var nid = data.toString().substring(3);
				messages[nid] = {
					"user": "{{ user.first_name }} {{ user.last_name }}",
					"date": "now",
					"content": content,
					"rendered": html
				};
				$('#replies').append('<div id="message_' + nid + '"></div>');
				render(nid);
			});
		});
		return false;
	});
}

function render(id) {
	if (id == first_msg_id)
		return render_first();

	{% if user.get_profile.moderate %}
    var links = '[ <span class="action_link" onclick="edit('+id+');">edit</span>, ' +
				'<span class="action_link" onclick="remove('+id+');">remove</span> ] ';
	{% else %}
	var links = '';
    {% endif %}

	$('#message_' + id).addClass('forums_reply');
	$('#message_' + id).html('<p class="forums_reply_header">' + links + 'On ' + 
					         messages[id].date + ', ' + messages[id].user + ' wrote :</p>');
	$('#message_' + id).append('<p class="forums_reply_p">' + messages[id].rendered + '</p>');
}

function render_first() {
	$('#inner_post').html(messages[first_msg_id].rendered);
}

{% if user.get_profile.moderate %}

function edit(id) {
	overlay_reset();
	overlay_title("Edit");
	overlay_form({"id": "edit_form", "url": "{% url message_edit %}",
				  "content": '{{ eform.as_table|escapejs }}', "submit": "edit"});
	$('#reply_form_app').append('<p><strong>Edit of the message from '+messages[id].user+'</strong><br>'+messages[id].rendered+'</p>');
	$('#id_message').val(messages[id].content);
	$('#id_source').val(id);
	overlay_show();
	overlay_refresh();
	$('#edit_form').submit(function() {
		var content = $('#id_message').val();
		Pload('edit_form', '{% url message_edit %}', function() {
			messages[id].content = content;
			$.post('{% url markdown %}', {"string": content}, function (html) {
				messages[id].rendered = html;
				render(id);
			});
		});
		return false;
	});
}

function remove(id) {
	$.post('{% url message_remove %}', {'id': id}, function(data) {
		if (data == 'ok') {
			if (id == first_msg_id)
				Iload('{% url course_show object.referc.slug %}');
			else {
				delete messages[id];
				$('#message_' + id).remove();
			}
		} else
			alert('remove error : ' + data);
	});
}

{% endif %}

$(document).ready(function() {

{% for m in object.msgs.all %}
	{% if not forloop.first %}
		$('#replies').append('<div id="message_{{ m.id }}"></div>');
		render({{ m.id }});
	{% endif %}
{% endfor %}

{% if object.referp %}
	$('#page_image').load(function () {
		var h = Math.max($('#left_post').height(), $('#right_post').height());
		$('#left_post').height(h);
		$('#right_post').height(h);
	});
{% endif %}
});

</script>
