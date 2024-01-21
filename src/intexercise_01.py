#intermediate python excercisem #1
# Manny Campbell, Natalie Tepedino, Nathan Gray, Philip Vishnevsky

#take input to determine the size of the list
list_size = int(input("Please determine the size of your list: "))
# make empty list 
initial_list=[]

#create a for loop to iterate over the list
for i in range(0, list_size):
    #appending every value to intial list
    user_input = int(input("Please enter an integer: "))
    initial_list.append(user_input)
print("Initial List:" + str(initial_list))

#creating a new function to be called
def get_non_repeat_list(initial_list):
    #empty list to appened all unique values
    non_repeat_list = []
    #iterting through the initial list using set to eliminate duplicates
    #return list in sorted order
    for val in sorted(set(initial_list)):
        #appending all unique values to the non repeating list
        non_repeat_list.append(val)
    return non_repeat_list

#code to call the function
non_repeat_list = get_non_repeat_list(initial_list)
print("Non-repeating List: " + str(non_repeat_list))

#referenced the official python docs provided to us
# https://docs.python.org/3/tutorial/datastructures.html#looping-techniques