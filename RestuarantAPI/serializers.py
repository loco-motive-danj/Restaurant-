from rest_framework import serializers
from .models import MenuItem 
from .models import Rating
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory':{'min_value':0}
        }

class RatingSerializer (serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            default=serializers.CurrentUserDefault()
    )

class Meta:
    model = Rating
    fields = ['user', 'menuitem_id', 'rating']

validators = [
    UniqueTogetherValidator(
        queryset=Rating.objects.all(),
        fields=['user', 'menuitem_id']
    )
]

extra_kwargs = {
    'rating': {'min_value': 0, 'max_value':5},
}