<html>
    <head>
        <title>PROJ-402</title>
        <script src="/static/jquery-1.7.min.js"></script>
        <link href="/static/header.css" rel="stylesheet" type="text/css">
        <link href="/static/overlay.css" rel="stylesheet" type="text/css">
        <link href="/static/proj402.css" rel="stylesheet" type="text/css">
        {% block header %}{% endblock %}
    </head>
    
    <body>
        <div id="top">
            <h1 id="big_title">PROJ-402 <small>alpha</small></h1>
            {% block links %}
            {% endblock %}
        </div>
        
        <div id="content">
        {% block content %}
            <p>Project-402 is an attempt to make the next-gen student application
            for the sciences faculty.<br>
            You should <a href="https://www.ulb.ac.be/intranet/p402">login</a></p>
        {% endblock %}
        </div>

        {% block overlay %}
        {% endblock %}
    </body>
</html>
