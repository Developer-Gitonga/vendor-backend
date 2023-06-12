from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer
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

# def form_list(request):
#     forms = Form.objects.all()
#     return render(request, {'forms': forms})