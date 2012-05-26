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
