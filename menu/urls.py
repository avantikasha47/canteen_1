from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns=[
    path('menus',views.menu,name='menus'),
    path('hotbeverages.html',views.hotbev,name='hotbev'),
    path('coolrefreshers.html',views.coolrefs,name='coolref'),
    path('shakes.html',views.shakes,name='shakes'),
    path('mocktails.html',views.mocktails,name='mocktails'),
    path('burgers.html',views.burgers,name='burgers'),
    path('garlicbread.html',views.garlicbreads,name='garlicbread'),
    path('sandwich.html',views.sandwichs,name='sandwich'),
    path('snacks.html',views.snack,name='snacks'),
    path('pudding.html',views.puddings,name='pudding'),
    path('chinese.html',views.chineses,name='chinese'),
    path('pastries.html',views.pasteriess,name='pastries'),
    path('maggi.html',views.maggis,name='maggi'),
    path('egg.html',views.eggs,name='egg'),
    path('parantha.html',views.paranthas,name='paranthas'),
    path('registers/',views.register,name='registers'),
    path('profile/',views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='login1.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='menu1.html'),name='logout'),
    path('cart/',views.cart,name='cart'),
    
    
]


