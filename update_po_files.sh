#!/bin/bash

django-admin.py makemessages -a --ignore="ve/*" --settings=settings.py -e html -e tpl
