g = '1223'   # zadanie: zsumować dwa na pozycji ll i ll+1
ll = 1
# g[od:do], przy czym "od" włączone, "do" jest wyłączone

prefix = g[:ll]
suffix = g[ll+2:]
mid = str(int(g[ll]) + int(g[ll+1]))
print('prefix=',prefix)
print('suffix=', suffix)
print('mid=', mid)
tot = prefix + mid + suffix
print('total=', tot, int(tot))
