from rest_framework import serializers

from explain_code.models import ExplainPythonCode


class ExplainPythonCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplainPythonCode
        fields = ('error', 'msg', 'data')
