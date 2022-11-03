from rest_framework import serializers

from Octomber_Hackathon.api.models import Companies
from Octomber_Hackathon.auth_app.models import AdvocateProfile, AdvocateUser


# class LinksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Links
#         fields = '__all__'
#

class CompanySerializer(serializers.ModelSerializer):
    # TODO fix this problem class --> 'CompanySerializer' object has no attribute 'get_employee_count'
    # employee_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Companies
        fields = '__all__'

    # @staticmethod
    # def get_employees_count(self, obj):
    #     count = obj.advocate_set.count()
    #     return count


class ListAdvocatesSerializer(serializers.ModelSerializer):
    profile_pic = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        return obj.profile_pic.url

    company = CompanySerializer(read_only=True)

    class Meta:
        model = AdvocateProfile
        fields = '__all__'


'''
{
    "id":1,
    "name":"Dennis Ivy",
    "profile_pic":"/user_pic.png",
    "short_bio":"...",
    "long_bio":"...",
    "advocate_years_exp":1,
    "company":{
        "id":6,
        "name":"Agora",
        "logo":"agora_logo.png",
        "href":"/companies/6",
    },
    "links":{
        "youtube":"youtube.com/username",
        "twitter":"twitter.com/username",
        "github":"github.com/username",
    }
}'''


class CreateAndEditAdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = AdvocateProfile
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user


class RetrieveAdvocateSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = AdvocateProfile
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = AdvocateProfile
        fields = ('field', 'image', 'image_url')

    def get_image_url(self, obj):
        return obj.image.url
