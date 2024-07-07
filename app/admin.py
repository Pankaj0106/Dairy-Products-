from django.contrib import admin
from app.models import Product,Customer,Cart,Payment,OrderPlaced,Wishlist
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.

admin.site.register(Product)
@admin.register(Customer)

class CustomerRegister(admin.ModelAdmin):
    list_display = ('user','name','locality','city','mobile','state','zipcode')


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products','quantity']
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link, obj.product.pk)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','rozarpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status','payment']    

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']