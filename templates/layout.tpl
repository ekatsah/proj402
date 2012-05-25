{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
{% load i18n %}
<html>
    <head>
        <title>PROJ-402</title>
        <script src="/static/jquery-1.7.min.js"></script>
        <link href="/static/header.css" rel="stylesheet" type="text/css">
        <link href="/static/overlay.css" rel="stylesheet" type="text/css">
        <link href="/static/proj402.css" rel="stylesheet" type="text/css">
        {% block header %}
        <style type="text/css">
        	#infos {
        		width: 781px;
        		margin-right: auto;
        		margin-left: auto;
        		margin-top: 50px;
        	}
        	
        	#left {
	        	float: left;
	        	margin: 0px;
	        	width: 340px;
	        	text-align: right;
	        	font-size: 14px;
	        	padding-top: 30px;
	        }
	        
	        #right {
		        float: left;
		        margin-left: 40px;
		        width: 300px;
		        padding: 0px;
		 	}
		</style>
        {% endblock %}
    </head>

    <body>
        <div id="top">
            <h1 id="big_title">
            	P402 <small>alpha</small>
            </h1>
            <p id="slogan">
                {% trans "Bring back real collaboration between students!" %}
            </p>
            {% block links %}
            {% endblock %}
        </div>

        <div id="content">
        {% block content %}
        <div id="infos">
	        <div id="left">
    	    {% blocktrans %}
				<p>Project-402 is a proposed application to <br>help students <strong>share
				   informations</strong> with their fellows. It's stricly for students only.
				   It's under heavy developement and managed by students.</p>
				   
				<p>Why not give it a try? You should <strong>
			   	   <a href="https://www.ulb.ac.be/intranet/p402">login</a></strong>.</p>
			   
				<p>Project-402 is currently open for <strong>sciences</strong> and 
				   <strong>polytech</strong> students. Interested in making this 
				   available for another faculty? Write us<br>an email at 
				   <a href="p402@cerkinfo.be">p402@cerkinfo.be</a>.</p>
	        {% endblocktrans %}
    	    </div>
        	<div id="right">
        		<img src="/static/p402.png"/>
        	</div>
	    </div>
        {% endblock %}
        </div>

        {% block overlay %}
        {% endblock %}
    </body>
</html>
