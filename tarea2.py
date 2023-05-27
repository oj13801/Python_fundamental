#Tarea #2 
# in  python create an app that print all prime numbers from 1 to 100 
for i in range (0,100):
    if i > 2:  #start at #3 since number 2 is a special number 
        for x in range(2,i) :       
            if (i % x) == 0:
                break
        else:    
            print(i)

