from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

from explain_code.serializers import ExplainPythonCodeSerializer
from explain_code.controllers import ask_gpt
# Create your views here.

class ExplainCodeView(APIView):
    def post(self, request):
        msg = request.data['text']
        try:
            result = ask_gpt(msg)[0]
            res_data = {
                'error': 0,
                'msg': 'success',
                'data': result
            }
            serializer = ExplainPythonCodeSerializer(data=res_data)
            if serializer.is_valid():
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'data': str(e)}, status=status.HTTP_200_OK)
