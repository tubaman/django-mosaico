from __future__ import unicode_literals
import posixpath

from django.db import models
from sorl.thumbnail import ImageField


class Upload(models.Model):
    name = models.CharField(max_length=200)
    image = ImageField(upload_to="uploads")

    def __unicode__(self):
        return posixpath.basename(self.image.name)

    def to_json_data(self):
        data = {
            'deleteType': 'DELETE',
            'deleteUrl': self.image.url,
            'name': posixpath.basename(self.image.name),
            'originalName': posixpath.basename(self.name),
            'size': self.image.size,
            'thumbnailUrl': self.image.url,
            'type': None,
            'url': self.image.url,
        }
        return data
