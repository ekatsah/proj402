{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
{% with pages=object.all_pages %}

<script type="text/javascript">

img_urlz = { {% for p in pages %}"#bimg{{ forloop.counter }}":"{%url download_page p.id %}",{% endfor %} '0': '0'};
mini_urlz = { {% for p in pages %}"mimg{{ forloop.counter }}":"{%url download_mpage p.id %}",{% endfor %} '0': '0'};

function load_image(id) {
	elem = '#bimg' + id;
	if ($(elem) != undefined && $(elem).attr('src') == '/static/blank.png')
		$(elem).attr('src', img_urlz[elem]);
}

function construct_b2m() {
	b2m = Array();
	// value of the first margin + pseudo page height
	boff = $('#pseudopage').height() + 15;
	
	$('.bigimg').each(function(idx) {
		b2m[idx] = boff + 5;
		boff = boff + 17 + $('#bpa' + (1 + idx)).height();
	});
}

function construct_m2p() {
	m2p = Array();
	boff = 0; // value of the first margin + pseudo page height
	
	$('.minimg').each(function(idx) {
		m2p[idx] = boff + 5;
		boff = boff + 47 + $('#mimg' + (1 + idx)).height();
	});
}

function construct_sizes() {
	sizes = Array();
	$('.bigimg').each(function(idx) {
		sizes[idx] = {'width': $('#bimg' + (1 + idx)).width(),
			      'height': $('#bimg' + (1 + idx)).height() };
	});
}

function pzoom() {
	$('.bigimg').each(function(idx) {
		$(this).width(sizes[idx].width * zoom /100);
		$(this).height(sizes[idx].height * zoom /100);
	});
	$('.bigpage').each(function(idx) {
		$(this).width($('#bimg' + (1 + idx)).width() + 2);
	});
	construct_b2m();
	$('#zv').val(Math.floor(zoom) + '%');
}

function refresh_mpage() {
	$('#mimg' + current_page).css('border', '1px #555 solid');
	for (current_page = b2m.length; current_page > 0; --current_page)
		if (b2m[current_page] < $('#pright').scrollTop())
			break;
	++current_page;
	$('#mimg' + current_page).css('border', '3px #5080ff solid');
	$('#pleft').scrollTop(m2p[current_page - 1]);
	if (backup_current_page != current_page) {
		// FIXME take account of page height!!
		var n = current_page - 2, t = current_page + 2;
		for (; n < t; ++n)
			load_image(n);
		backup_current_page = current_page;
	}
}

function doc_thread() {
	overlay_reset();
	overlay_title("New Thread");
	overlay_form({"id": "new_thread", "url": "{% url thread_post %}",
				  "content": '{{ tform.as_table|escapejs }}', "submit": "post"});
	$('#new_thread_app').append('<p>This thread is about the document : <strong>{{ object.name }}</strong></p>');
	$('#id_course').val({{ object.refer.id }});
	$('#id_document').val({{ object.id }});
	$('#id_page').val(0);
	overlay_show();
	overlay_refresh();
	$('#new_thread').submit(function() {
		Pload('new_thread', '{% url thread_post %}', function() {
			if ($('#doc_cfront').length == 0)
				$('#doc_comment').html('<div id="doc_cfront" class="doc_com" onclick="doc_show_thread();">Read the comment</div>');
			else if ($('#doc_comCTR').length == 0)
				$('#doc_comment').html('<div id="doc_cfront" class="doc_com" onclick="doc_show_thread();">Read the <span id="doc_comCTR">2</span>comments</div>');
			else
				$('#doc_comCTR').html(parseInt($('#doc_comCTR').html()) + 1);
		});
		return false;
	});
}

function doc_show_thread() {
	$('#com_content').html('<strong>Loading..</strong>');
	$('#com_content').css('display', 'block');
	$.getJSON('{% url thread_list object.refer.id object.id 0 %}', function(data) {
		$('#com_content').html('<h1>Threads about this document : </h1><table id="comtabledoc" class="thread_list"><tr><th>Subject</th><th>Poster</th><th>#post</th><th>Last Activity</th></tr></table>');
		$.each(data, function(key, obj) {
			var td = '<tr><td><a href="{% url thread_view "'+obj.id+'" %}"';
			td += ' onclick="return Iload(\'{% url thread_view "'+obj.id+'" %}\');">';
			td += obj.subject + '</a></td><td>' + obj.owner_name + '</td><td><center>';
			td += obj.length + '</center></td><td>' + obj.date_max + '</td></tr>';
			$('#comtabledoc').append(td);
		});
	});
}	
	
function page_thread(pid) {
	overlay_reset();
	overlay_title("New Thread");
	overlay_form({"id": "new_thread", "url": "{% url thread_post %}",
				  "content": '{{ tform.as_table|escapejs }}', "submit": "post"});
	$('new_thread_app').append('<p>This thread is about the page : <br><center><img src="{% url download_page "'+pid+'" %}" style="max-height: 400px;"/></center></p>');
	$('#overlay_content').html(form);
	$('#id_course').val({{ object.refer.id }});
	$('#id_document').val({{ object.id }});
	$('#id_page').val(pid);
	overlay_show();
	overlay_refresh();
	$(form).submit(function() {
		Pload('new_thread', '{% url thread_post %}', function() {
			var jq = $('#cntr' + pid);
			var jq2 = $('#cntk' + pid);
			if (jq.length)
				jq.html(parseInt(jq.html()) + 1);
			else if (jq2.length)
				jq2.html('<div class="white" onclick="page_show('+pid+');" id="cntk'+pid+'">Read the <span id="cntk'+pid+'">2</span> comments</div>');
			else {
				$('#read'+pid).append('<img style="margin-bottom: -12px; margin-top: -8px;" src="/static/com-middle.png"/>');
				$('#read'+pid).append('<div class="white" onclick="page_show('+pid+');" id="cntk'+pid+'">Read the comment</div>');
			}
		});
		return false;
	});
}

function page_show(pid) {
	$('#comfront' + pid).html('<strong>Loading..</strong>');
	$('#comfront' + pid).css('display', 'block');
	$.getJSON('{% url thread_list object.refer.id object.id "'+pid" %}, function(data) {
		$('#comfront' + pid).html('<table id="comtable'+pid+'" class="thread_list"><tr><th>Subject</th><th>Poster</th><th>#post</th><th>Last Activity</th></tr></table>');
		$.each(data, function(key, obj) {
			var td = '<tr><td><a href="{% url thread_view "'+obj.id+'" %}"';
			td += ' onclick="return Iload(\'{% url thread_view "'+obj.id+'" %}\');">';
			td += obj.subject + '</a></td><td>' + obj.owner_name + '</td><td><center>';
			td += obj.length + '</center></td><td>' + obj.date_max + '</td></tr>';
			$('#comtable' + pid).append(td);
		});
	});
}

$(document).ready(function() {
  $(window).resize(function() {
  	$('#pages').height($(window).height() - 155);
  });
  $(window).resize();

  zoom = 100;
  current_page = 0;
  backup_current_page = 0;
  construct_sizes();
  construct_b2m();
  construct_m2p();
  refresh_mpage();

  $('.minimg').each(function(idx) {
  	$(this).click(function() {
  		$('#pright').scrollTop(b2m[idx] + 2);
  	});
  });

  $('#zp').click(function() {
  	if (zoom < 250)
  		zoom += 25;
	else
	  	zoom = zoom * 1.1;
  	pzoom();
  });

  $('#zm').click(function() {
  	if (zoom < 250)
  		zoom -= 25;
  	else
	  	zoom = zoom * 0.9;
  	if (zoom < 10)
  		zoom = 10;
  	pzoom();
  });

  $('#zf').submit(function() {
  	zoom = $('#zv').val();
  	var i = zoom.indexOf("%");
  	if (i != -1)
  		zoom = zoom.substring(0, i);
  	zoom = Number(zoom)
  	if (zoom == NaN)
  		zoom = 100;
  	if (zoom < 10)
  		zoom = 10;
  	pzoom();
  });

  $('#pright').scroll(refresh_mpage);

{% if user.get_profile.moderate %}
  $('#edit_but').click(function(event) {
          overlay_reset();
          overlay_title("Edit Document");
          var form = document.createElement('form');
          form.id = 'edit_form';
          form.method = 'post';
          form.action = '{% url document_edit object.id %}';
          $(form).append('<input type="hidden" value="{{ csrf_token }} name="csrfmiddlewaretoken"/>');
          $(form).append('<table class="vtop">{{ eform.as_table|escapejs }}</table>');
          $(form).append('<center><input type="submit" value="edit" id="edit_button"/></center>');
          $('#overlay_content').html(form);
          overlay_show();
          overlay_refresh();
          $(form).submit(function() {
              Pload('edit_form', '{% url document_edit object.id %}', function(data) {
                  $.getJSON('{% url document_desc object.id %}', function(doc) {
                      $('#doc_name').html(doc.name);
                      $('#doc_desc').html(doc.description);
                      });
                  });
              return false;
              });
  });
{% endif %}

function load_min(i) {
    $('#mimg'+i).attr('src', mini_urlz['mimg'+i]);
    if (i < {{ object.size }})
        setTimeout(function() { load_min(i+1); }, 10);
}
setTimeout(function () { load_min(1); }, 10);

});

</script>

<div id="pmenu">
  <form action="#" id="zf">
    <a class="back_but" href="{% url course_show object.refer.slug %}"
       onclick="return Iload('{% url course_show object.refer.slug %}');">&lt;&lt; back to course</a>
    <a class="download_but" href="{% url download_file object.id %}">Download</a>
    <div style="float: left; margin-top: 2px"><img src="/static/l_plus.png" id="zp"/>&nbsp;&nbsp;&nbsp;<img src="/static/l_minus.png" id="zm"/></div>&nbsp;
    &nbsp;&nbsp;<input class="shadow" style="width: 50px" id="zv" value="100%"/>
    <input type="submit" style="display: none"/>&nbsp;&nbsp;&nbsp;
  </form>
</div>

<div id="pages">
    <div id="pleft"><center>
        {% for p in pages %}
            <p>page {{ forloop.counter }}</p>
            <img id="mimg{{ forloop.counter }}" class="page minimg"
                src="/static/blank.png"
                width="118" height="{% widthratio p.height p.width 118 %}"><br>
        {% endfor %}</center>
    </div>
    <div id="pmiddle"></div>
    <div id="pright"><center>
        <div id="pseudopage">
        {% if user.get_profile.moderate %}
            <img style="margin-top: -1px; float: left; cursor: pointer"
                src="/static/edit.png" id="edit_but"/>
        {% endif %}
            <h1 id="doc_name">{{ object.name }}</h1>
            <p>Document uploaded by {{ object.owner.username }} on {{ object.date|date:"d/m/y H:i" }}<br>
            This document is classed in {{ object.points.full_category }}<br><br>
            <span id="doc_desc">{{ object.description }}</span></p>

            <div id="doc_comadd" class="doc_com" onclick="doc_thread();">Add comment on the whole document</div>
            <div id="doc_comment">
            {% with c=object.threads.all|length %}
            {% if c == 1 %}
            <div id="doc_cfront" class="doc_com" onclick="doc_show_thread();">Read the comment</div>
            {% endif %}{% if c > 1 %}
            <div id="doc_cfront" class="doc_com" onclick="doc_show_thread();">Read the <span id="doc_comCTR">{{ c }}</span> comments</div>
            {% endif %}
            {% endwith %}
            </div>
            <div id="com_content">
            </div>
        </div>

            {% for p in pages %}
                <div id="bpa{{ forloop.counter }}" class="bigpage" style="width: {{ p.width|add:2 }}">
                    <img id="bimg{{ forloop.counter }}"
                        class="page bigimg" src="/static/blank.png"
                        width="{{ p.width }}" height="{{ p.height }}">

                    <div class="comment_front"><div id="comfront{{ p.id }}" class="cominside">
                    </div></div>
                    <div class="comments">
                         <img style="float: left; margin-top: -8px" src="/static/com-left.png"/>
                         <div class="white" onclick="page_thread({{p.id}});">Add comment</div>
                         <div id="read{{p.id}}" style="display: inline">
                         {% if p.threads.all %}
                         <img style="margin-bottom: -12px; margin-top: -8px;" src="/static/com-middle.png"/>
                         {% with c=p.threads.all|length %}
                         {% if c == 1 %}
                         <div class="white" onclick="page_show({{p.id}});" id="cntk{{p.id}}">Read the comment</div>
                         {% else %}
                         <div class="white" onclick="page_show({{p.id}});">Read the <span id="cntr{{p.id}}">{{ c }}</span> comments</div>
                         {% endif %}
                         {% endwith %}
                         {% endif %}
                         </div>
                         <img style="float: right; margin-top: -8px" src="/static/com-right.png"/>
                    </div>
                </div>
            {% endfor %}
    </center></div>
</div>
{% endwith %}
