from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET', 'POST'])
def home(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)
    if not serializer.is_valid():
        return Response(
            {
                'status': 'error',
                'message': serializer.errors
            }
        )
    serializer.save()
    return Response(
        {
            'status': 'success',
            'payload': data,
            'message': 'Student created successfully'
        }
    )

@api_view(['PUT'])
def update_student(request,id):
    student_obj = Student.objects.get(id=id)
    serializer = StudentSerializer(student_obj, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(
            {
                'status': 'error',
                'message': serializer.errors
            }
        )
    serializer.save()
    return Response({
        'mesaage': 'Student updated successfully'
    })
