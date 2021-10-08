from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # def __str___(self):
    #     return '{}'.format(self.name)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas', on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)

    # def __str___(self):
    #     return '{} {}'.format(self.first_name, self.last_name)
