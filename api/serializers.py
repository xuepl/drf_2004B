
from rest_framework import serializers

from api.models import Project


class SerializersProject(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True,min_length=4,max_length=40)
    version=serializers.CharField(max_length=50,default='v0.1')
    type = serializers.CharField(max_length=50, default="Web")
    description = serializers.CharField(max_length=1024, allow_blank=True, allow_null=True)
    status = serializers.BooleanField(default=True)
    LastUpdateTime = serializers.DateTimeField(read_only=True)
    createTime = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key in validated_data:
            setattr(instance, key, validated_data[key])
        return instance


class ModelSerializerProject(serializers.ModelSerializer):
    task_count = serializers.SerializerMethodField(label="任务数",read_only=True)

    class Meta:
        model=Project
        fields="__all__"
        extra_kwargs = {
            "name":{
                "required":True,
                "max_length":40,
                "min_length":4,
                "error_messages": {
                    "required": "项目名是必填字段",
                    "max_length": "项目名不能超过40位",
                    "min_length": "项目名不能低于4位"
                }
            }
        }
    def get_task_count(self,obj):

        return 100


