from django.db import models


class SafariAccount(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    is_expired = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.email, self.is_expired)
