from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from system.views import admin_car_list, admin_msg, order_list, car_created, order_update, order_delete, msg_delete
from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin_car_list, name='adminIndex'),
    path('listOrder/', order_list, name = "order_list"),
    path('<int:id>/editOrder/', order_update, name = "order_edit"),
    path('<int:id>/deleteOrder/', order_delete, name = "order_delete"),
    path('create/', car_created, name = "car_create"),
    path('message/', admin_msg, name='message'),
    path('<int:id>/deletemsg/', msg_delete, name = "msg_delete"),
    path('car/', include('system.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

