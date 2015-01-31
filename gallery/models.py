from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    pic = models.ImageField("Select an Image", upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, editable=False)

