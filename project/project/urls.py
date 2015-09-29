from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
  # Examples:
  # url(r'^$', 'project.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
	url(r'^schools/', include('school.urls')),
	url(r'^jobs/', include('staff.urls')),
	url(r'^events/', include('events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
