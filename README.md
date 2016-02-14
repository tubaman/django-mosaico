# django-mosaico

djangom-mosaico is a django app that contains the
[mosaico](http://mosaico.io) frontend and implements the mosaico backend
in python.


## Quick start

    1. Add "mosaico" to your `INSTALLED_APPS` setting like this:

    INSTALLED_APPS = [
        ...
        'mosaico',
    ]


    2. Include the mosaico URLconf in your project urls.py like this:

    url(r'^mosaico/', include('mosaico.urls')),

    3. Run `python manage.py migrate` to create the mosaico models.

    4. Visit http://127.0.0.1:8000/mosaico/ to use it.
