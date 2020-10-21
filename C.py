str = input().split(' ')
t = int(str[0])
k = int(str[1])
m, n, win_list = [], [], []

for i in range(t):
	a = input().split(" ")
	m, n = int(a[0]), int(a[1])
	quntity_moves = m + n -2
	if k >= n or k >= m:
		if quntity_moves % 2 == 0:
			win_list.append('-')
		else:
			win_list.append('+')
	else:
		# while quntity_moves - k*2 + 1 <=0:
		# 	quntity_moves -= k*2 + 1
		# if quntity_moves % 2 == 0:
		# 	win_list.append('-')
		# else:
		# 	win_list.append('+')

		count_k = 0
		if m >= n:
			count_k = int((n - 1) / k)
		else:
			count_k = int((m - 1) / k)
		if quntity_moves % 2 == 1 and quntity_moves - (count_k * k * 2) - 1 >=0:
			if count_k % 2 == 0:
				win_list.append('+')
			else:
				win_list.append('-')
		elif quntity_moves % 2 == 1 and quntity_moves - (count_k * k * 2) - 1 < 0:
			win_list.append('+')
		elif quntity_moves % 2 == 0:
			if count_k % 2 == 1:
				win_list.append('+')
			else:
				win_list.append('-')
		else:
			if count_k % 2 == 1:
				win_list.append('+')
			else:
				win_list.append('-')


for i in range(len(win_list)):
	print(win_list[i])



