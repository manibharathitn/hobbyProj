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
  groupby = params.get('by', None)
  isPercent = True
  if not groupby == None:
    isPercent = True if not params.get('percent', None) == None else False


  data = ChartData.getPendingChartData(groupby, isPercent)

  return HttpResponse(json.dumps(data), content_type='application/json')

def getGraphData(request):
  params = request.GET
  month = params.get('for_month', None)
  need = params.get('need', None)
  basedOn = params.get('based_on', None)
  topN = params.get('top', None)
  isAvg = False if params.get('avg', None) == None else True
  data = {}

  if (not month == None and not need == None and not basedOn == None) :

    data = ChartData.getMonthlyChartData(month, need, basedOn, topN, isAvg)

  return HttpResponse(json.dumps(data), content_type='application/json')

