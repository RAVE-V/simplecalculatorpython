#introduction
print("********************************************************************************")
print("                          PYTHON CALCULATOR                                      ")
print("                                                                            " )         
print("********************************************************************************")
true = 1
while true :
    print ("\n \n OPTIONS :\n")
    print("Type   ' + '      to  ADD ")
    print("Type   ' - '      to  SUBTRACT " )
    print("Type   ' * '      to  MULTIPLY")
    print("Type   ' / '      to  DIVIDE")
    print ("Type   ' quit '   to  QUIT\n")
    user_input = input(":" )
        
# waits for user to input  'quit' ,  +   ,  - ,  /  ,  * 
    if user_input =="quit":
        break
    #above says it to quit
    elif user_input =="+":
        x = float(input("\n \nEnter a Number  :  "))
        y = float (input("Enter another Number :  "))
        a=str(x)
        b=str(y)
        result_a=str(x+y)
        print(a +" + "+ b + " = "+ result_a)
        #addition takes place
    elif user_input =="-":
            x = float(input("\n\nEnter a Number  :  "))
            y = float (input("Enter another Number :  "))
            a=str(x)
            b=str(y)
            result_s=str(x-y)
            print(a +" - " +b +" = " +result_s)
            #subtraction takes place
    elif user_input=="*":
          x = float(input("\n\nEnter a Number  :  "))
          y = float (input("Enter another Number :  "))
          a=str(x)
          b=str(y)
          result_m=str(x*y)
          print(a+" * " +b+" = " +result_m)
          #multiplication takes place
    elif user_input=="/":
          x = float(input("Enter a Number to be divided :  "))
          z=str(x)
          y = float(input("Enter Number to divide  " +z + " with : "))
          result_d=str(x/y)
          #division takes place
          modulo_remain=str(x%y)#the modulo(gives remainder)
          floor_quotient=str(x//y)#the floor (gives the exponent)
          a=str(x)
          b=str(y)
          print(a+" / " +b+ " = " +result_d)
          print("The Quotient Is "+ floor_quotient)
          print("The Remainder Is  "+modulo_remain)
          
          
         
          
          
         
        
       
