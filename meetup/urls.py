from django.conf.urls import include, url
from django.contrib import admin

from ui import views as ui_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^djangular_beer/', ui_views.DjangularFormView.as_view(), name="djangular_beer"),
    url(r'^djangular_validation_beer/', ui_views.DjangularValidationFormView.as_view(), name="djangular_validation_beer"),
    url(r'^djangular_model_beer/', ui_views.DjangularModelFormView.as_view(), name="djangular_model_beer"),
    url(r'^$', ui_views.ClassicDjangoFormView.as_view(), name="classic_django"),

    url(r'^internet_explorer/', ui_views.internet_explorer, name="internet_explorer"),

]
