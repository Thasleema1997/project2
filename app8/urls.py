from django.urls import path
from . import views
urlpatterns=[path("",views.home,name="home"),
             path("p1",views.admin,name="admin"),
             path("p2",views.employee,name="employee"),
             path("p3",views.manager,name="manager"),
             path("p4",views.adminlogin,name="adminlogin"),
             path("p5",views. managerlogin,name=" managerlogin"),
             path("p6",views.employeelogin,name="employeelogin"),
             path("p7",views.commonlogin,name="commonlogin"),
             path("p8",views.weladm,name="weladm"),
             path("p9",views.welemp,name="welemp"),
             path("p10",views.welman,name="welman")]