{% extends "layout.tpl" %}
{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

{% block header %}

<script type="text/javascript">
{% include "overlay.js" %}
</script>

<script src="/static/menu.js"></script>

<script src="/static/jquery.address-1.4.min.js"></script>
<script src="/static/datatable-1.9.js"></script>

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

	function dump(obj) {
		var txt = '{';
		for (idx in obj)
			txt += '"' + idx.toString() + '": "' + obj[idx].toString() + '",\n';
		return txt + '}';
	}
	
	function Iload(url) {
		$('#content').html('loading..');
		$.get(url, function(resp) {
			$('#content').html(resp);
		}).error(function(resp) {
			$('#content').html('<h1>{% trans "Error!" %}</h1><pre>'+resp['responseText']+'</pre>');
		});
		
		var exist_url = window.location.toString();
		var target = exist_url.substring(0, exist_url.indexOf('#') + 1) + url;
		current_page = target;
		window.location = target;
		overlay_close();
		return false;
	}

	function Gload(url, func) {
		$.get(url, function(data) {
			if (data.indexOf("ok") == 0)
				func(data);
			else
				alert("{% trans "Error!" %} " + data);
		});
	}

	function Pload(form, url, func) {
		$.post(url, $('#' + form).serialize(), function(data) {
			if (data.indexOf("ok") == 0) {
				func(data);
				overlay_close();
			}
			else
				alert(data);
		});
		return false;
	}

	function url_load() {
		var url = window.location.toString();
		var p = url.indexOf('#');
		if (p != -1) {
			var target = url.substring(p + 1);
			if (target.length > 0) {
				Iload(target);
			}
		} else
			Iload('{% url profile %}');
	}

	$(window).ready(function() {
		$(window).resize(function() {
			$('#content').height($(window).height() - 117);
		});
		$(window).resize();

		current_page = window.location;
		url_load();
		
		// make the title a link to profile
		$('#big_title').css('cursor', 'pointer');
		$('#big_title').click(function() { Iload('{% url profile %}'); });
	});
	
	$.address.externalChange(function(e) {
		if (window.location != current_page)
			url_load();
	});

</script>
{% endblock %}


{% block links %}
  <div id="links">
    <div class="dright">
      <a href="{% url user_logout %}">{% trans "Logout" %}</a>
    </div>

{% if user.get_profile.moderate %}
    <div class="dright">
      <a href="{% url admin_index %}" onclick="return Iload('{% url admin_index %}');">{% trans "Admin" %}</a>
    </div>
{% endif %}

    <div class="dright">
      <input class="search" type="text" value="{% trans "search" %}" name="q" id="search_q">
      <input class="search" type="submit" value="{% trans "go" %}" id="search_go">
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
		$('#content').html('{% trans "searching for" %} "' + query + '"..');
		$('#content').load('{% url search_query %}?q=' + query);
	});
      </script>
    </div>

<dl class="menu" >
  <dt onmouseover="mshow('main_menu')" onmouseout="mhide('main_menu')">
    <a href="{% url profile %}" onclick="return Iload('{% url profile %}');">{% trans "Home" %}</a>
  </dt>
  <dd id="main_menu" onmouseover="mshow2('main_menu')" onmouseout="mhide2('main_menu')">
    <ul>
      <li onclick="mmake(1, 1);"><span>{% trans "Courses" %}</span></li>
      <li><a href="{% url general_boards %}" 
             onclick="return Iload('{% url general_boards %}');">{% trans "General Forums" %}</a></li>
      <li><a href="{% url wall %}" 
             onclick="return Iload('{% url wall %}');">{% trans "Wall" %}</a></li>
      <li><a href="{% url help %}" onclick="return Iload('{% url help %}');">{% trans "Help" %}</a></li>
      <li><a href="https://github.com/ekatsah/proj402">{% trans "Developpement" %}</a></li>
    </ul>
  </dd>
</dl>
</div>
{% endblock %}

{% block content %}
<p><strong>{% trans "Why not zoidberg?" %}</strong></p>
<p>{% trans "If nothing happens, it's probably because you didn't activate javascript." %}</p>
{% endblock %}

{% block overlay %}
<div id="front">
	<div id="grey" onclick="overlay_close()"></div>
	<div id="overlay_box">
		<h3 id="overlay_title"></h3>
		<img src="/static/close.gif" id="overlay_closeb">
		<script type="text/javascript">
		  $('#overlay_closeb').click(overlay_close);
		</script>
		<p id="overlay_content">{% trans "loading.." %}</p>
	</div>
</div>
{% endblock %}
