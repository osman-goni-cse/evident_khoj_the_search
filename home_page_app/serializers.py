from rest_framework.serializers import ModelSerializer
from . models import *

class StoreNumberSerializer(ModelSerializer):
  class Meta:
    model = StoreNumber
    fields = '__all__'