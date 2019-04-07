from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, default='sha')
    pwd = models.CharField(max_length=32)
    introduction = models.TextField(default='')
    winTimes = models.IntegerField(default=0)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    me = models.IntegerField()
    opponent = models.IntegerField()
    win = models.IntegerField(default=-1)  # 0/1  fail/win

    def __str__(self):
        return self.pk


class Friend(models.Model):
    me = models.IntegerField()
    friend = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.pk
