from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, BookSerializer, CategorySerializer
from .models import Student,Book

# Create your views here.
@api_view(['GET'])
def home(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({
        'books': serializer.data
    })

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
    try:
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
    except Exception as e:
        print(e)
        return Response({
            'message': 'Student not found'
        })

@api_view(['DELETE'])
def delete_student(request,id):
    try:
        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({
            'message': 'Student deleted successfully'
        })

    except Exception as e:
        return Response({
            'message': 'Student not found'
        })