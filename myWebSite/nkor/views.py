from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "nkor/index.html")

def nkor_view(request):
    return render(request, "nkor/main.html")

from .models import Testdata

#  def testdata_view(request):
#      data = Testdata.objects.all()
#      # print(data)
#      return render(request, 'main/index.html', {"data": data})

def mirror_view(request):
    data = Testdata.objects.all()
    # print(data)
    return render(request, 'nkor/mirror.html', {"data": data})
