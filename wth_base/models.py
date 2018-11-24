from django.db import models


class User(models.Model):
    user_telegram_id = models.IntegerField(unique=True)
    fake_count = models.IntegerField(default=0)

    def __str__(self):
        return f"<User: {self.user_telegram_id}, fake count: {self.fake_count}>"


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    stop_name = models.CharField(max_length=100)

    visible = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Location: {self.user_telegram_id}, stop name: {self.stop_name}, " \
               f"visible: {self.visible}, created on: {self.created_on}>"
