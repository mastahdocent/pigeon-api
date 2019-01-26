import os

from django.contrib.auth.models import AbstractUser
from django.db import models

# todo: overwrite avatars instead of adding suffixes to another filename

def avatars_path(instance, filename):
    file_extension = os.path.splitext(filename)[-1]
    new_filename = "{id}{ext}".format(id=instance.id, ext=file_extension)
    return "images/avatars/{filename}".format(filename=new_filename)


class User(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True)
    avatar = models.ImageField(blank=True, null=True, upload_to=avatars_path)

    def __str__(self):
        return self.username
