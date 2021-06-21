import time
password = input('Enter an 4 digit password: ')

t0 = time.time()

characters = ['','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

results = [(a+b+c+d+x)
for a in characters
for b in characters
for c in characters
for d in characters
for x in characters]

for i in results:
    if password == i:
        print('Your password is', i)
        break

print(time.time()-t0)
