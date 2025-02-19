import sys


sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

print(sys.stdin.readline().rstrip())
print(sys.stdin.readline())
print(sys.stdin.readline())
