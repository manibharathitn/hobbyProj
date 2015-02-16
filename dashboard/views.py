from django.shortcuts import render
from dashboard.chartutil import ChartData
from django.http import HttpResponse
import json

# Create your views here.

def detail(request):
    return render(request, 'dashboard/index.html')

#for graph1
def getPendingBooking(request):
	params = request.GET
	groupby = params.get('by', '')

    #groupby = by

	#data = {}
	data = ChartData.getChartData(groupby)

	return HttpResponse(json.dumps(data), content_type='application/json')

