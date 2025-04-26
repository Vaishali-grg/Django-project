#Serializers convert your complex models into simple dictionary

#Models => Serializers(Dictionary) => Response(JSON)

from rest_framework import serializers
class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    price=serializers.IntegerField()
    quantity=serializers.IntegerField()
    