from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from .forms import RegisterForm

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^register/', CreateView.as_view(
        template_name='register.html',
        form_class=RegisterForm,
        success_url='/LokahiApp/homepage'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^createGroup', views.create_group),
    url(r'^editGroup/(?P<pk>[0-9]+)/(?P<qk>[0-9]+)/$', views.edit_group),
    url(r'^joinGroup/(?P<pk>[0-9]+)/$', views.join_group),
    url(r'^leaveGroup/(?P<pk>[0-9]+)/$', views.leave_group),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^login/', auth_views.login, name='login'),
    # Logging out takes you back to the landing page
    url(r'^logout/$', auth_views.logout, {'template_name': 'index.html'}, name='logout'),
    url(r'^homepage/', views.homepage),
    url(r'^messenger/', views.message),
    url(r'^inbox/', views.inbox),
    url(r'^individual_message/(?P<pk>\d+)/$', views.individual_message, name="individual_message"),
    url(r'^delete_message/(?P<pk>\d+)/$', views.delete_message, name="delete_message"),
    url(r'^sent_messages/(?P<pk>\d+)/$', views.sent_messages, name="sent_messages"),
    url(r'^report/new/$', views.create_report, name="create_report"),
    url(r'^report/', views.report),
    url(r'^result/(?P<pk>\d+)/$', views.result, name="result"),
    url(r'^result/(?P<pk>\d+)/edit/$', views.report_edit, name='report_edit'),
    url(r'^sitemanagerindex/', views.sitemanagerindex),
    url(r'^media/(?P<path>.*)$', views.download),
    url(r'^$', views.index),
]

