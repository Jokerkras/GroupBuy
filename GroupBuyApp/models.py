from django.db import models

class Lot(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=128)
    email = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    cash = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return 'Username: %s; email: %s' % (
            self.username, self.email)
