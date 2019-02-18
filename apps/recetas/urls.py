from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.recetas.views import Index, addReceta, RecetasList, RecetaDetail, CommentList, RecetaUpdate, RecetaDelete, filtro

app_name = 'receta'
urlpatterns = [
    url(r'^$', Index.as_view(), name='index_receta'),
    url(r'^nueva_receta$', login_required(addReceta), name='new_receta'),
    url(r'^listar_recetas$', RecetasList.as_view(), name='list_recetas'),
    url(r'^detalle/(?P<pk>\d+)$', login_required(RecetaDetail.as_view()), name='detail_receta'),
    # url(r'^detalle/(?P<pk>\d+)$', CommentList.as_view(), name='list_comment'),
    url(r'^editar/(?P<pk>\d+)$', RecetaUpdate.as_view(), name='edit_receta'),
    url(r'^eliminar/(?P<pk>\d+)$', RecetaDelete.as_view(), name='delete_receta'),
    path('listar_recetas/filtro', filtro, name='filtro'),

]