#list
'''text=["ram","sita","shyam","hari"]
print(text)
print(text[2])
print(text[-3])
print(text[0:2])
print(text[:2])
print(text[3:])
text[1]="razesh"
print(text)
for x in text:
    print(x)
print(len(text))
text.pop()
print(text)'''

years = list(range(2000, 2030))
for year in years:
    if year % 4 == 0:
        print(year)

