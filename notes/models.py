from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    hex_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title