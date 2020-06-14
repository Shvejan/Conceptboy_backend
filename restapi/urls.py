from django.urls import include, path
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippets', views.SnippetViewset)
router.register(r'video', views.VideoViewset)
router.register(r'subject', views.SubjectViewset)
router.register(r'subcategory', views.SubcategoryViewset)
router.register(r'category', views.CategoryViewset)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
