from rest_framework import serializers
from .models import Sizer, SizerItem

class SizerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sizer
		fields ='__all__'


class SizerItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = SizerItem
		fields ='__all__'