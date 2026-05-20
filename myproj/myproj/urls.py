from django.conf.urls import url
from django.contrib import admin
from myproj import views  # Импорт ваших представлений

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    
    # Главная страница
    url(r'^$', views.index, name='index'),
    
    # Страница с рендерингом шаблона
    url(r'^hello/$', views.indexRender, name='hello'),
    
    # Страницы для работы с данными университета (задания 8-12)
    url(r'^universityInfo/$', views.universityInfo, name='universityInfo'),
    url(r'^disciplineInfo/$', views.disciplineInfo, name='disciplineInfo'),
    url(r'^groupsInfo/$', views.groupsInfo, name='groupsInfo'),
    url(r'^departmentsInfo/$', views.departmentsInfo, name='departmentsInfo'),
    url(r'^universityStructure/$', views.universityStructure, name='universityStructure'),
]