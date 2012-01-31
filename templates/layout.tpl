<html>
    <head>
        <title>PROJ-402</title>
        <link href="/static/header.css" rel="stylesheet" type="text/css">
        <link href="/static/overlay.css" rel="stylesheet" type="text/css">
        <link href="/static/proj402.css" rel="stylesheet" type="text/css">
        <script src="/static/jquery-1.7.min.js"></script>
        {% block header %}{% endblock %}
    </head>
    
    <body>
        <div id="top">
            <h1>PROJ-402 <small>alpha</small></h1>
            {% block links %}
            {% endblock %}
        </div>
        
        <div id="content">
        {% block content %}
            <p>Project-402 est une tentative d'implémenter la plateforme étudiant
            next-gen de la faculté des sciences. <br>
            Vous devriez vous <a href="{% url profile %}">logger</a></p>
        {% endblock %}
        </div>

        {% block overlay %}
        {% endblock %}
    </body>
</html>