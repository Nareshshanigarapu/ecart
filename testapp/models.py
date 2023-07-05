from django.db import models
# Create your models here.

class getouch_model(models.Model):
    message=models.CharField(max_length=100)
    name=models.CharField(max_length=120)
    email=models.EmailField()



#class seller_model(models.Model):
 #   name=models.CharField(max_length=100)
  #  user_name=models.CharField(max_length=120)
   # email=models.EmailField()
    #phone=models.IntegerField()
 #   password=models.CharField(max_length=8)
 #   pic = models.FileField(null=True,upload_to='media/')
    #pic=models.ImageField(null=True,upload_to='media/',)

class product_detail(models.Model):
    p_type=models.CharField(max_length=100)
    p_size=models.IntegerField()
    p_dis=models.CharField(max_length=500)
    #p_img=models.FileField(null=True,upload_to='media/')



