from django.db import models

class BietOn(models.Model):
    Ngay = models.DateTimeField(auto_now_add=True)
    NoiDung = models.TextField()

    def __str__(self):
        return f"{self.Ngay.date()} - {self.NoiDung[:30]}"

class MuonLam(models.Model):
    Ngay = models.DateTimeField(auto_now_add=True)
    NoiDung = models.TextField()

    def __str__(self):
        return f"{self.Ngay.date()} - {self.NoiDung[:30]}"

class BaiHoc(models.Model):
    Ngay = models.DateTimeField(auto_now_add=True)
    NoiDung = models.TextField()

    def __str__(self):
        return f"{self.Ngay.date()} - {self.NoiDung[:30]}"
