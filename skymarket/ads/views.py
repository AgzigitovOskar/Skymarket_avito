from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdTitleFilter
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from ads.models import Ad, Comment
from ads.permissions import IsOwner
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdTitleFilter

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return AdDetailSerializer
        else:
            return AdSerializer

    def det_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
        return super().get_permissions()

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        return Comment.objects.filter(ad_id=ad_id)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

