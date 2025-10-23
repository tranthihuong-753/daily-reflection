from django.db import models

class BietOn(models.Model):
    Ngay = models.DateField(auto_now_add=True)
    NoiDung = models.TextField()

class MuonLam(models.Model):
    Ngay = models.DateField(auto_now_add=True)
    NoiDung = models.TextField()

class BaiHoc(models.Model):
    Ngay = models.DateField(auto_now_add=True)
    NoiDung = models.TextField()
