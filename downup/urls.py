from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from paypal.standard.ipn import views as paypal_views

from user import views as profile_views
from tracker import views as pages_views
handler404 = pages_views.notfound

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pages_views.index, name='index'),
    path('about/', pages_views.about, name='about'),
    path('terms/', pages_views.terms, name='terms'),
    path('partners/', pages_views.partners_page, name='partners'),
    path('sponsors/', pages_views.partners_page, name='partners'),
    path('privacy/', pages_views.privacy, name='privacy'),
    path('404/', pages_views.notfound),

    path('register/', profile_views.CreateUserFormView.as_view(), name='register'),
    path('login/', profile_views.login, {'template_name': 'profiles/login_form.html'}, name='login'),
    path('logout/', profile_views.logout, name='logout'),

]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
