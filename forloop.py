# my_list = [10, 20, 30, 40]

# for el in my_list:
#     print(el)
# else:
#     print("done")
#     print("Last element was:", el)


####Print the elements of the following list using a loop:
# list = []
# for el in range(1, 11):
#     list.append(el**2)
# print(list)


##Search for a number x in this tuple using loop:

mytuple= (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
x= int(input("Enter a number to search: "))
for el in mytuple:
    if el == x:
        print("Found")
        break