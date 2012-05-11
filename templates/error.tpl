{% extends "layout.tpl" %}

{% block content %}
<h1>A wild error appears!</h1>

<p>We are sorry for the inconvenience. Please send an email to 
<a href="mailto:p402@cerkinfo.be">p402@cerkinfo.be</a> describing 
your error. <br>
Don't forget to add your broswer information, the url of the 
error page and all useful informations. Thx!<br><br>

{% if msg %}
Would you be kind and append this text to your email?<br>
<pre>{{msg}}</pre>
{% endif %}
</p>
{% endblock %}

