from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status

# Create your views here.
class TaskViewSet(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request):
        queryset = Task.objects.all()
        serializer = self.serializer_class(queryset, many = True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "status":"success"
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors":serializer.errors
                }
            )
    def put(self, request):
        task = Task.objects.all()
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "status":"success"
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors":serializer.errors
                }
            )
    def patch(self, request):
        task = Task.objects.all()
        serializer = self.serializer_class(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "status":"success"
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors":serializer.errors
                }
            )
    def delete(self, request):
        task = Task.objects.all()
        task.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class CatalogueViewSet(APIView):
    queryset = Catalogue.objects.all
    serializer_class = CatalogueSerializer

    def get(self, request):
        queryset = Catalogue.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                statsu=status.HTTP_200_OK,
                data={
                    "status":"success"
                }
            )
        else: 
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors":serializer.errors
                }
            )
        
    def delete(self, request):
            catalogue = Catalogue.objects.all()
            catalogue.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )


class ProductViewSet(APIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer

    def get(self, request):
        queryset = Product.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK,
                data={
                    "status":"success"
                }
        )
        else: 
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "errors":serializer.errors
                }
            )
        
    def delete(self, request):
            product = Product.objects.all()
            product.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )