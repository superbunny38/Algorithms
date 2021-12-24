#2828
#사과 담기 게임
#류채은

N,M = map(int, input().split())
J = int(input())
apple_pos = []#사과 위치
for _ in range(J):
    tmp = int(input())
    apple_pos.append(tmp)

r_end = M#바구니오른쪽끝
l_end = 0#바구니왼쪽끝
distance = 0#최단거리
#apple_pos에서 왼쪽으로 갈 때는 -1통일 왜냐하면 N칸이지만 사실상 N+1의크기

for i in range(len(apple_pos)):
    if l_end <= apple_pos[i]-1 and apple_pos[i]<=r_end:
        distance = distance + 0#바구니 위치 범위에 있음
        #print(i+1,"번째 사과에서 이동x")
    elif apple_pos[i] > r_end:
        distance = distance + apple_pos[i] - r_end#오른쪽으로 가야하는 거리
        r_end = apple_pos[i]
        l_end = r_end - M#항상 오른끝이랑 왼끝의 차이는 M만큼
        #print(i+1,"번째사과에서",distance,"만큼 이동")
    elif apple_pos[i]-1<l_end:#왼쪽으로 이동
        distance = distance + l_end - (apple_pos[i]-1)
        l_end = apple_pos[i]-1
        r_end = l_end + M
        #print(i+1,"번째사과에서",distance,"만큼 이동")

print(distance)
