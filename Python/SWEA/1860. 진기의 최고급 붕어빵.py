# 일단 손님들이 도착하는 시간을 오름차순으로 정렬을 한다.
# 오름차순으로 정렬된 도착시간을 탐색하며 해당 시간에 붕어빵이 있는지 없는지 검사한다.
# 예를 들어 첫 도착 시간이 4초, 붕어빵 만드는데 걸리는 시간이 2초, 한번에 만들 수 있는 개수 2개라고 한다면
# 4초(도착시간)//2초(붕어빵제작시간)*2개(한번에 만든 개수)-0개(앞 손님이 먹고간 개수)=4개(해당 도착시간까지 만들 수 있는 붕어빵 개수)
# 이와 같은 연산을 통해 해당 시간의 붕어빵 개수를 구하고 그 시간에 도착한 손님에게 줄 수 있다면 (1이상이라면) eat+=1 해준다.
# 즉 다음 연산에서는 다음 도착시간//2초(붕어빵제작시간)*2개(한번에 만든 개수)-1개(앞 손님이 먹고간 개수)를 해주면 된다.


T=int(input())
for t in range(1,T+1):
    n,m,k=map(int,input().split())
    ls=list(map(int,input().split()))
    ls.sort()
    eat=0
    for i in ls:
        if (i//m)*k-eat<=0:
            print(f"#{t} Impossible")
            break
        else:
            eat+=1
    else:
        print(f"#{t} Possible")
    