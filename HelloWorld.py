from funPython import var2 as var22

var1 = 'hello word '
var2 = 'start crawling'
finded1 = var1.find('h')
finded2 = var2.find('h')
var3 = "I am {0} I am {name}".format("김재철", name="우리집")
print(var1[:5])
print(finded2)
print(var2.split())
print(var2.upper())
print(len(var1.upper()))
print(var1.strip())
print(len(var1.lower()))
print(var3)
a = ["1", "2", "3", "4", "5", "6", "7", "8"]
print(".".join(a))

b = [1, 2, 3, 4, 5, 6, 7]
c = [1, 2, 3, 4, 5, 6, 7, [8, 9, 0]]

print(b + c)
print(b * 3)

a.sort(reverse=True)
print(a)

var3 = dict({"key1": "value1", "key2": "value2"})
var4 = {"key1": "value1", "key2": "value2"}
print(var3)
print(var4)

print(var3['key1'])
print(var4.get('key3', 'default value'))
print(var4.keys())
print(var4.items())

var5 = list(var4.values())
print(var5)

var6 = (1, 2, 3, 4, 5, 6, 7)
print(var6[0:4])

if ('T' in 'hello world'):
    print("김재철")
elif ('h' in 'hello world'):
    print("김은영")

count = 0
while count < 5:
    print('%d 번째' % (count))
    count += 1

for i in range(0, 5):
    print('%d 번째' % (i))

for i in 'hello world':
    print(i)

# print(player_a.show_info())
# print(player_b.show_info())
# print(fx(200, 300))
print('%d 값' % var2)
