from django.contrib import admin
from testapp.models import *
# Register your models here.


#class adminmodel(admin.ModelAdmin):
 #   list_display=['name','user_name','email','phone',]
    
#admin.site.register(Login_model,adminmodel)



class getouchadmin(admin.ModelAdmin):
    list_display=['message','name','email',]
    
admin.site.register(getouch_model,getouchadmin)

#class selleradmin(admin.ModelAdmin):
    #list_display=['name','user_name','email','phone','password','pic']
#admin.site.register(seller_model,selleradmin)