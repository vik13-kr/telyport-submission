from rest_framework import serializers
from .models import Member


    
class MemberSeralizer(serializers.ModelSerializer):
    '''
    Class to buid a serializer for Member Class in models.py

    '''    
    class Meta:
        model = Member
        fields = "__all__"
