# Задача: ABC417 C – Distance Indicators
# Рашэнне зроблена праз ChatGPT на базе афіцыйнага разбору

from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))

    # Слоўнік для падліку колькасці сустрэтых значэнняў i + A[i]
    count = defaultdict(int)
    ans = 0

    for j in range(N):
        key = j - A[j]
        # Колькі разоў сустракалася i + A[i] = j - A[j]
        ans += count[key]
        # Запамінаем j + A[j] для будучых праверак
        count[j + A[j]] += 1

    print(ans)

if __name__ == "__main__":
    main()