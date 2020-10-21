string = input()
n = int(string.split(" ")[0])
k = int(string.split(" ")[1])


i = 2
arr_mlp = []
a = k


while i * i <= a:
	if a % i == 0:
		arr_mlp.append(i)
		a //= i
	else:
		i += 1
arr_mlp.append(a)
arr_mlp = list(set(arr_mlp))

for i in arr_mlp:
	for j in arr_mlp:
		if i * j <= k:
			arr_mlp.append(i * j)

# arr_mlp = set(arr_mlp)
final_arr = []

for i in arr_mlp:
	if k % i == 0 and k / i <= n and i <= n:
		final_arr.append(k / i)
		final_arr.append(i)
final_arr = set(final_arr)
print(len(final_arr))