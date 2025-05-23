from rest_framework import viewsets

from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet to provide CRUD functionality for Member models
    """
    serializer_class = MemberSerializer

    def get_queryset(self):
        """
        Can be adjusted to filter for specific members
        :return: QuerySet
        """
        return Member.objects.all()
