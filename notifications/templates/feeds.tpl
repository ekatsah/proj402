{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

{% endcomment %}
<rss version="2.0">
	<channel>
		<title>P402 Feedz</title>
		<link>http://cours.cerkinfo.be</link>
		<description>P402 Student Application</description>

{% for event in events %}
		<item>
			<title>Event {{ event.type }} {{ event.date|date:"d/m/y H:i" }}</title>
			<link>http://cours.cerkinfo.be/{{ event.url }}</link>
			<description>{{ event }}</description>
		</item>
{% endfor %}
	</channel>
</rss>
