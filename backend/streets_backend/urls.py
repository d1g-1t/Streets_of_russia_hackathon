from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from aboutus.views import (AboutUsViewSet, FederalTeamViewSet,
                           GalleryViewSet, MediaViewSet, PartnerTypeViewSet,
                           PartnerViewSet, RegionalTeamViewSet, RegionViewSet)
from blog.views import BlogPostViewSet
from contacts.views import ContactViewSet
from events.views import EventViewSet, CoordinatesViewSet, EventLocationViewSet
from myauth.views import MyAuth, MyUnAuth
from streetculture.views import StreetCultureViewSet
from users.views import ManagementViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('v1/blog', BlogPostViewSet, basename='blog')
router.register('v1/contacts', ContactViewSet, basename='contacts')
router.register('v1/aboutus', AboutUsViewSet, basename='aboutus')
router.register('v1/federalteam', FederalTeamViewSet, basename='federalteam')
router.register('v1/regionalteam', RegionalTeamViewSet, basename='regionalteam')
router.register('v1/partnertype', PartnerTypeViewSet, basename='partnertype')
router.register('v1/partner', PartnerViewSet, basename='partner')
router.register('v1/gallery', GalleryViewSet, basename='gallery')
router.register('v1/media', MediaViewSet, basename='media')
router.register('v1/streetculture', StreetCultureViewSet, basename='streetculture')
router.register('v1/region', RegionViewSet, basename='region')
router.register('v1/event', EventViewSet, basename='event')
router.register('v1/eventlocation', EventLocationViewSet, basename='eventlocation')
router.register('v1/coordinates', CoordinatesViewSet, basename='coordinates')
router.register('v1/management', ManagementViewSet, basename='management')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('v1/login', MyAuth.as_view(), name='login'),
    path('v1/logout', MyUnAuth.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
