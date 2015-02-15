from django.shortcuts import render
from dashboard.models import Booking
from dashboard.chartutil import ChartData
import json
#from django.http import HttpResponse

# Create your views here.

def detail(request):
    return render(request, 'dashboard/index.html')

#for graph1
def getPendingBooking(request):
	params = request.GET
	groupby = params.get('by', '')
	data = ChartData.getChartData(groupby)
	
	return HttpResponse(json.dumps(data), content_type='application/json')
