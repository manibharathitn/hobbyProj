from dashboard.models import Booking
from django.db.models import Sum, Count, Avg
class ChartData:
  @staticmethod
  def getPendingChartData(groupByFeild, isPercent):
    data = {}
    result = Booking.objects.values(groupByFeild).annotate(Sum('Pending'))
    result = list(result)
    data['X'] = [str(key_val[groupByFeild]) for key_val in result]
    data['Y'] = [int(key_val['Pending__sum']) for key_val in result]

    if isPercent:
      ySum = sum(data['Y'])
      data['Y'] = [ (val*100/float(ySum)) for val in data['Y'] ]

    return data

  @staticmethod
  def getMonthlyChartData(pMonth, need, basedOn, topN, isAvg):
    top = 15 if topN == None else topN
    data = {}
    #Currently average is supported only for duration
    if isAvg and need == 'duration':
      result = Booking.objects.filter(month=pMonth).values(basedOn).annotate(res_val=Avg(need)).order_by('-res_val')
    else:
      result = Booking.objects.filter(month=pMonth).values(basedOn).annotate(res_val=Sum(need)).order_by('-res_val')
    result = list(result)
    result = result[:int(top)]
    data['X'] = [str(key_val[basedOn]) for key_val in result]
    data['Y'] = [int(key_val['res_val']) for key_val in result]

    return data
