driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit 
age = input ('請問你的年齡?')
age = int(age)
if driving == '有' :
	if age >= 18 :
		print ('有駕照乖寶寶')
	else:
		print('無照駕駛壞寶寶')
elif driving == '沒有':
	if age >= 18 :
		print('怎不考?')
	else:
		print('慢慢長大')
else:
	print('請依照格式回答')
