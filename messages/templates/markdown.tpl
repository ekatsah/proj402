{% load markup %}
{{ string|markdown:'nl2br,smart_strong,headerid(level=3),' }}