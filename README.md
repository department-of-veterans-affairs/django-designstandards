django-designstandards
======================

Django base templates that include the joint USDS and 18F US Web Design
Standards. The US Web Design Standards are an Open source UI components
and visual style guide to create consistency and beautiful user experiences
across U.S. federal government websites.

## Install

Add to requirements.txt:

    -e git+https://github.com/department-of-veterans-affairs/django-designstandards.git#egg=designstandards

Add `'designstandards'` to `INSTALLED_APPS` in settings.

Make your templates extend from the base template in this app:

    {% extends "designstandards/base.html" %}

OR include the same JS and CSS files as in (designstandards/templates/designstandards/base.html)[designstandards/templates/designstandards/base.html].
