#Set - Are immutable, but they don't allow duplicate, Unorder

# african_countries = {"Algeria", "Gambia"}  # Create a set
# european_countries = {"Uk", "Estonia", "France", "Turkey", "Spain"}
# africa_countries.update(new_african_countries)
# euro_country = "Portugal"
# european_countries.add(euro_country)  # Use to add a new item
# countries = africa_countries.union(european_countries)
# # print(countries)
# print(africa_countries)
# print(european_countries)
# africa_countries = set(("Nigeria", "Ghana", "Togo"))  #Create a set


#True = 1 and False = 0
# thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False}
# print("apple" not in thisset)
# print(len(thisset))
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
#
# thisset.update(mylist)
# mylist.extend(thisset)
#
# print(thisset)
# print(mylist)


# thisset = {"apple", "banana", "cherry"}
#
# # thisset.remove("banana")
# # thisset.discard("banana")
# thisset.pop()
# print(thisset)

#Union
set1 = {1, 2, 3}
set2 = {4, 2, 5}

set3 = set1.union(set2) #It like addition of two set
set4 = set1.difference(set2) # It return what is in the first set and not in the second set
set5 = set1.intersection(set2) #retun what is common to the two sets
print(set4)
print(set3)
print(set5)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)