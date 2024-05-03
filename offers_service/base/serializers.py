from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nombre = serializers.CharField()
    apellido = serializers.CharField()
    ciudad = serializers.CharField()
    email = serializers.EmailField()
    celular = serializers.CharField()
    actividadEconomica = serializers.CharField()
    empresa = serializers.CharField()
    ingresos = serializers.FloatField()
    pasivos = serializers.FloatField()

    class Meta:
        fields = '__all__'
