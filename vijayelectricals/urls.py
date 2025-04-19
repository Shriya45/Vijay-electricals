
from django.contrib import admin
from django.urls import path, include
from app.views import index
from app.views import index, chatbot_response 
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app.sitemap import StaticViewSitemap  # make sure this is correct
from django.http import HttpResponse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'services', 'gallery', 'contact']

    def location(self, item):
        return reverse(item)
def custom_sitemap(request):
    response = sitemap(request, sitemaps=sitemaps)
    response['X-Robots-Tag'] = 'index, follow'
    return response

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path ('',index, name="index"),
    path('admin/', admin.site.urls),
     path("chatbot/", chatbot_response, name="chatbot"),
    path('', include('app.urls')),  # include our app's urls
    path('sitemap.xml', custom_sitemap, name='sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # sitemap path
]


