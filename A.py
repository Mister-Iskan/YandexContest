import sys
j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()
res_list = [i for i in s if i in j]
print(len(res_list))
