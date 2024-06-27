from django.shortcuts import render

# Create your views here.
def anil(request):
    d={'name':'anilkumar','age':45}
    return render(request,'anil.html',d)
