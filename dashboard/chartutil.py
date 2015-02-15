class ChartData:
	@classmethod
	def getChartData(groupByFeild):	
		data = {}
		result = Booking.objects.values(groupByFeild).annotate(Sum('Pending'))
		result = list(result)
		data['X'] = [pen_mon[groupByFeild] for pen_mon in result]
		data['Y'] = [pen_mon['Pending__sum'] for pen_mon in result]
		
		return data
