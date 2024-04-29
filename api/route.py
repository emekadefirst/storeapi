from django.urls import path
from .user.views import LoginUser, RegisterUser, LoginUser
from .product.views import ProductListView, ProductDetailView
from .cart.views import CartView
from .order.views import OrderView
from .payment.views import PayView
from rest_framework_swagger import renderers

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    # user auth
	path('register', RegisterUser.as_view(), name='register'),
	path('login', LoginUser.as_view(), name='login'),
	# path('logout', UserLogout.as_view(), name='logout'),
	# path('user', UserView.as_view(), name='user'),
        # product
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart', CartView.as_view(), name='cart'), #cart
    path('order', OrderView.as_view(), name='order'), # order
    path('pay', PayView.as_view(), name='payment'), # payment
    path(r'doc', schema_view),
]




