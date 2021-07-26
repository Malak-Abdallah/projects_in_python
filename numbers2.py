# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def sum(l1,l2):
    x=''.join(l1[0:])
    y=''.join(l2[0:])
    sum=str(int(x)+int(y))
    print(list(sum[::-1]))


def main():
    inp = list(map(str,input("enter first list numbers").split(" ")))
    inp2 = list(map(str, input("enter second list numbers").split(" ")))
    sum(inp,inp2)


if __name__ == '__main__':
    main()
