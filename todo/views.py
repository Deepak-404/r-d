from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
import logging

logger = logging.getLogger(__name__)
class TodoViewSet(ModelViewSet):
    """
    A viewset that provides the standard actions
    (list, create, retrieve, update, destroy) for the Todo model.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = Todo.objects.create(**serializer.validated_data)
        print(f"Saved Todo: {todo}")  # Debugging
        return Response(serializer.data, status=201)

    

    def update(self, request, *args, **kwargs):
        """
        Override the update method for customized update behavior.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Override the destroy method to customize deletion if needed.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
