from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer, BookSerializer, CategorySerializer, UserSerializer
from .models import Student, Book
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your views here.

@api_view(['GET'])
def get_book(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response({
        'books': serializer.data
    })


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    'status': 'error',
                    'message': serializer.errors
                }
            )
        serializer.save()


        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ = Token.objects.get_or_create(user=user)


        return Response(
            {
                'status': 'success',
                'payload': request.data,
                'message': 'User created successfully',
                'token': str(token_obj)
            }
        )


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
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
                'payload': request.data,
                'message': 'Student created successfully'
            }
        )

    def put(self, request):
        pass

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(
                student_obj, data=request.data, partial=True)
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

    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({
                'message': 'Student deleted successfully'
            })

        except Exception as e:
            return Response({
                'message': 'Student not found'
            })


