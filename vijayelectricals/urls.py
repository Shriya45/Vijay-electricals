
from django.contrib import admin
from django.urls import path, include
from app.views import index
from app.views import index, chatbot_response 
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'services', 'gallery', 'contact']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path ('',index, name="index"),
    path('admin/', admin.site.urls),
     path("chatbot/", chatbot_response, name="chatbot"),
    path('', include('app.urls')),  # include our app's urls
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  # sitemap path
]


