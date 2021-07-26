from itertools import permutations

if __name__ == '__main__':
    a= list(map(int,input().split(" ")))
    target =input()
    per=list(permutations(a,2))
    sol=[]
    for x in per:
        if (int(x[0])+int(x[1]))==int(target):
            sol.append(a.index(x[0]))
            sol.append(a.index(x[1]))
            break

    print(sol)