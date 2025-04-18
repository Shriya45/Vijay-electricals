
from django.contrib import admin
from django.urls import path, include
from app.views import index
from app.views import index, chatbot_response 

urlpatterns = [
    path ('',index, name="index"),
    path('admin/', admin.site.urls),
     path("chatbot/", chatbot_response, name="chatbot"),
    path('', include('app.urls')),  # include our app's urls
    
]


