from rest_framework.views import APIView
from action_log.models import EventLog
from django.http import HttpResponse
import time


# Create your views here.

class ActionLogView(APIView):
    def post(self, request):

        def get_client_ip(request_in):
            x_forwarded_for = request_in.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request_in.META.get('REMOTE_ADDR')
            return ip

        all_data = request.data['data']
        e = EventLog(action=all_data['action'], metadata=all_data['metadata'], timestamp=all_data['timestamp'],
                     client_agent=all_data['client_agent'], client_ip=get_client_ip(request),
                     timestamp_server=int(time.time() * 1000))
        e.save()

        return HttpResponse('log success', status=200)
