#make a function that takes in a list of numbers that adds up all values.
# numberlist = [70, 69, 7, 41, 89, 56, 56, 56, 95, 5, 80, 81, 3, 91, 31, 35, 82, 28, 15, 23, 6, 61, 40, 69, 26, 40, 25, 45, 67]

# def number(listnumber):
#     sum=0
#     for x in listnumber:
#         if x%2==0:
#             sum+=x
#     return sum

# print(number(numberlist))



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# nums = [2,7,11,15] 
# target = 9


# def integers(list, target):
#     for x in range(len(list)):
#         for y in range(len(list)):
#             if x==y:
#                 continue
#             if list[x] + list[y]==target:
#                 return [x,y]
# print(integers(nums , target))

bomb=0
explode = 0
print("Defuse the bomb!")
wire_cut=input("There are 3 wires in front of you, a blue wire, a red wire, and a green wire, which one will you cut? ")
if wire_cut.lower == "green":
    bomb+=1
elif wire_cut.lower == "blue":
    bomb+=1
elif wire_cut.lower =="red":
    bomb=0
else:
    print("sorry that isn't one of the wires. RUN!")
    bomb+=1
if bomb>0:
    explode+= 1
    print("BOOM!")
else:
    print("Good job your bomb didn't explode!")
