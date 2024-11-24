from django.urls import path
from .views import login_view, signup_view , product_list

urlpatterns = [
    path('login/',login_view , name='login'),
    path('signup/', signup_view, name='signup'),
    path('', product_list, name='product_list'),
    # path('logout/', logout_view, name='logout'),
]
