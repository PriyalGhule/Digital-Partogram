from django.db import models

class Details(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.BigIntegerField(max_length=50,null=True)
    role=models.CharField(max_length=50)




class Section1(models.Model):    
    fhr=models.IntegerField(null=True)
    hrs=models.IntegerField(null=True)

class Section2(models.Model):
    amnioticfluid=models.CharField(max_length=50, null=True)
    moulding=models.CharField(max_length=50, null=True)
    protein=models.CharField(max_length=50, null=True)
    acetone=models.CharField(max_length=50, null=True)
    volume=models.CharField(max_length=50, null=True)


class Section3(models.Model):
    contractionsno=models.CharField(max_length=50,null=True)
    contractionsdur=models.CharField(max_length=50,null=True)
    chours=models.IntegerField(null=True)
    oxytocin=models.CharField(max_length=50, null=True)

class Parto_dets(models.Model):
    c_dilation=models.IntegerField(null=True)
    hours=models.IntegerField(null=True)
    time=models.TimeField(null=True)