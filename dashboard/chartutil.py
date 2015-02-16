from dashboard.models import Booking
from django.db.models import Sum
class ChartData:
	@staticmethod
	def getChartData(groupByFeild):
		data = {}
		result = Booking.objects.values(groupByFeild).annotate(Sum('Pending'))
		result = list(result)
		data['X'] = [str(key_val[groupByFeild]) for key_val in result]
		data['Y'] = [int(key_val['Pending__sum']) for key_val in result]

		return data
