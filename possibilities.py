characters = ['','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

results = [(a+b+c+d)
for a in characters
for b in characters
for c in characters
for d in characters]
print(len(results))
with open('possibilites.txt', 'w') as f:
    write(str(results))
