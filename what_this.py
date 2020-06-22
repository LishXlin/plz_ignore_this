print('欢迎使用该统计脚本!')
print('MENU:')
print('[1]生成早出勤情况(上午)\n[2]生成听课,作业情况(下午)')
check = int(input('键入[1-2]:'))
if check == 1:
	def userput(msg):
		default = 50
		b = input(msg)
		if b == '':
			return default
		else:
			return b
	total = int(userput('People in Class(default:50):'))
	collected = int(input('Arrive:'))
	print('==============RESULT==============')
	print('出勤:%s/%s'%(collected, total))
	print('出勤率:{:.2%}'.format(collected / total))
	print('===============DONE===============')
if check == 2:
	inclass = input('课堂表现:\n[1]好\n[2]一般\n[3]差\n选择[1-3]')
	homework = input('作业情况:\n[1]好\n[2]一般\n[3]差\n选择[1-3]')
	def inclass1():
		good = '好'
		soso = '一般'
		bad = '差'
		no = '?'
		if inclass == '1':
			return good
		elif inclass == '2':
			return soso
		elif inclass == '3':
			return bad
		else:
			return no
	def hw():
		good = '好'
		soso = '一般'
		bad = '差'
		no = '?'
		if homework == '1':
			return good
		elif homework == '2':
			return soso
		elif homework == '3':
			return bad
		else:
			return no
	print('=========RESULT==========')
	print('课堂情况:',inclass1())
	print('作业情况:',hw())
	print('===========DONE==========')
else:
	print('\033[1;35m ????? \033[0m')
