from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView 

app_name = "tienda"

urlpatterns = [
    path('', home, name='homepage'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='tienda:homepage'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('contacto/', contacto, name='contacto'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='tienda/change_password_done.html'), name='password_change_done'),
    path('edit_profile/', UserProfileUpdateView.as_view(), name='edit_profile'),

    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),

    path('reserva/<int:product_id>/', reserva, name='reserva'),
    path('confirmar_reserva/', confirmar_reserva, name='confirmar_reserva'),

]
