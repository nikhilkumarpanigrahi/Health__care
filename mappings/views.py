from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import PatientDoctorMapping
from .serializers import MappingSerializer, MappingDetailSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MappingDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # GET /api/mappings/<patient_id>/ — all doctors assigned to a patient
    def get(self, request, pk):
        mappings = PatientDoctorMapping.objects.filter(patient_id=pk)
        serializer = MappingDetailSerializer(mappings, many=True)
        return Response(serializer.data)

    # DELETE /api/mappings/<id>/ — remove a mapping by its ID
    def delete(self, request, pk):
        try:
            mapping = PatientDoctorMapping.objects.get(pk=pk)
        except PatientDoctorMapping.DoesNotExist:
            raise NotFound('Mapping not found.')
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
