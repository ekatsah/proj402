function Box (x, y) {
    o = document.createElement("div");
    o._title = document.createElement("h3");
    o._content = document.createElement("p");
    o._close = document.createElement("img");
    o._close.src = "/static/close.png";
    o._close.addEventListener("click", function() {
    	document.body.removeChild(o);
    });
    o._close.className = "box_close";
    o.style.left = x + 'px';
    o.style.top = y + 'px';
    o.className = "box";
    o.appendChild(o._title);
    o.appendChild(o._content);
    o.appendChild(o._close);

    return o;
};
