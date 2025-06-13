# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('create/', views.product_create, name='product_create'),
#     path('<int:pk>/edit/', views.product_update, name='product_update'),
#     path('<int:pk>/delete/', views.product_delete, name='product_delete'),

#     path('', views.index, name='index'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('cart/', views.cart, name='cart'),
#     path('products/', views.product_list, name='product_list'),
#     path('add/', views.product_create, name='add_product'),

# ]
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/edit/', views.product_update, name='product_update'),
    path('registration/', views.registration, name='registr'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('user/', include('user.urls')),

    # КОРЗИНА
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    
    # Логин
    path('login/', auth_views.LoginView.as_view(template_name='products/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='product_list'), name='logout'),

    # Сброс пароля
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
]







# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('users.urls')),  # или другое имя твоего приложения
#     path('accounts/', include('django.contrib.auth.urls')),  # логин/логаут
# ]
