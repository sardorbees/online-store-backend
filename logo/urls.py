from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
