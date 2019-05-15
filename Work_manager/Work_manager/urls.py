from django.conf.urls import include, url
from django.contrib import admin
# from Work_manager import TaskManager

urlpatterns = [
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'TaskManager.views.index.page'),
    url(r'^index$', 'TaskManager.views.index.page')
]
