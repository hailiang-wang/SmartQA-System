def cmp_ignore_case(s1, s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r=f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()