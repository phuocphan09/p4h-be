from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from run_code.models import RunPythonCode
from run_code.serializers import RunPythonCodeSerializer
from run_code.controllers import runPythonCode3

class RunPythonView(APIView):
    def post(self, request):
        result = runPythonCode3(request.data['script'])
        if ('err_class' in result):
            res_data = {
                'error': 23,
                'msg': 'code error',
                'data': {
                    'error_class': result['err_class'],
                    'line_no': result['line_no'][0],
                    'char_no': result['char_no'][0] if len(result['char_no']) > 0 else 0,
                    'detail': result['detail']
                }
            }
        else:
            res_data = {
                'error': 0,
                'msg': 'success',
                'data': str(result)
            }
        return JsonResponse(res_data, status=status.HTTP_200_OK)
