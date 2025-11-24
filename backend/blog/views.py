from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer
from users.models import UserRegion
from utils.permissions import OwnerOrReadOnly


class BlogPostViewSet(viewsets.ModelViewSet):
    '''ViewSet для модели BlogPost'''
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # permission_classes = (OwnerOrReadOnly,)

    @action(detail=False, url_path='main-page')
    def main_page(self, request):
        '''Отображение для главной страницы.'''
        user_regions = get_list_or_404(UserRegion, user=request.user)
        region_ids = []
        for user_region in user_regions:
            region_ids.append(user_region.region.id)
        print(region_ids)
        print(BlogPost.objects.filter(type='reg news'))
        reg_news = BlogPost.objects.filter(type='reg news').filter(region__in=region_ids)[:2]
        fed_news = BlogPost.objects.filter(type='fed news')[:2]
        main_news = reg_news | fed_news
        print(main_news)
        serializer = self.get_serializer(main_news)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    
