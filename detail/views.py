from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from .models import *
from detail.serializers import *
from django.db.models import OuterRef, Subquery, F, Max,ExpressionWrapper,IntegerField
from django.db.models.functions import Cast
from django.db.models import CharField
# Create your views here.
class EventDetailView(views.APIView):
    def get(self, request, pk, format=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = DetailSerializer(instance=event, context={'request': request})
        return Response({"message":"이벤트 상세 조회 성공", "data": serializer.data})

# Create your views here.


class MenuLikeView(views.APIView):
    def get(self, request, menu_id):
        try:
            event = Event.objects.get(pk=menu_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        is_liked = event.like.filter(id=request.user.id).exists()

        response_data = {
            "message": "메뉴 좋아요 상태 조회 성공",
            "data": {
                "menu": menu_id,
                "is_liked": is_liked,
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)


    def patch(self, request, menu_id):
        try:
            menu = Menu.objects.get(pk=menu_id)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 모든 유저가 false 상태에서 patch를 통해 true로 바꾸는 구현
        if not menu.like.filter(id=request.user.id).exists():
            menu.like.add(request.user)
            is_liked = True
        else:
            menu.like.remove(request.user)
            is_liked = False

        response_data = {
            "message": "메뉴 좋아요 상태 변경 성공",
            "data": {
                "menu": menu_id,
                "is_liked": is_liked,
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

    
class EventLikeView(views.APIView):
    def get(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 사용자의 좋아요 상태 확인
        is_liked = event.like.filter(id=request.user.id).exists()

        response_data = {
            "message": "이벤트 좋아요 상태 조회 성공",
            "data": {
                "event": event_id,
                "is_liked": is_liked,
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)


    def patch(self, request, event_id):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 모든 유저가 false 상태에서 patch를 통해 true로 바꾸는 구현
        if not event.like.filter(id=request.user.id).exists():
            event.like.add(request.user)
            is_liked = True
        else:
            event.like.remove(request.user)
            is_liked = False

        response_data = {
            "message": "이벤트 좋아요 상태 변경 성공",
            "data": {
                "event": event_id,
                "is_liked": is_liked,
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)
