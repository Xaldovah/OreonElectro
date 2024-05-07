from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Sum, F
from django.db.models.functions import TruncDay
from .models import UserActivity
from .serializers import UserActivitySerializer
from django.utils import timezone


class UserActivityListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        activity_type = request.query_params.get('activity_type')
        activities = UserActivity.objects.filter(user=user)

        if activity_type:
            activities = activities.filter(activity_type=activity_type)

        if 'aggregate' in request.query_params:
            aggregation = activities.values('activity_type').annotate(total=Count('id')).order_by('-total')
            return Response(aggregation, status=status.HTTP_200_OK)

        serializer = UserActivitySerializer(activities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogUserActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        activity_type = request.data.get('activity_type')
        activity_data = request.data.get('activity_data')

        if activity_type not in UserActivity.ActivityTypes.__members:
            return Response({'error': 'Invalid activity'}, status=status.HTTP_400_BAD_REQUEST)

        activity = UserActivity.objects.create(
                user=user,
                activity_type=activity_type,
                activity_data=activity_data
        )
        serializer = UserActivitySerializer(activity)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SalesOverviewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sales_activities = UserActivity.objects.filter(
                activity_type=UserActivity.ActivityTypes.PURCHASE
        )

        aggregation = sales_activities.aggregate(
                total_sales=Count('id'),
                total_revenue=Sum(F('activity_data__amount'))
        )

        daily_sales = sales_activities.annotate(date=TruncDay('timestamp')).values('date').annotate(
                daily_sales=Count('id'),
                daily_revenue=Sum(F('activity_data__amount'))
        ).order_by('-date')

        return Response({
            'total_sales': aggregation['total_sales'],
            'total_revenue': aggregation['total_revenue'],
            'daily_sales': daily_sales
        }, status=status.HTTP_200_OK)


class CustomerBehaviorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            activities = UserActivity.objects.filter(user_id=user_id)
        else:
            activities = UserActivity.objects.all()


        activity_count = activities.values('activity_type').annotate(total=Count('id')).order_by('-total')

        last_login = activities.filter(activity_type=UserActivity.ActivityTypes.LOGIN).order_by('-timestamp').first()

        return Response({
            'activity_count': activity_count,
            'last_login': UserActivitySerializer(last_login).data if last_login else None,
        }, status=status.HTTP_200_OK)


class GeneralMetricsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_date = timezone.now().date()
        start_date = request.query_params.get('start_date', current_date)
        end_date = request.query_params.get('end_date', current_date)

        activities = UserActivity.objects.filter(
                timestamp__date_gte=start_date,
                timestamp__date_lte=end_date
        )

        activity_summary = activities.values('activity_type').annotate(total=Count('id')).order_by('-total')

        unique_users = activities.values('user').distinct().count()

        return Response({
            'activity_summary': activity_summary,
            'unique_users': unique_users
        }, status=status.HTTP_200_OK)
