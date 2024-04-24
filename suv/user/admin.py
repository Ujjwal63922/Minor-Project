from django.contrib import admin
from user.models import userform
from user.models import contact
from user.models import buy_form

class userforms(admin.ModelAdmin):
    data = ('name','email','contact','category','location','price','description')
admin.site.register(userform,userforms)

class contacts(admin.ModelAdmin):
    data = ('name','email','description')
admin.site.register(contact,contacts)
class buy_forms(admin.ModelAdmin):
    data = ('p_id','name','email','contact')
admin.site.register(buy_form,buy_forms)