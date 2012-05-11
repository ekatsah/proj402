{% extends "layout.tpl" %}
{% load url from future %}

{% block content %}

{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

<h1>This form is only for <underline>system accounts</underline></h1>
<p>You <strong>must</strong> use the <strong><a href="https://www.ulb.ac.be/intranet/p402/">NetID</a></strong> system if your are an ULB student.
<br><br><br><br>

If you are an administrator (if not, <a href="https://www.ulb.ac.be/intranet/p402/">click here</a>) : 
<form method="post" action="{% url 'django.contrib.auth.views.login' %}">
{% csrf_token %}
<table>
<tr>
    <td>{{ form.username.label_tag }}</td>
    <td>{{ form.username }}</td>
</tr>
<tr>
    <td>{{ form.password.label_tag }}</td>
    <td>{{ form.password }}</td>
</tr>
</table>

<input type="submit" value="login" />
<input type="hidden" name="next" value="{{ next }}" />
</form>

{% endblock %}