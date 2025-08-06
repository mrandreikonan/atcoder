# Рашэнне для ABC417 F – Random Gathering
# Выкарыстоўваецца atcoder.lazysegtree (афіцыйная Python бібліятэка)

from atcoder.lazysegtree import LazySegTree

MOD = 998244353
INF = 10 ** 18

# Кожны вузел захоўвае (total_value, count)
e = (0, 0)  # нейтральны элемент для сумаў
id_ = INF  # спецыяльнае значэнне для таго, каб нічога не рабіць (lazy)

# Аб’яднанне двух сегментаў: проста складаем
def op(a, b):
    return ((a[0] + b[0]) % MOD, (a[1] + b[1]) % MOD)

# Як прымяніць аперацыю f да сегмента s
def mapping(f, s):
    if f == id_:
        return s
    return ((f * s[1]) % MOD, s[1])

# Як аб’яднаць дзве аперацыі f(g(x)) → f пасля g
def composition(f, g):
    return g if f == id_ else f

# Увод
N, M = map(int, input().split())
A = list(map(int, input().split()))

# Ініцыялізуем LazySegTree
lz = LazySegTree(op, e, mapping, composition, id_, [(a, 1) for a in A])

# Апрацоўка аперацый
for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    total, size = lz.prod(l, r)
    inv = pow(size, MOD - 2, MOD)
    avg = total * inv % MOD
    lz.apply(l, r, avg)

# Вывад
print(*[lz.get(i)[0] for i in range(N)])