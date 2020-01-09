from django.db import models

# Create your models here.
class Gdp(models.Model):
    city = models.CharField(max_length=20, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    gdp = models.FloatField(blank=True, null=True)
    percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gdp'

class EnergyElectric(models.Model):
    city = models.CharField(max_length=10, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_electric'

class EnergyCoal(models.Model):
    city = models.CharField(max_length=30, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    num = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_coal'

class FixedInvest(models.Model):
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.CharField(max_length=10, blank=True, null=True)
    num = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_invest'

class HouseInvest(models.Model):
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    city = models.CharField(max_length=10, blank=True, null=True)
    num = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_invest'


class NbFixedInvest(models.Model):
    area = models.CharField(max_length=10, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nb_fixed_invest'


class NbHouseInvest(models.Model):
    area = models.CharField(max_length=10, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nb_house_invest'

class NbGdp(models.Model):
    area = models.CharField(max_length=10, blank=True, null=True)
    year = models.TextField(blank=True, null=True)  # This field type is a guess.
    num = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nb_gdp'

