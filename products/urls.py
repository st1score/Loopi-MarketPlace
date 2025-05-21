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

from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    # path('', views.index, name='index'),# корневая страница
    path('', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/edit/', views.product_update, name='product_update'),
    path('registration/', views.registration, name='registr'),

    
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('user/', include('user.urls')),
    path('cart/', views.cart, name='cart'),
]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('users.urls')),  # или другое имя твоего приложения
#     path('accounts/', include('django.contrib.auth.urls')),  # логин/логаут
# ]
