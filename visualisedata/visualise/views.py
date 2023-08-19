from .serializers import DetailSerializer
from . models import details
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import View
from django.shortcuts import render,redirect



class home(View):
    def get(self,request):
        return render(request,'home.html')

class range(ModelViewSet):
    queryset=details.objects.all()
    serializer_class=DetailSerializer

    def get_queryset(self):
        x,y=0,10000
        if self.request.GET.get('start_year')=='' or self.request.GET.get('start_year')==None:
            x=0
        else:
            x=int(self.request.GET.get('start_year'))
        if self.request.GET.get('end_year')=='' or self.request.GET.get('end_year')==None:
            y=10000
        else:
            y=int(self.request.GET.get('end_year'))
        return details.objects.filter(start_year__gt=x,start_year__lt=y)
        

class intensity(ModelViewSet):
    queryset=details.objects.all()
    serializer_class=DetailSerializer

    def get_queryset(self):
        x,y=0,100000000
        if self.request.GET.get('start')=='' or self.request.GET.get('start')==None:
            x=0
        else:
            x=int(self.request.GET.get('start'))
        if self.request.GET.get('end')=='' or self.request.GET.get('end')==None:
            y=100000000
        else:
            y=int(self.request.GET.get('end'))
        return details.objects.filter(intensity__gt=x,intensity__lt=y)

class load_api(ModelViewSet):
    queryset=details.objects.all()
    serializer_class=DetailSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['end_year','topic','sector','region','pestle','source','country','start_year']


















    # def create(self,request):
    #     d1=DetailSerializer(data=request.data)
    #     if d1.is_valid():
    #         d1.save()
    #         return Response({'msg':"data created"})
    #     return Response(d1.errors)
    
    # def list(self,request):
    #     if request.data==None:
    #         d1=details.objects.all()
    #         dser=DetailSerializer(d1,many=True)
    #         return Response(dser.data)
    #     l=list(request.data.keys())+list(request.data.values())
    #     # d1=details.objects.filter(end_year=l[1])
    #     d1=(details.objects.values('country').annotate(dcount=Count('country')).order_by('country'))
    #     print(list(d1))
    #     dser=DetailSerializer(d1,many=True)
    #     return Response(dser.data)
    
    # def retrieve(self,request,pk):
    #     d1=details.objects.get(id=pk)
    #     dser=DetailSerializer(d1)
    #     return Response(dser.data)
