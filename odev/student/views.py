from django.shortcuts import render

# Create your views here.
from .models import Student
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework import filters

from .serializers import StudentSerializer


class StudentViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  GenericViewSet):
    """
    The following endpoints are fully provided by mixins:
    * List view
    * Create view
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = [JSONRenderer]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=no']


def index(request):
    return render(request, 'index.html')

