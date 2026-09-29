from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer, MappingSerializer
from .models import Patient, Doctor, Mapping

class RegisterView(APIView):
  def post(self, request):
    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(
        {"message": "user created successfully"},
        status= status.HTTP_201_CREATED
      )
    return Response(
      serializer.errors,
      status= status.HTTP_400_BAD_REQUEST
    )
    
class PatientListCreateView(ListCreateAPIView):
  serializer_class = PatientSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    return Patient.objects.filter(user= self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(user= self.request.user)
    
class PatientDetailView(RetrieveUpdateDestroyAPIView):
  serializer_class = PatientSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    return Patient.objects.filter(user= self.request.user)
  
class DoctorListCreateView(ListCreateAPIView):
  serializer_class = DoctorSerializer
  permission_classes = [IsAuthenticated]
  queryset = Doctor.objects.all()
  
class DoctorDetailView(RetrieveUpdateDestroyAPIView):
  serializer_class = DoctorSerializer
  permission_classes = [IsAuthenticated]
  queryset = Doctor.objects.all()
  
class MappingListCreateView(ListCreateAPIView):
  serializer_class = MappingSerializer
  permission_classes = [IsAuthenticated]
  queryset = Mapping.objects.all()
  
class PatientMappingView(APIView):
  permission_classes = [IsAuthenticated]
  
  def get(self, request, patient_id):
    mappings = Mapping.objects.filter(patient_id = patient_id)
    serializer = MappingSerializer(mappings, many = True)
    
    return Response(serializer.data)
  
class MappingDeleteView(DestroyAPIView):
  serializer_class = MappingSerializer
  permission_classes = [IsAuthenticated]
  queryset = Mapping.objects.all()