from http import client
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# models.object - serializer of single student data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    print(serializer)
    print(serializer.data)
    # converting above native python code in (serializer) into jason
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)

    # # to send to client as responce
    # return HttpResponse (json_data, content_type='application/json')
    return JsonResponse(serializer.data)




def student_detail(request,st):
    stu1 = Student.objects.all()
    print(stu1)
# this is complex data of model
    stu = Student.objects.get(id = st)
    print(stu)
    # converting above complex data in serializer
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)
    # converting above native python code in (serializer) into jason
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)

    # to send to client as responce
    return HttpResponse (json_data, content_type='application/json')



