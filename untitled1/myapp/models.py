from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime
import datetime

# Create your models here.



class Country(models.Model):
    countryName = models.CharField(max_length=100)

    def __str__(self):
        return self.countryName


class Province(models.Model):
    countryName = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinceName = models.CharField(max_length=100)

    def __str__(self):
        return self.provinceName


class City(models.Model):
    cityName = models.CharField(max_length=100)
    countryName = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinceName = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.cityName


class PropertyFacing(models.Model):
    PROPERTY_FACING = (
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
        ('Other', 'Other'),
    )
    PropertyFacing = models.CharField(choices=PROPERTY_FACING, max_length=20, default='North')

    def __str__(self):
        return self.PropertyFacing


PROPERTY_SECTOR = ("Private", "Residential", "Commercial", "Government", "Rural", "Other")


class PropertySector(models.Model):
    PROPERTY_SECTOR = (
        ('Private', 'Private'),
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Government', 'Government'),
        ('Rural', 'Rural'),
        ('Other', 'Other'),
    )
    PropertySector = models.CharField(choices=PROPERTY_SECTOR, max_length=20, default='Private')

    def __str__(self):
        return self.PropertySector


PROPERTY_CATEGORY = ("Single House", "Attached House", "Town House", "Apartment", "Store", "Farm", "Factory", "Mall", "Building", "Other")


class PropertyCategory(models.Model):
    PROPERTY_CATEGORY = (
        ('Single House', 'Single House'),
        ('Attached House', 'Attached House'),
        ('Town House', 'Town House'),
        ('Apartment', 'Apartment'),
        ('Store', 'Store'),
        ('Farm', 'Farm'),
        ('Factory', 'Factory'),
        ('Mall', 'Mall'),
        ('Building', 'Building'),
        ('Other', 'Other'),
    )
    PropertyCategory = models.CharField(choices=PROPERTY_CATEGORY, max_length=20, default='Single House')

    def __str__(self):
        return self.PropertyCategory


class Property(models.Model):
    propertyID = models.IntegerField()
    propertyTitle = models.CharField(max_length=100)
    propertyCategory = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)
    propertySector = models.ForeignKey(PropertySector, on_delete=models.CASCADE)
    PropertyFacing = models.ForeignKey(PropertyFacing, on_delete=models.CASCADE)
    PropertyCountry = models.ForeignKey(Country, on_delete=models.CASCADE)
    PropertyProvince = models.ForeignKey(Province, on_delete=models.CASCADE)
    PropertyCity = models.ForeignKey(City, on_delete=models.CASCADE)
    PropertyStreet = models.CharField(max_length=200)
    propertyPostalCode = models.CharField(max_length=200)
    propertyStreetNumber = models.CharField(max_length=200)
    propertyConstructionDate = models.DateField()
    propertyRegistrationDate = models.DateField()
    propertyNoOfHalls = models.IntegerField()
    propertyNoOfBedRooms = models.IntegerField()
    propertyNoOfBathRooms = models.FloatField()
    propertyNoOfFloors = models.IntegerField()
    propertyTotalArea = models.FloatField()
    propertyAskingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    propertySellingPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.propertyTitle


class PropertyImages(models.Model):
    propertyID = models.ForeignKey(Property, on_delete=models.CASCADE)
    propertyImage = models.ImageField(blank=True,null=True)
    propertyImageID = models.IntegerField()
    propertyImageDescription = models.CharField(max_length=500)

    def __str__(self):
        return self.propertyImageDescription


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=500)


class UserRole(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100,default='abc')
    rolename = models.CharField(max_length=100, default='admin')

    def __str__(self):
        return self.username


class RoleCode(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SysFeature(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SysFeatureRole(models.Model):
    id = models.IntegerField(primary_key=True)
    rolename = models.CharField(max_length=100, default='admin')
    featurename = models.CharField(max_length=100, default='add user')
    permissiontype = models.CharField(max_length=100, default='read')

    def __str__(self):
        return self.rolename


class PermissionType(models.Model):
    id = models.IntegerField(primary_key=True)
    NAME = (
        ('Read', 'Read'),
        ('Write', 'Write'),
        ('Delete', 'Delete'),
        ('Update', 'Update'),

    )

    name = models.CharField(choices=NAME, max_length=20, default='Read')

    def __str__(self):
        return self.name


#class RolePermission(models.Model):
    #    id = models.IntegerField(primary_key=True)
    #name = models.CharField(max_length=100,default='admin')
    #perName = models.ForeignKey(PermissionType,on_delete=models.CASCADE)

        #def __str__(self):
# return self.name

#class Password(models.Model):
    #id = models.IntegerField(primary_key=True)
    #username = models.CharField(max_length=200)
    # encryptedPassword = models.CharField(max_length=200)
    #salt = models.CharField(max_length=100)
    #UserAccountExpiryDate = models.DateField()
    # PasswordMustChanged = models.BooleanField()
#PasswordReset = models.BooleanField()

