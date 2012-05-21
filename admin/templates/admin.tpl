{% load i18n %}
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
    {% url category_tree as category_tree %}
    <li>{% blocktrans %}<a href="#{{ category_tree }}" onclick="return Iload('{{ category_tree }');">
        Category Tree</a> Place to define all the category and the relation
        between them{% endblocktrans %}</li>

    {% url admin_users as admin_users %}
    <li>{% blocktrans %}<a href="#{{ admin_users }}" onclick="return Iload('{{ admin_users }');">
        User Manager</a> Place to see every users, edit some properties.. heck,
        it's the fuck'ng LART!{% endblocktrans %}</li>

    {% url admin_documents as admin_documents %}
    <li>{% blocktrans %}<a href="#{{ admin_documents }}" onclick="return Iload('{{ admin_documents }');">
        Document Manager</a> list of documents{% endblocktrans %}</li>
</ul>
