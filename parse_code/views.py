from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.views import APIView

from parse_code.controllers import parse_code_and_return_api


class ParseCodeView(APIView):
    def post(self, request):
        result = parse_code_and_return_api(request.data)
        response = {
            "error": 0,
            "msg": "success",
            "data": result['data']
        }
        return JsonResponse(response, status=status.HTTP_200_OK)