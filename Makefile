MANAGE=django-admin.py
SETTINGS=forty_two_tasks.settings

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test
