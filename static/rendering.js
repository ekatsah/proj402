function Box () {
    o = document.createElement("div");

    o.refresh = function() {
    	o.style.left = ($(window).width() / 2 - $(o).width() / 2) + 'px';
	o.style.top = ($(window).height() / 2 - $(o).height() / 2) + 'px';
    };

    o.show = function() {
    	o.refresh();
	document.body.appendChild(o);
	$('#grey').css('display', 'block');
    };
    
    o.close = function() {
    	document.body.removeChild(o);
    	$('#grey').css('display', 'none');
    };

    o._title = document.createElement("h3");
    o._content = document.createElement("p");
    o._close = document.createElement("img");
    o._close.src = "/static/close.png";
    o._close.addEventListener("click", o.close);
    o._close.className = "box_close";
    o.className = "box";
    o.appendChild(o._title);
    o.appendChild(o._content);
    o.appendChild(o._close);
    return o;
};
