from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import static_template_view, about_view, contact_view


app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    path('static-template/', static_template_view, name='static_template'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    # view refers to the view function
    # name the URL

    # path for about view
    

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index')

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)