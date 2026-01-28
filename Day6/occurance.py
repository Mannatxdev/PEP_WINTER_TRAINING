s = input().strip()
    
c = {}
for ch in s:
    c[ch] = c.get(ch, 0) + 1

t3 = sorted(c.items(), key=lambda x: x[1], reverse=True)[:3]
print(t3)
