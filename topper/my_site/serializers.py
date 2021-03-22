from rest_framework import serializers
from .models import *



class TopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topper
        fields = ('owner', 'topper_name', 'logo', 'info', 'money', 'id')


class TopperCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topper
        fields = ('topper_name', 'logo', 'info', 'money', 'id')

    def create(self, validated_data):
        print('STARTED')
        print("create func in ser", self.context)
        owner = self.context.get('owner')
        print('in serializers', self.context)
        topper = Topper.objects.create(owner=owner, **validated_data)
        topper.save()
        return topper


class TopperDetailSerializer(serializers.ModelSerializer):
    comment = Commentary.objects.all()

    class Meta:
        model = Topper
        fields = ('owner', 'topper_name', 'logo', 'info', 'id', 'comment')


class TopperEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topper
        fields = ('topper_name', 'logo', 'info', 'id')



class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('topper', 'title', 'body', 'created_at', 'id')

        def to_representation(self, instance):
            representation = super().to_represetation(instance)
            representation['image'] = instance.images.count()
            representation['topper'] = instance.topper.topper_name
            return representation


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('body', 'topper')

 
class AdvertisementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('topper', 'body', 'created', 'id')

        def to_representation(self, instance):
            representation = super().to_represetation(instance)
            representation['image'] = ImageSerializer(instance.images.all(), many=True).data
            representation['topper'] = instance.incident.topper_name
            return representation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdverImage
        fields = ('image', 'description')


class AdvertisementEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('topper', 'body', 'user', 'id')


class AdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdverImage
        fields = ('advertisement', 'image')


class CommentaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('body', 'topper', 'user')


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('body', 'topper', 'user', 'id')
