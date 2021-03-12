#Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
#     }



def print_info(dojo):
    # print (list(dojo.keys())[0])
    # print (dojo['locations'][0])
    # print (len(list(dojo.keys())[0]))
    # print (len(dojo['locations']))
    
    for i in range (0, len(dojo), 1):
        print  (len(dojo[list(dojo.keys())[i]]), list(dojo.keys())[i].upper())
        for j in range (0, len(dojo[list(dojo.keys())[i]]),1):
            print  (dojo [list(dojo.keys())[i]][j])

            


print_info({
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    })   