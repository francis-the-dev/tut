
from django.contrib import admin
from django.urls import path
from tutor import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tutor/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('bc_tutor/', views.bc_tutor, name='tutor_reg'),
    path('scholar_det/<int:id>/',views.scholar_det, name='scholar_det')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
