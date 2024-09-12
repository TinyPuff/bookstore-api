from rest_framework.routers import SimpleRouter
from .views import BookViewSet, CategoryViewSet


router = SimpleRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("", BookViewSet, basename="books")

urlpatterns = router.urls
