x = 10

if x > 0:
    print("pippo")
  
# IF  a catena
if ( x > 10 ):
    print("sei sopra 10")
elif( x > 1):
    print("sei sopra 1")
elif(x >0):
    print("sei un numero negativo")
else:
    print("sei 0")


# IF  annidato
if (x > 0):
    if (x < 10):
        print("sei sopra 0 ma sotto 10")
        
        if(x>20):
            print("superiore a 20") 
        else: 
            print("non è maggiore di 20")
            
    else:
        print("sei sopra 10")
else:
    print("sei un numero negativo")
  
   
# IF  con condizioni multiple
if x > 0 and x < 10 or x > 50:
    print("sei sopra 0 ma sotto 10") 
    
y = ""  
y = input("iserisci un nome")

# IF su stringhe
if ( y == "Mirko" ):
       print("sei " + y) 
else:
    print("hai sbagliato l'iserimento")
    
lista = [1,2,3,4,5]

# IF su aggregazioni
if 5 in lista:
    print("il 5 eè nella lista")
else:
    print("non è nella lista")  
