from rest_framework import serializers

from Octomber_Hackathon.api.models import Companies
from Octomber_Hackathon.auth_app.models import AdvocateProfile


class CompanySerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Companies,
        fields = '__all__'

    @staticmethod
    def get_employees_count(self, obj):
        count = obj.advocate_set.count()
        return count


class ListAdvocatesSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = AdvocateProfile
        fields = '__all__'


class CreateAndEditAdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateProfile
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user
