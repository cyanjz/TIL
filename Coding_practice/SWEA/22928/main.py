import sys
sys.stdin = open('input.txt','r')

# 강사님 코드 복습

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work_t = [0]     # 각 작업(idx)의 작업 시간을 기록.
    pre = [[] for _ in range(N+1)]   # 각 작업에서 선행되어야 하는 작업 목록
    next = [[] for _ in range(N+1)]  # 각 작업 이후에 시행되어야 하는 작업 목록
    ready2 = [0] # 각 작업 별 남은 선행 작업의 개수
    for idx in range(1,N+1):
        arr = list(map(int,input().split()))
        work_t.append(arr[0])
        ready2.append(arr[1])
        for work in arr[2:]:
            pre[idx].append(work)
            next[work].append(idx)

    min_time = 10000000000000000
    for i in range(1,N+1):
        tmp = work_t[i]
        work_t[i] //= 2

        # 반복을 위한 복사
        ready = ready2[:]

        finish_t = [0] * (N + 1)  # 각 작업이 완료된 시간이 기록
        q = []  # 현재 작업 중인 작업이 들어갈 큐
        # 선행 작업이 없는 작업들을 먼저 수행한다
        for i in range(1, N + 1):
            if ready[i] == 0:
                q.append(i)

        # 작업할 수 있는 일이 없을 때까지 반복할 것
        while q:
            v = q.pop(0)
            for j in next[v]:  # i를 선행작업으로 가지는 작업들의 목록
                ready[j] -= 1  # 선행 작업 개수 1 감소
                if ready[j] == 0:  # 선행 작업이 방금 0이 되었다면, 큐에 추가
                    q.append(j)
            max_time = 0
            for k in pre[v]:  # 현재 작업의 선행 작업 목록
                if finish_t[k] > max_time:
                    max_time = finish_t[k]  # 그 중 가장 늦게 끝난 거 찾기
            finish_t[v] = max_time + work_t[v]  # 끝난 시간 기록

        if 0 in finish_t[1:]:  # 완료되지 않은 일이 있다면, -1 출력하고 종료
            print(f'#{tc} -1')
            break

        if min_time > max(finish_t):
            min_time = max(finish_t)

        work_t[i] = tmp

    else:
        print(f'#{tc} {min_time}')


    # last = finish_t.index(max(finish_t))    # 마지막으로 끝난 일이 무엇인지
    # print(finish_t)
    # print(finish_t[last])
    # max_time = 0
    # for work in pre[last]:
    #     if work_t[work] > max_time: # 해당 일의 선행 작업 중 가장 오래 걸린 것은?
    #         work_need_help = work
    #         max_time = work_t[work]
    # if work_t[last] > max_time: # 해당 일까지 포함해서 체크
    #     work_need_help = last   # 그럼 가장 오래 걸린 이게 도움이 필요한 일이다.
    #
    # work_t[work_need_help] //= 2    # 해당 작업의 시간 절반으로 줄임

    # 1 377
    # 2 906
    # 3 -1
    # 4 11877
    # 5 13278
