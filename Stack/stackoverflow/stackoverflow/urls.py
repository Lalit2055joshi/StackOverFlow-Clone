"""stackoverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  
from stack import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('question/',views.question,name='question'),
    path('reply/',views.reply,name='reply'),
    path('',views.dashboard,name='dashbord'),
    path('ans/<int:pk>',views.answer,name='ans'),
    path('reply/<int:pk>',views.reply,name='reply'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('delete/<int:pk>',views.delete_question,name='delete'),
    path('update/<int:pk>',views.update_question,name='updatequestion'),
    path('replyto/<int:pk>',views.reply_to,name='replyto'),
    path('logout/',views.logout_user,name='logout')

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
