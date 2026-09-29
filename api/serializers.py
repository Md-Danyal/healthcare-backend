from rest_framework.serializers import ModelSerializer
from .models import User, Patient, Doctor, Mapping

class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = ["id","name","email","password"]
    extra_kwargs = {
      "password": {"write_only": True}
    }
    
  def create(self, validated_data):
    user = User(
      name = validated_data["name"],
      email = validated_data["email"]
    )
    user.set_password(validated_data["password"])
    user.save()
    return user
  
class PatientSerializer(ModelSerializer):
  class Meta:
    model = Patient
    fields = "__all__"
    read_only_fields = ["user"]
    
class DoctorSerializer(ModelSerializer):
  class Meta:
    model = Doctor
    fields = "__all__"
    
class MappingSerializer(ModelSerializer):
  class Meta:
    model = Mapping
    fields = "__all__"