from django.contrib import admin
from .models import Product,Prod_rec,Crop,Crop_prd,Post,Post_Comment,Crop_activity,Schedule
# Register your models here.


admin.site.register(Product)
admin.site.register(Prod_rec)
admin.site.register(Crop)
admin.site.register(Crop_prd)
admin.site.register(Post)
admin.site.register(Post_Comment)
admin.site.register(Crop_activity)
admin.site.register(Schedule) 

