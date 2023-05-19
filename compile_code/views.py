from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from compile_code.controllers import handle_compile_info


class CompileCodeView(APIView):
    def post(self, request):
        code = request.data['script']
        compile_result = handle_compile_info(code)

        response = {
            "error": 0,
            "msg": "success",
            "data": compile_result
        }

        return JsonResponse(response, status=status.HTTP_200_OK)
