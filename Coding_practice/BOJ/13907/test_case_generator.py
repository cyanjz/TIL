import sys

sys.stdout = open('edge_case.txt', 'w')

print(1000, end=" ")
print(30000)
