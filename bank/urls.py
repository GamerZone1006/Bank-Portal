from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage,name='Homepage'),
    path("accounts/",views.accounts,name="Accounts"),
    path("loginpg/",views.loginpg,name="login page"),
    path("support/",views.support,name="support page"),
    path("transaction/",views.transaction,name="transaction  page"),
]
