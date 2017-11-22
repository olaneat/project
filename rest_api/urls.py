from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token
from rest_api import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = 'rest_api'
urlpatterns = [
url(r'^bucketlists/$', CreateView.as_view(), name = "create"),
url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name = "details"),
url(r'^auth/', include('rest_framework.urls', namespace = 'rest_framework')),
url(r'^$', views.dashboard, name = 'dashboard'),
url(r'^signup/$', views.signup, name = 'signup'),
url(r'^login/$', auth_views.login, name = 'login'),
url(r'^logout/$', auth_views.logout,{'next_page': '/'}, name = 'logout'),
url(r'^admin/', admin.site.urls),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
    url(r'^docs/', include('rest_framework_docs.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
