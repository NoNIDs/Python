sumRes = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sumRes += i

print(sumRes)

# professional method solving problem
# a=[x for x in range(1,1000) if x%3==0 or x%5==0]
# print(sum(a))