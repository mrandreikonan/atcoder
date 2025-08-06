# ------------------------------
# ABC417 D - Takahashi’s Expectation
# Аўтарскі алгарытм перакладзены з C++ (editorial) і адаптаваны на Python
# Рэалізавана ChatGPT па тваім запыце
# ------------------------------

import sys
import bisect

def main():
    input = sys.stdin.readline

    # Чытаем колькасць падарункаў
    N = int(input())
    P, A, B = [], [], []

    # Чытаем самі падарункі
    for _ in range(N):
        p, a, b = map(int, input().split())
        P.append(p)
        A.append(a)
        B.append(b)

    # Чытаем колькасць запытаў і значэнні X
    Q = int(input())
    X_list = [int(input()) for _ in range(Q)]

    # Максімальна магчымы настрой, які мае сэнс для DP
    M = max(P[i] + A[i] for i in range(N))

    # Ініцыялізуем dp-масіў: dp[i][j] = настрой пасля ўсіх падарункаў, калі цяпер i-ты і настрой j
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Базавы выпадак: пасля ўсіх падарункаў канчатковы настрой — гэта той, што маем
    for j in range(M + 1):
        dp[N][j] = j

    # Запаўняем dp у зваротным парадку
    for i in range(N - 1, -1, -1):
        for j in range(M + 1):
            if j <= P[i]:
                nj = min(M, j + A[i])  # павелічэнне настрою
            else:
                nj = max(0, j - B[i])  # памяншэнне настрою
            dp[i][j] = dp[i + 1][nj]

    # Кумулятыўная сума стратаў B: cumB[i] = сума B[0] + ... + B[i-1]
    cumB = [0] * (N + 1)
    for i in range(N):
        cumB[i + 1] = cumB[i] + B[i]

    # Апрацоўка запытаў
    res = []
    for X in X_list:
        if X <= M:
            # Калі пачатковы настрой малы — проста бярэм з dp
            res.append(dp[0][X])
        else:
            # Знаходзім, колькі стратаў трэба, каб апусціцца ў зону dp
            target = X - M
            idx = bisect.bisect_left(cumB, target)
            if idx >= len(cumB):
                # Нават пасля ўсіх стратаў настрой занадта вялікі — вылічаем наўпрост
                res.append(X - cumB[N])
            else:
                j = X - cumB[idx]
                # Засцярога: абрэзаем j у межах [0, M]
                j = min(max(j, 0), M)
                res.append(dp[idx][j])

    # Вывад усіх адказаў
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()