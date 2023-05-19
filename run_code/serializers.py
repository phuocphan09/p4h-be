from rest_framework import serializers

from run_code.models import RunPythonCode


class RunPythonCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunPythonCode
        fields = ('error', 'msg', 'data')
