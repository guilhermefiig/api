from rest_framework import routers
from .views import TodoListViewset, PessoaViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoListViewset)
router.register(r'pessoa', PessoaViewSet)
urlpatterns = router.urls