a = int(input())
c = [0] * a
for i in range(a):
   c[i] = [0] * a
dx, dy, x, y = 1, 0, -1, 0
for i in range(a ** 2):
   if not(0 <= x + dx < a and 0 <= y + dy < a and c[y+dy][x+dx] == 0):
       dx, dy = -dy, dx
   x += dx
   y += dy
   c[y][x] = i + 1
for i in range(a):
   print(*c[i])