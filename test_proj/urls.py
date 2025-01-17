"""testproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^api-auth/",
        include("rest_framework.urls", namespace="rest_framework")),
    re_path(r"^mfa/", include("deux.urls")),
    re_path(r"^mfa/authtoken/",
        include(("deux.authtoken.urls", "authtoken"), namespace="authtoken"),
    ),
    re_path(r"^mfa/oauth2/",
        include(("deux.oauth2.urls", "oauth2"), namespace="oauth2"),
    ),
]
