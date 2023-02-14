from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

class menus(models.Model):
    item_menus=models.AutoField
    item_name=models.CharField(max_length=100)
    links=models.CharField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class burger(models.Model):
    item_burgerid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class hotbeverages(models.Model):
    item_hotbevid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class maggi(models.Model):
    item_maggiid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class shake(models.Model):
    item_shakeid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class snacks(models.Model):
    item_snacksid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class chinese(models.Model):
    item_chineseid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class pudding(models.Model):
    item_puddingid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class sandwich(models.Model):
    item_sandwichid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class garlicbread(models.Model):
    item_garlicid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class coolref(models.Model):
    item_coolrefid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class pastries(models.Model):
    item_pastriesid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class parantha(models.Model):
    item_paranthaid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name
class mocktail(models.Model):
    item_mocktailid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name   
class egg(models.Model):
    item_eggid=models.AutoField
    item_name=models.CharField(max_length=100)
    item_price=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.item_name                                                   
        
class facultycse(models.Model):
    sno=models.AutoField
    faculty_name=models.CharField(max_length=100)
    faculty_id=models.IntegerField(max_length=100)
    image= models.ImageField(upload_to="menu/images",default="")
    def __str__(self):
        return self.faculty_name
