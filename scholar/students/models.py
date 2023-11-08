from django.db import models
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    status = models.BooleanField(null=false)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=false)
class Students(models.Model):
    code = models.CharField(max_length=50)
    id_person = models.IntegerField()
    status = models.BooleanField(null=true)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=false)
class IdentificationType(models.Model):
    name = models.CharField(max_length=50)
    abrew = models.CharField(max_length=10)
    descrip = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)
    
class Persons(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_iden_type = models.IntegerField()
    ident_number = models.CharField(max_length=15)
    Id_exp_city = models.IntegerField()
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=50)
    id_user = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

class City(models.Model):
    name = models.CharField(max_length=100)
    abrew = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    id_dept = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

class Department(models.Model):
    name = models.CharField(max_length=100)
    abrew = models.CharField(max_length=10)
    deschp = models.CharField(max_length=10)
    id_country = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)
