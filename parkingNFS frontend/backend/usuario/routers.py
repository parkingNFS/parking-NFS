from rest_framework.routers import DefaultRouter
from ..rol.views import *
from ..facturacion.views import *

router = DefaultRouter()

router.register(r'rol', RolViewset, basename='rol')
router.register(r'facturacion', FacturacionViewset, basename='facturacion')

urlpatterns = router.urls