import secrets
import uuid
import requests
from django.conf import settings
from django.db import models
from rest_framework import status
from rest_framework.generics import GenericAPIView
from . import exceptions




class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




def get_or_create(model, **kwargs):
    object = model.objects.filter(**kwargs).first()
    if object:
        return object
    return model.objects.create(**kwargs)


def raise_errors():
    """
    Decorator to raise errors
    """

    def raise_errors(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions.Exception as error:
                raise error

        return wrapper

    return raise_errors

class FileStorageAPI:

    base_url = settings.FILE_STORAGE_URL

    @raise_errors()
    def _upload_file(self, file):
        return requests.post(
            "%s/files/" % self.base_url,
            files={"file": file},
        ).json()["file"]

    @raise_errors()
    def upload_file(self, *files):
        return list(map(self._upload_file, files))


def generate_reference():
    return secrets.token_hex(8).upper()
