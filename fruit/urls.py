from django.urls import path
from .views import raqam,cart,chackout,contact,home,shop,shop_detail,testimonial


urlpatterns=[
    path('',home,name='home_page'),
    path('raqam/',raqam,name='raqam_page'),
    path('cart/',cart,name='cart_page'),
    path('chackout/',chackout,name='chackout_page'),
    path('contact/',contact,name='contact_page'),
    path('shop/',shop,name='shop_page'),
    path('shop_detail/',shop_detail,name='shop_detail_page'),
    path('testimonial/',testimonial,name='testimonial_page')
]