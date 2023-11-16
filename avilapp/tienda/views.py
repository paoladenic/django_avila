from .models import Product
from .forms import CustomUserCreationForm, EditProfileForm, ReservaProfileForm

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.views.generic.edit import UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'tienda/index.html')


class CustomLoginView(LoginView):
    template_name = 'tienda/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tienda:product_list')

    
class RegisterPage(FormView):
    template_name = 'tienda/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tienda:product_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tienda:product_list')
        return super(RegisterPage, self).get(*args, **kwargs)
    
    
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'tienda/change_password.html'
    success_url = reverse_lazy('tienda:password_change_done')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User 
    template_name = 'tienda/edit_profile.html'
    form_class = EditProfileForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('tienda:product_list')

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    
class ProductList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'tienda/productos.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'products'
    template_name = 'tienda/lista.html'

def contacto(request):
    return render(request, 'tienda/contacto.html')


def reserva(request, product_id):
    if not request.user.is_authenticated:
        return redirect('tienda:login')

    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
    
        user_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        user_info = ReservaProfileForm(initial=user_data)
        for field_name, field in user_info.fields.items():
            if field_name in ['first_name', 'last_name', 'email']:
                field.widget.attrs['readonly'] = True

            send_reservation_email(product, user_data)
            return render(request, 'tienda/confirmar_reserva.html', {'product': product, 'user_info': user_info})

    context = {
        'product': product,
        'user_info': user_info,
    } 
    return render(request, 'tienda/reserva.html', context)


def send_reservation_email(product, user_data):
    email_message = f"Reserva de producto:\nNombre del producto: {product.name}\nCategoría: {product.category}\nCondición: {product.condition}\nPrecio: €{product.price}\n\nDatos del usuario:\nNombre: {user_data['first_name']} {user_data['last_name']}\nEmail: {user_data['email']}"

    result = send_mail(
        'Reserva de Producto',
        email_message,
        settings.EMAIL_HOST_USER,
        ['tu_email@gmail.com'],
        fail_silently=False,
    )
    if result == 1:
        print("El correo se envió correctamente.")
    else:
        print("Hubo un error al enviar el correo.")


def confirmar_reserva(request):
    return render(request, 'tienda/confirmar_reserva.html')
