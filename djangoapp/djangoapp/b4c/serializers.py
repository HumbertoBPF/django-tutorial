from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from djangoapp.b4c.models import Organization


class SignupSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, data):
        if len(data) < 8:
            raise ValidationError("The username must have at least 8 characters")
        return data

    def validate_password(self, data):
        if len(data) < 8:
            raise ValidationError("The username must have at least 8 characters")
        return data

    def save(self, **kwargs):
        email = self.validated_data["email"]
        username = self.validated_data["username"]
        password = self.validated_data["password"]

        user = User.objects.create(
            email=email,
            username=username,
            password=password
        )

        return user


class MemberSerializer(serializers.Serializer):
    username = serializers.CharField()
    organization = serializers.CharField()

    def save(self, **kwargs):
        username = self.validated_data["username"]
        organization = self.validated_data["organization"]

        user = get_object_or_404(User, username=username)
        organization = get_object_or_404(Organization, name=organization)

        organization.members.add(user)
        organization.save()


class OrganizationSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = "__all__"
