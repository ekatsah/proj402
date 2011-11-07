<html>
    <head>
        <title>PROJ-402</title>
        <link href="/static/proj402.css" rel="stylesheet" type="text/css">
        <script src="/static/jquery-1.7.min.js"></script>
        <script src="/static/rendering.js"></script>
        <script type="text/javascript">{% block scripts %}{% endblock %}</script>
    </head>
    
    <body>
        <div id="top">
            <h1>PROJ-402</h1>
            {% if user.is_authenticated %}
                <a href="{% url user_show %}">Home</a>
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