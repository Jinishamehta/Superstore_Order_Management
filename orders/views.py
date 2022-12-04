from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import *
from .pagination import *
# Create your views here.

def loginPage(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("Hello")
            return redirect('index')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context = {'form':form}
    return render(request,'orders/login.html',context)

def index(request):
    context = {'data':"Welcome TO Wow"}
    return render(request,'orders/index.html',context)

def getCustomers(request):
    data = mm_customer.objects.raw(
        "SELECT * FROM mm_customer"
    )
    context = {'data': data}
    return render(request, 'orders/customers.html',context)

class ViewOrders(viewsets.ModelViewSet):
    queryset = mm_order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = LargeResultsSetPagination

def OrderDetials(request, pk):
    try:
        order = mm_order.objects.get(pk=pk)
    except mm_order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    context = {
        'request': Request(request),
    }

    if request.method == 'GET':
        serializer = OrderSerializer(instance=order, context=context)
        return Response(serializer.data)


