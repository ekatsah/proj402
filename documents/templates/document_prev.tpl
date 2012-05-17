{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
<p>{% if object.description %}{{ object.description }}{% else %}No description{% endif %}</p>
<p><small>
   [ <a href="{% url download_file object.id %}">download file</a> ]
   [ <span onclick="$('#tr_doc_{{ object.id }}').remove();">close</a> ]
</small></p>
