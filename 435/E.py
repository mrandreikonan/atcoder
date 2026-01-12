from atcoder.lazysegtree import LazySegTree

# --- Monoid over S = (sum, len) ---
def op(a, b):
    # merge two nodes: sum adds, length adds
    return (a[0] + b[0], a[1] + b[1])

def e():
    # identity: sum=0, len=0
    return (0, 0)

# --- Lazy tag F = add value (number) ---
def mapping(f, x):
    # apply: add f to all elements in this segment
    # sum increases by f * len; len unchanged
    return (x[0] + f * x[1], x[1])

def composition(f, g):
    # apply g first, then f; for addition it's commutative, so f + g works
    return f + g

def id():
    # identity tag is 0: add nothing
    return 0


N, Q = map(int, input().split())
LLT = LazySegTree(op, e, mapping, composition, id, init)

for _ in range(Q):
    L, R = map(int, input().split())
