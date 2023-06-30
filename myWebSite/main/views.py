from django.shortcuts import render

# Create your views here.
#  def index(request):
#      return render(request, "main/index.html")

from .models import Testdata

#  def testdata_view(request):
#      data = Testdata.objects.all()
#      # print(data)
#      return render(request, 'main/index.html', {"data": data})

def index(request):
    data = Testdata.objects.all()
    # print(data)
    return render(request, 'main/index.html', {"data": data})
