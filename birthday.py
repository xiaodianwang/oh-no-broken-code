from datetime import datetime

number_endings = {
    1: 'st',
    2: 'nd',
    3: 'rd'
}

today = datetime.now()
todays_day = today.day
# get the right ending, e.g. 1 => 1st, 2 => 2nd
# but beware! 11 => 11th, 21 => 21st, 31 => 31st

# test your code by forcing todays_day to be something different

def format_day(day):
	ending = 'th'
	if day < 10 or day > 20:
		# x % y (mod) will give the remainder when x is divided by y
		# -- but x needs to be an integer!
		number = day % 10
		# look up number in number_endings
		# and if you find it as a key, put the value in ending
		if number in number_endings:
			# make this print ending, not 'th'
			ending = number_endings[number]
	formatted_date = str(day) + ending
	return formatted_date

print "Today is the {}".format(format_day(todays_day))

birthday = int(raw_input("What day of the month is your birthday?\n"))

# make this print the birthday, and the right ending
print "Your birthday is on the {}".format(format_day(birthday))