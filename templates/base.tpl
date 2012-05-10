{% extends "layout.tpl" %}

{% block header %}
<script src="/static/overlay.js"></script>
<script src="/static/menu.js"></script>
<script src="/static/messages.js"></script>

<script type="text/javascript">

// From https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
jQuery(document).ajaxSend(function(event, xhr, settings) {
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	function sameOrigin(url) {
		var host = document.location.host; // host + port
		var protocol = document.location.protocol;
		var sr_origin = '//' + host;
		var origin = protocol + sr_origin;
		return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		       (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
		       !(/^(\/\/|http:|https:).*/.test(url));
	}
	function safeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
});

	URL_CAT_SUB = '{% url category_sub 0 %}';
	URL_COURSES_CAT = '{% url courses_by_cat 0 %}';

	function Iload(url) {
		$('#content').html('loading..');
		$.get(url, function(resp) {
			$('#content').html(resp);
		}).error(function(resp) {
			$('#content').html('<h1>ERROR</h1><pre>'+resp['responseText']+'</pre>');
		});
		window.location = '/zoidberg#' + url;
		overlay_close();
		return false;
	}

	function Pload(form, url, func) {
		$.post(url, $('#' + form).serialize(), function(data) {
			if (data.indexOf("ok") == 0) {
				func();
				overlay_close();
			}
			else
				alert(data);
		});
		return false;
	}

	$(window).ready(function() {
		$(window).resize(function() {
			$('#content').height($(window).height() - 117);
		});
		$(window).resize();

		var url = window.location.toString();
		var p = url.indexOf('#');
		if (p != -1) {
			var target = url.substring(p + 1);
			if (target.length > 0) {
				Iload(target);
				return true;
			}
		}
		
		Iload('{% url profile %}');
	});
</script>
{% endblock %}


{% block links %}
  <div id="links">
    <div class="dright">
      <a href="{% url user_logout %}">Logout</a>
    </div>

{% if user.get_profile.moderate %}
    <div class="dright">
      <a href="{% url admin_index %}" onclick="return Iload('{% url admin_index %}');">Admin</a>
    </div>
{% endif %}

    <div class="dright">
      <input type="text" value="search" name="q" id="search_q">
      <input type="submit" value="go" id="search_go">
      <script type="text/javascript">
	var search_clicked = 0; 
	$('#search_q').focus(function() {
		if (!search_clicked) {
			search_clicked = 1;
			$('#search_q').val('');
			$('#search_q').css('color', 'black');
		}
	});
	$('#search_go').click(function() {
		var query =  $('#search_q').val().replace(/ /g, '+');
		$('#content').html('searching for "' + query + '"..');
		$('#content').load('{% url search_query %}?q=' + query);
	});
      </script>
    </div>

<dl class="menu" >
  <dt onmouseover="mshow('main_menu')" onmouseout="mhide('main_menu')">
    <a href="{% url profile %}" onclick="return Iload('{% url profile %}');">Home</a>
  </dt>
  <dd id="main_menu" onmouseover="mshow2('main_menu')" onmouseout="mhide2('main_menu')">
    <ul>
      <li onclick="mmake(1, 1);"><span>Courses</span></li>
      <li><a href="{% url general_boards %}" 
             onclick="return Iload('{% url general_boards %}');">General Forums</a></li>
      <li><span>Walls</span></li>
      <li><a href="{% url help %}" onclick="return Iload('{% url help %}');">Help</a></li>
      <li><a href="https://github.com/ekatsah/proj402">Developpement</a></li>
    </ul>
  </dd>
</dl>
</div>
{% endblock %}

{% block content %}
<p><strong>Why not zoidberg?</strong></p>
<p>If nothing happens, it's probably because you didn't activate javascript.</p>
{% endblock %}

{% block overlay %}
<div id="front">
	<div id="grey"></div>
	<div id="overlay_box">
		<h3 id="overlay_title"></h3>
		<img src="/static/close.gif" id="overlay_closeb">
		<script type="text/javascript">
		  $('#overlay_closeb').click(overlay_close);
		</script>
		<p id="overlay_content">loading..</p>
	</div>
</div>
{% endblock %}
