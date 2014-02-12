import time

"""
January		1
February	2
March		3
April		4
May			5
June		6
July		7
August		8
September	9
October		10
November	11
December	12

Sunday		1
Monday		2
Tuesday		3
Wednesday	4
Thursday	5
Friday		6
Saturday	7
"""

thirty_day_months = set([4, 6, 9, 11])
thirty_one_day_months = set([1,3,5,7,8,10,12])

def next_month(start, endyear):
	day, month, year = start
	while year != endyear:
		yield (day, month, year)
		if month in thirty_day_months:
			day = day + 2
		elif month in thirty_one_day_months:
			day = day + 3
		elif year % 4 == 0:
			day = day + 1
		# update day, month, and year
		if day > 7:
			day = day % 7
		if month == 12:
			month = 1
			year = year + 1
		else:
			month = month + 1

if __name__ == "__main__":
	start = time.time()
	n_sundays = sum( (d[0] for d in next_month((3,1,1901),2001) if d[0] == 1) )
	elapsed = time.time() - start
	print "found %d after %f seconds" % (n_sundays, elapsed)