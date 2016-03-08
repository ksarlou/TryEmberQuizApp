# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Application(models.Model):
    idapplication = models.IntegerField(db_column='idApplication')  # Field name made lowercase.
    taskstartdate = models.DateTimeField(db_column='taskStartDate')  # Field name made lowercase.
    taskenddate = models.DateTimeField(db_column='taskEndDate')  # Field name made lowercase.
    departurepoint = models.CharField(db_column='departurePoint', max_length=45)  # Field name made lowercase.
    arrivalpoint = models.CharField(db_column='arrivalPoint', max_length=45)  # Field name made lowercase.
    meanoftransport = models.CharField(db_column='meanOfTransport', max_length=45)  # Field name made lowercase.
    categoryoftransport = models.CharField(db_column='categoryOfTransport', max_length=45)  # Field name made lowercase.
    project = models.CharField(max_length=45)
    subproject = models.CharField(max_length=45)
    departuredate = models.DateTimeField(db_column='departureDate')  # Field name made lowercase.
    arrivaldate = models.DateTimeField(db_column='arrivalDate')  # Field name made lowercase.
    ticketprice = models.FloatField(db_column='ticketPrice')  # Field name made lowercase.
    hotelprice = models.FloatField(db_column='hotelPrice')  # Field name made lowercase.
    publictransportprice = models.FloatField(db_column='publicTransportPrice', blank=True, null=True)  # Field name made lowercase.
    numberoftickets = models.IntegerField(db_column='numberOfTickets', blank=True, null=True)  # Field name made lowercase.
    user_iduser = models.ForeignKey('User', db_column='User_idUser')  # Field name made lowercase.
    applicationstatus = models.CharField(db_column='applicationStatus', max_length=15)  # Field name made lowercase.
    country_idcountry = models.ForeignKey('Country', db_column='Country_idCountry')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Application'


class Country(models.Model):
    idcountry = models.IntegerField(db_column='idCountry', primary_key=True)  # Field name made lowercase.
    countrynumber = models.IntegerField(db_column='countryNumber')  # Field name made lowercase.
    countrycomp = models.FloatField(db_column='countryComp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class User(models.Model):
    iduser = models.IntegerField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=45)  # Field name made lowercase.
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    specialty = models.CharField(max_length=45, blank=True)
    property = models.CharField(max_length=45, blank=True)
    iban = models.CharField(max_length=45)
    taxregnum = models.IntegerField(db_column='taxRegNum')  # Field name made lowercase.
    taxoffice = models.CharField(db_column='taxOffice', max_length=45)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=13)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
