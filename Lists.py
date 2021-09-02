#lists
lucky_numbers = [4,8,15] #create list named lucky_numbers
friends = ["john", "jake", "jim"]
friends.extend(lucky_numbers) 
friends.append("creed")
friends.insert(1, "kelley")
#friends.clear()
friends.pop()
#friends.sort()
print(friends.index("john"))
friends2 = friends.copy()
print(friends + friends2)
