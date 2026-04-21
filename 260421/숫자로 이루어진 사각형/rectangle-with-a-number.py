n = int(input())

# Please write your code here.


def print_(n):
    a=1
    for i in range(n):
        for j in range(n):
            if a==10: a=1
            print(a, "", end="")
            a+=1
        print()

print_(n)