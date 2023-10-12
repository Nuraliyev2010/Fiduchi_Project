from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def get_category_name(request):
    category_name = Category.objects.all()
    ser = CategorySerializers(category_name, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_home_at_your_department(request):
    department = Home_At_your_department.objects.last()
    ser = Home_At_your_departmentSerializers(department)
    return Response(ser.data)


@api_view(["GET"])
def get_home_department(request):
    department2 = Department.objects.all()
    ser = DepartmentSerializers(department2, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_home_connection1(request):
    home_connection1 = Home_Connection1.objects.last()
    ser = Home_Connection1Serializers(home_connection1)
    return Response(ser.data)


@api_view(["GET"])
def get_home_connection2(request):
    home_connection2 = Home_Connection2.objects.all()
    ser = Home_Connection2Serializers(home_connection2, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    ser = ProductSerializers(products, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_size(request, pk):
    category = Category.objects.get(pk=pk)
    size = request.GET.get('size')
    product = Product.objects.filter(size=size)
    ser = ProductSerializers(product, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_color(request, pk):
    category = Category.objects.get(pk=pk)
    color = request.GET.get('color')
    product = Product.objects.filter(color = color)
    ser = ProductSerializers(product, many=True)
    return Response(ser.data)


@api_view(["GET"])
def get_name(request, pk):
    category = Category.objects.get(pk = pk)
    name = request.GET.get('name')
    product = Product.objects.filter(name = name)
    ser = ProductSerializers(product, many=True)
    return Response(ser.data)


