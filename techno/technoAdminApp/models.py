from django.db import models
import uuid

class PostTable(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)


    def __str__(self):
        return self.name
