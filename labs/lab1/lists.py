l1 = [1,2,3]
l1.reverse()
# print(l1)

l2 = ['abc', 'xyz', 'aba', '1221', 'abba']
count = 0
for word in l2:
  if len(word) >= 2 and word[0] == word[-1]:
    count = count +1

print(count)

# list comprehension
# i) 
names = ['muzzamil', 'ali', 'NAbeel', 'hUzaifa', 'hina', 'umer']
newNames = [name.lower() for name in names if len(name) >5]

# print(newNames)

# ii)
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’] 
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink']

filteredList = [colors[i] for i in range(len(colors)) if i not in [0,4,5] ]

# print(filteredList)