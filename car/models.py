from __future__ import unicode_literals

from django.db import models

from ums.models import Driver


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class DriverGroup(models.Model):
    group = models.ForeignKey(Group)
    driver = models.ForeignKey(Driver)

    class Meta:
        unique_together = (('group', 'driver'),)

    def __unicode__(self):
        return self.group.__unicode__() + " " + self.driver.__unicode__()


class Car(models.Model):
    license_plate = models.CharField(max_length=50, unique=True)
    group = models.ForeignKey(Group)
    active_driver = models.ForeignKey(Driver, blank=True, null=True)

    def __unicode__(self):
        return self.license_plate


class CarAccess(models.Model):
    car = models.ForeignKey(Car)
    driver = models.ForeignKey(Driver)
    start_time = models.DateField()
    end_time = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = (('car', 'driver'),)

    def __unicode__(self):
        return self.driver.__unicode__() + " for " + self.car.__unicode__()


class CarUsage(models.Model):
    car = models.ForeignKey(Car)
    driver = models.ForeignKey(Driver)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.car.__unicode__() + " " + self.driver.__unicode__()
