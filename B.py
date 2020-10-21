gold = int(input())
price = input()
price_for_number = [int(i) for i in price.split(" ")]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mark_for_number = []

for i in range(0, 9):
	mark_for_number.append(number[i] / price_for_number[i])

num = []
max_mark = mark_for_number.index(max(mark_for_number))
while gold >= 0:
	if gold - price_for_number[max_mark] < 0:
		del mark_for_number[max_mark], number[max_mark], price_for_number[max_mark]
		if not mark_for_number:
			break
		max_mark = mark_for_number.index(max(mark_for_number))
	else:
		if gold - price_for_number[max_mark] < 0:
			break
		num.append(str(number[max_mark]))
		gold -= price_for_number[max_mark]
if len(num) == 0:
	num = -1
	print(num)
else:
	num = sorted(num, reverse=True)
	print(''.join(num))
