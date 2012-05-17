{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<h1>Admin</h1>
<ul>
	<li><a href="#{% url category_tree %}" onclick="return Iload('{% url category_tree %}');">
		Category Tree</a> Place to define all the category and the relation 
		between them</li>

	<li><a href="#{% url admin_users %}" onclick="return Iload('{% url admin_users %}');">
		User Manager</a> Place to see every users, edit some properties.. heck, 
		it's the fuck'ng LART!</li>

	<li><a href="#{% url admin_documents %}" onclick="return Iload('{% url admin_documents %}');">
		Document Manager</a> list of documents</li>
</ul>
