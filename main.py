# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 18:34:20 2023

@author: Hannah
"""

from ArrayDeque import ArrayDequeMaxlen

     
        
AQM = ArrayDequeMaxlen(20)


print('Adding last')
for i in range(100):
    AQM.add_last(i)
    print (i, AQM._data)
    
print('\nDelete 80', AQM.remove(80), AQM._data, AQM.first())
    


    
print ('\nAdding first')
for i in range(20, 10, -1):
    AQM.add_first(i)
    print (i, AQM._data)
    
    
print(AQM.first())
    

    
print('\nPerforming the removals')
while not AQM.is_empty():
    print ('Remove first', AQM.first(), AQM.delete_first(), 'Remove '
                                                       'last',
           AQM.last(),  AQM.delete_last())

print(AQM.length())