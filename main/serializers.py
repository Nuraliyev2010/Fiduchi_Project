from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Home_At_your_departmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home_At_your_department
        fields = "__all__"


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class Home_Connection1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Home_Connection1
        fields = "__all__"


class Home_Connection2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Home_Connection2
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class SavedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = "__all__"