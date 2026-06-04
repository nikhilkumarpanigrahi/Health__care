from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound

from .models import PatientDoctorMapping
from .serializers import MappingSerializer, MappingDetailSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()


class PatientDoctorsView(generics.ListAPIView):
    serializer_class = MappingDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient_id=self.kwargs['patient_id'])


class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return PatientDoctorMapping.objects.get(pk=self.kwargs['pk'])
        except PatientDoctorMapping.DoesNotExist:
            raise NotFound('Mapping not found.')
