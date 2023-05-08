from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from djangoapp.b4c.serializers import SignupSerializer, MemberSerializer, OrganizationSerializer

from djangoapp.b4c.models import Organization


class SignupView(views.APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(data={
            "email": user.email,
            "username": user.username
        }, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def add_member(request):
    serializer = MemberSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_204_NO_CONTENT)


class OrganizationsView(views.APIView):
    def get(self, request):
        search = request.GET.get("search")

        organizations = Organization.objects.all()

        if search is not None:
            organizations = organizations.filter(name__icontains=search)

        serializer = OrganizationSerializer(organizations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
