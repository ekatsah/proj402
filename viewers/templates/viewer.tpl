{% extends "base.tpl" %}

{% block scripts %}

function construct_b2m() {
	b2m = Array();
	boff = 315; // value of the first margin + pseudo page height
	
	$('.bigimg').each(function(idx) {
		b2m[idx] = boff + 5;
		boff = boff + 17 + $('#bimg' + (1 + idx)).height();
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
		if (idx)
			$(this).width($('#bimg' + idx).width() + 40);
	});
	construct_b2m();
	$('#zv').val(Math.floor(zoom) + '%');
}

function refresh_mpage() {
	$('#mimg' + current_page).css('border', '1px #6ed8ff solid');
	for (current_page = b2m.length; current_page > 0; --current_page)
		if (b2m[current_page] < $('#pright').scrollTop())
			break;
	++current_page;
	$('#mimg' + current_page).css('border', '3px red solid');
	$('#pleft').scrollTop(m2p[current_page - 1]);
}

$(document).ready(function() {
  $('#pages').height($(window).height() - 150);
  zoom = 100;
  current_page = 0;
  construct_sizes();
  construct_b2m();
  construct_m2p();
  refresh_mpage();

  $('.minimg').each(function(idx) {
  	$(this).click(function() {
  		$('#pright').scrollTop(b2m[idx]);
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
});

{% endblock %}

{% block content %}

<div id="pmenu">
  <form action="#" id="zf">
    <span id="zp">Zoom+</span> <span id="zm">Zoom-</span>
    <input class="shadow" style="width: 50px" id="zv" value="100%"/>
    <input type="submit" style="display: none"/>
  </form>
</div>

<div id="pages">
    <div id="pleft"><center>
        {% for p in object.pages.all %}
            <p>page {{ forloop.counter }}</p>
            <img id="mimg{{ forloop.counter }}" class="page minimg"
                src="{% url download_page object.id p.num %}" 
                width="118" height="{% widthratio p.height p.width 118 %}"><br>
        {% endfor %}</center>
    </div>
    <div id="pmiddle"></div>
    <div id="pright"><center>
		<div class="bigpage" style="height: 300px; border: 1px red solid">
		<h1>{{ object.name }}<br>PSEUDO PAGE</h1>
		</div>
            {% for p in object.pages.all %}
                <div class="bigpage" style="width: {{ p.width|add:37 }}">
                    <div class="pbutton">C<br>A</div>
                    
                    <img id="bimg{{ forloop.counter }}"
                        class="page bigimg" src="{% url download_page object.id p.num %}" 
                        width="{{ p.width }}" height="{{ p.height }}"><br>
                </div>
            {% endfor %}
    </center></div>
</div>
{% endblock %}
