from __future__ import unicode_literals
import posixpath

from django.db import models
from django.contrib.sites.models import Site
from sorl.thumbnail import ImageField


class Upload(models.Model):
    name = models.CharField(max_length=200)
    image = ImageField(upload_to="uploads")

    def __unicode__(self):
        return posixpath.basename(self.image.name)

    def to_json_data(self):
        domain = Site.objects.get_current().domain
        url = "http://%s%s" % (domain, self.image.url)
        data = {
            'deleteType': 'DELETE',
            'deleteUrl': self.image.url,
            'name': posixpath.basename(self.image.name),
            'originalName': posixpath.basename(self.name),
            'size': self.image.size,
            'thumbnailUrl': url,
            'type': None,
            'url': url,
        }
        return data
