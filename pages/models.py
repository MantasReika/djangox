from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Hub(models.Model):
    UPCOMING = 'UPCOMING'
    ONGOING = 'ONGOING'
    FINISHED = 'FINISHED'
    HUB_STA_CHOICES = (
        (UPCOMING, 'Upcoming'),
        (ONGOING, 'Ongoing'),
        (FINISHED, 'Finished')
    )

    class Meta:
        indexes = [models.Index(fields=['faceit_hub_id'])]
        ordering = ['id']

    def __str__(self):
        return "{0} - {1}".format(self.game_id, self.name)

    faceit_hub_id = models.CharField(max_length=128,
                                blank = True,
                                null=True)
    game_id = models.CharField(max_length=128,
                                blank = True,
                                null=True)
    name = models.CharField(max_length=128,
                            blank = True,
                            null=True)
    status = models.CharField(max_length=128,
                              choices=HUB_STA_CHOICES,
                              default=UPCOMING)
    start_dttm = models.DateTimeField(blank = True,
                                      null=True)
    finish_dttm = models.DateTimeField(blank = True,
                                       null=True)
    created_dttm = models.DateTimeField(auto_now_add=True)
    modified_dttm = models.DateTimeField(auto_now=True)

class HubScore(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    place = models.IntegerField(blank = True,
                                null=True)
    points = models.IntegerField(blank = True,
                                 null=True)
    created_dttm = models.DateTimeField(auto_now_add=True)
    modified_dttm = models.DateTimeField(auto_now=True)

class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    faceit_id = models.CharField(max_length=256,
                                 blank = True,
                                 null=True)
    eth_wallet_address = models.CharField(max_length=512,
                                          blank = True,
                                          null=True)
    created_dttm = models.DateTimeField(auto_now_add=True)
    modified_dttm = models.DateTimeField(auto_now=True)


class Invites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             blank = True,
                             null=True)
    invite_code = models.CharField(max_length=256,
                                   blank = True,
                                   null=True)
    transaction_hash = models.CharField(max_length=512,
                                        blank = True,
                                        null=True)
    created_dttm = models.DateTimeField(auto_now_add=True)
    modified_dttm = models.DateTimeField(auto_now=True)
