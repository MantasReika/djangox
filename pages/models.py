from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Hub(models.Model):
    UPCOMING = 'UPCOMING'
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'
    HUB_STA_CHOICES = (
        (UPCOMING, 'Upcoming'),
        (STARTED, 'Started'),
        (FINISHED, 'Finished')
    )

    status = models.CharField(max_length=128,
                              choices=HUB_STA_CHOICES,
                              default=UPCOMING)
    hub_name = models.CharField(max_length=128,
                                blank = True,
                                null=True)
    hub_start_dttm = models.DateTimeField(blank = True,
                                          null=True)
    hub_finish_dttm = models.DateTimeField(blank = True,
                                           null=True)

class HubScore(models.Model):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    place = models.IntegerField(blank = True,
                                null=True)
    points = models.IntegerField(blank = True,
                                 null=True)

class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    faceit_id = models.CharField(max_length=256,
                                 blank = True,
                                 null=True)
    eth_wallet_address = models.CharField(max_length=512,
                                          blank = True,
                                          null=True)


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
