"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import time

number_mapping = {
	"0":"",
	"1":"one",
	"2":"two",
	"3":"three",
	"4":"four",
	"5":"five",
	"6":"six",
	"7":"seven",
	"8":"eight",
	"9":"nine",
	"10":"ten",
	"11":"eleven",
	"12":"twelve",
	"13":"thirteen",
	"14":"fourteen",
	"15":"fifteen",
	"16":"sixteen",
	"17":"seventeen",
	"18":"eighteen",
	"19":"nineteen",
}

two_digit_mapping = {
	"2":"twenty",
	"3":"thirty",
	"4":"forty",
	"5":"fifty",
	"6":"sixty",
	"7":"seventy",
	"8":"eighty",
	"9":"ninety",
}

def number_to_words(n):
	text = str(n)
	words = ""
	power = len(text)
	need_and = False
	for c in text:
		modifier = ""
		if c == "0":
			power = power - 1
			continue
		elif power == 4:
			words = words + number_mapping[c] + " thousand"
		elif power == 3:
			words = words + " " + number_mapping[c] + " hundred"
			need_and = True
		elif power == 2:
			last_two = text[-2:]
			if need_and:
				words = words + " and"
			if last_two in number_mapping:
				words = words + " " + number_mapping[last_two]
			else:
				words = words + " " + two_digit_mapping[last_two[0]] + " " + number_mapping[last_two[1]]
			break
		elif power == 1:
			if need_and:
				words = words + " and"
			words = words + " " + number_mapping[c]
		power = power - 1
	return words


if __name__ == "__main__":
	start = time.time()
	l = 0
	for i in xrange(1,1001):
		l += len(number_to_words(i).replace(" ",""))
	elapsed = (time.time() - start)
	print "found %s in %s seconds" % (l, elapsed)