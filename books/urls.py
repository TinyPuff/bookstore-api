from rest_framework.routers import SimpleRouter
from .views import BookViewSet, CategoryViewSet, ReviewViewSet


router = SimpleRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("reviews", ReviewViewSet, basename="reviews")
router.register("", BookViewSet, basename="books")

urlpatterns = router.urls
