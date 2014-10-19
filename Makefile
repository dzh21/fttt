MANAGE=django-admin.py
SETTINGS=fttt.settings

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test

