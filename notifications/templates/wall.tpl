{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}

<h1>All events</h1>

{% for event in object_list %}
	<div style="margin: 20px 10px 10px 10px;">
		<span style="border: 1px #bbb solid; padding: 10px; border-radius: 10px; background-color: #eee">
			{{ event }}
		</span>
	</div>
{% endfor %}
