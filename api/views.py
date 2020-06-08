

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Project
from api import serializers


# class Projects(APIView):
#
#     def get(self,request):
#         projects = Project.objects.all()
#         serializer = SerializersProject(instance=projects,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         data = request.data # request.POST request.body
#         serializer = SerializersProject(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return  Response(serializer.validated_data)

class Projects(APIView):

    def get(self,request):
        projects = Project.objects.all()
        serializer = serializers.ModelSerializerProject(instance=projects,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data # request.POST request.body
        serializer = serializers.ModelSerializerProject(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return  Response(serializer.validated_data)




