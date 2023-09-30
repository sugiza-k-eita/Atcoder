"""
問題文 N 個のピースに分かれている円形のホールケーキがあり、時計回りで i 番目にあるピース（以下、ピース i とする）の大きさは A i ​ です。 1≤i≤N−1 に対し、ピース i とピース i+1 は隣接しており、ピース N とピース 1 も隣接しています。 ケーキのある連続するピースを選ぶ方法であって、選んだ部分が全体の大きさのちょうど 10 分の 1 になるものは存在するか、判定してください。
"""
N = int(input())
A = list(map(int, input().split()))
A2 = A * 2  # 配列を2倍に
total = sum(A)
K = total // 10  # 全体の大きさの10分の1

if total % 10 != 0:  # もし10で割り切れないなら、解は存在しない
    print("No")
    exit()
else:
    left, x = 0, 0
    for right in range(2*N):  # 2*Nまで探索する
        x += A2[right]  # rightを1つ進めるたびにxに加える
        while x > K:  # xがKを超えた場合、leftを進める
            x -= A2[left]
            left += 1
        if x == K:  # xがKと等しいならYesを出力
            print("Yes")
            exit()

print("No")
