'''
 #Take 5 user input and store them in a list.
 #Remove duplicates
 #add element
 #remove element
'''
print('\n ' + '='*50)
print('\n Task 1: A mini shopping list')
print('\n' + '='*50)

shopping_list = [] #an empty list

#allow user to input 5 items
shopping_list = input('Enter 5 items for your shopping list, separated by commas: ').split(',')
print(f'Shopping list: {shopping_list}') #print the list
print()

#remove duplicates by creating a dictionary from the list and back to a list
shopping_list = list(dict.fromkeys(shopping_list))
print(f'Shopping list after removing duplicates: {shopping_list}')
print()

#add element
element = input('Enter items:').split(',')
shopping_list.extend(element)
print(f'New shopping list after adding items: {shopping_list}')
print()

#remove element
element = input('Enter items to remove:').split(',')
for item in element: #loops through each item in the element list
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f'{item} not found in the shopping list.')
print(f'New shopping list after removing items: {shopping_list}')
print()
print(f"That's my shopping list!!!")



'''
 #create a number list 
 #find the minimum and maximum numbers on the list
 #sort the list
 #print the final unique sorted list
'''
print()
print()
print('\n' + '='*50)
print('\n Task 2: Student mark sheet')
print('\n' + '='*50)

#create a number list
student_marks = []
for i in range (10):
    marks = int(input('Enter student mark:'))
    student_marks.append(marks)
print()
print(f'Student marks: {student_marks}')

#find the minimum ,maximum and average numbers on the list
min_marks = min(student_marks)
max_marks = max(student_marks)
average_marks = sum(student_marks) / len(student_marks)
print(f'Minimum marks: {min_marks}')
print(f'Maximum marks: {max_marks}')
print(f'Average marks: {average_marks}')


#sort the list
student_marks.sort()
print(f'Sorted student marks: {student_marks}')
print()
print(f'Student mark sheet: {student_marks}')


