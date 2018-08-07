'''define function(2 arguments)'''
def s(bottom, high):
#     you can docstring in here
    area = bottom * high / 2
#     return [expression list]
    return area      

'''map(function, iterable): apply a function to a list and get a new list.'''
eur_jpy = 122.75
def jpy_to_eur(jpy):
    print(jpy // eur_jpy)
                
jpy_list = [10000, 30000, 50000, 70000]

for eur in map(jpy_to_eur, jpy_list):        
    print(eur)         
     
                
'''filter function'''
# get prime number from a list
def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num_list = range(2, 100)

'''
# normal solution                
prime_list = []                                 
for n in num_list:
    if prime_number(n) == True:
        prime_list.append(n)
    
print(prime_list) 
'''

                
# filter function, included in for loop.                      
for p in filter(prime_number, num_list):
    print(p)              


