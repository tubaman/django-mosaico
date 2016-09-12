# django-mosaico

djangom-mosaico is a django app that contains the
[mosaico](http://mosaico.io) frontend and implements the mosaico backend
in python.


## Quick start

   1. Enable the Django [sites framework](https://docs.djangoproject.com/en/1.10/ref/contrib/sites/#enabling-the-sites-framework)
   1. Add "jsonify" and "mosaico" to your `INSTALLED_APPS` setting like this:

       ```python
       INSTALLED_APPS = [
           ...
           'jsonify',
           'mosaico',
       ]
       ```

   1. Include the mosaico URLconf in your project urls.py like this:

       ```python
       url(r'^mosaico/', include('mosaico.urls')),
       ```

   1. Setup [files uploaded by a user during development](https://docs.djangoproject.com/en/1.10/howto/static-files/#serving-uploaded-files-in-development)
   1. Run `python manage.py migrate` to create the mosaico models.
   1. Login to the django admin
   1. Change the [first site](http://127.0.0.1:8000/admin/sites/site/1/change/) in the Django admin to be:
      * domain name - localhost:8000
      * display name - localhost
   1. Go to the Django admin here: http://127.0.0.1:8000/admin/mosaico/template/
   1. Create a new template in mosaico by clicking the `Add Template from Mosaico` button.
   1. When you're done, click "Save to Server".  Now that template should be listed in the Django admin under [templates](http://127.0.0.1:8000/admin/mosaico/template/).
