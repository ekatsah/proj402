Wat?
====

This django project is a website providing mean for students to exchange courses and tips.

Dependencies
============

You'll need pyPdf, django-south, poppler (the binary 'pdftotext') and ImageMagick (the binary 'convert')

Installation using virtualenv
=============================

To install:

    virtualenv --distribute --no-site-packages ve
    source ve/bin/activate
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py migrate

You still need to install poppler/pdftotext and ImageMagick/convert using your distribution packages.

To run:

    python manage.py runserver

Then go http://localhost:8000/help

License
=======

Copyright 2011, hast. All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Create a 'fake' user to use without NetID
=========================================
    $ ./manage.py shell
    >>> from django.contrib.auth.models import User
    >>> user = User.objects.create_user('netid', 'email', 'password')
    >>> user.last_name="NAME"
    >>> user.first_name="firstname"
    >>> user.save()
    >>> user_profile = user.profile
    >>> user_profile.registration = "ulb:etudiants:<matricul>"
    >>> user_profile.section = "fac:section"
    >>> user_profile.save()
    >>> user.save()
