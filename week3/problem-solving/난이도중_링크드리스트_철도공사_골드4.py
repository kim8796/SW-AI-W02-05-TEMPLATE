# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

import sys 

def main():

    station_count , build_count = list(map(int,(sys.stdin.readline().split())))
    stations = list(map(int,sys.stdin.readline().split()))
    # build_order = [a for a in (sys.stdin.readline().split() for _ in range(build_count))] 

    # constraint 에 맞는 이중 배열 생성 
    MAX = 1_000_000
    nxt = [0]*(MAX+1)
    prv = [0]*(MAX+1)
    print_subway = []
    # 고유번호는 배열 index 로 매칭 
    for i in range(station_count):
        cur = stations[i]
        nxt[cur] = stations[(i+1)%station_count]
        prv[cur] = stations[(i-1)%station_count]

    # for build in build_order:
    for _ in range(build_count):
        build = sys.stdin.readline().split()
        on = int(build[1])
        if build[0] == "BN":
            newn = int(build[2])
            print_subway.append(str(nxt[on]))
            nxt[newn] = nxt[on]
            prv[nxt[newn]] = newn
            nxt[on] = newn
            prv[newn] = on
            station_count+=1
        elif build[0] == "BP":
            newn = int(build[2])
            print_subway.append(str(prv[on]))
            prv[newn] = prv[on]
            nxt[prv[newn]] = newn
            prv[on] = newn
            nxt[newn] = on
            station_count+=1
        elif build[0]=="CN":
            if station_count >= 2:
                nnx = nxt[nxt[on]]
                print_subway.append(str(nxt[on]))
                nxt[on] = nnx
                prv[nnx] = on
                station_count -=1
        elif build[0] == "CP":
            if station_count >= 2:
                print_subway.append(str(prv[on]))
                prv[on] = prv[prv[on]]
                nxt[prv[on]] = on
                station_count -=1
    sys.stdout.write("\n".join(print_subway))
    



        
    

    





if __name__ == "__main__" :

    main()