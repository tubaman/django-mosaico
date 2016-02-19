from django.conf.urls import url

from .views import index, editor, upload, download, image, template

urlpatterns = [
    url(r'^$', index),
    url(r'^editor.html$', editor),
    url(r'^img/$', image),
    url(r'^upload/$', upload),
    url(r'^dl/$', download),
    url(r'^template/$', template),
]
