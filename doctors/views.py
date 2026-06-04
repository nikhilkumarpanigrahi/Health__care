from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return Doctor.objects.get(pk=self.kwargs['pk'])
        except Doctor.DoesNotExist:
            raise NotFound('Doctor not found.')
