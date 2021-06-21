#practice-leap
def is_leap(year):  #閏年=TRUE  平年=FALSE
	if year % 4 != 0:
		return False
	elif year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 100 == 0 and year % 400 != 0:
		return False
	elif year % 400 == 0 and year % 3200 != 0:
		return True
while True:
	inputyear = input('請輸入年分,輸入q離開')
	inputyear = str(inputyear)
	if inputyear == 'q':
		break
	else:
		inputyear = int(inputyear)
		print(is_leap(inputyear))