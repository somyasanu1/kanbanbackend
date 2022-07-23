from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    username = models.TextField(db_column="username", blank=False, null=False)
    password_hash = models.TextField(db_column="password_hash", blank=False, null=False)

    class Meta:
        db_table = "users"
