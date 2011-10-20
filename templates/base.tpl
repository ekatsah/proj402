<html>
    <head>
        <title>PROJ-402</title>
        <link href="/static/proj402.css" rel="stylesheet" type="text/css">
    </head>
    
    <body>
        <div id="top">
            <h1>PROJ-402</h1>
            {% if user.is_authenticated %}
                <a href="{% url user_logout %}">Logout</a>
            {% else %}
                <a href="{% url user_show %}">Login</a>
            {% endif %}
        </div>
        
        <div id="content">
        {% block content %}
            <p>Project-402 est une tentative d'implémenter la plateforme étudiant
            next-gen de la faculté des sciences. </p>
        {% endblock %}
        </div>
    </body>
</html>