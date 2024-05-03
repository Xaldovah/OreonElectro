from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserActivity
from .serializers import UserActivitySerializer


class UserActivityListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        activities = UserActivity.objects.filter(user=user)
        serializer = UserActivitySerializer(activities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogUserActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        activity_type = request.data.get('activity_type')
        activity_data = request.data.get('activity_data')
        activity = UserActivity.objects.create(
                user=user,
                activity_type=activity_type,
                activity_data=activity_data
        )
        serializer = UserActivitySerializer(activity)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
