import os
import validation as v
import Grading as g
import Histogram as hist


Part2_List = []

#-------------------Check if Text file Available in directory-------------------------------
#-------------------If Available remove text file-------------------------------------------

if os.path.exists('Text.txt'):
    os.remove('Text.txt')
    
#-------------------Main Enclosing Function-------------------------------------------------

def main():

#-------------------Function to get Pass Credit---------------------------------------------
        
    def get_pass():
        Pass = input("\nPlease Enter your credits at Pass:  ")
        Valid_Pass = v.validate(Pass)
        if Valid_Pass == True:
            Pass=int(Pass)
            return Pass
        elif Valid_Pass == False:
            return 1

    Pass = get_pass()
            
    while Pass == 1:
        Pass = get_pass()

#-------------------Function to get Defer Credit--------------------------------------------
    
    def get_defer():
        Defer = input("Please Enter your credits at Defer: ")
        Valid_Defer = v.validate(Defer)
        if Valid_Defer == True:
            Defer=int(Defer)
            return Defer
        elif Valid_Defer == False:
            return 1

    Defer = get_defer()
            
    while Defer == 1:
        Defer = get_defer()

#-------------------Function to get Fail Credit---------------------------------------------
        
    def get_fail():
        Fail = input("Please Enter your credits at Fail:  ")
        Valid_Fail = v.validate(Fail)
        if Valid_Fail == True:
            Fail=int(Fail)
            return Fail
        elif Valid_Fail == False:
            return 1

    Fail = get_fail()
            
    while Fail == 1:
        Fail = get_fail()

#-------------------Get Total of the input credits------------------------------------------
    
    Total = int(Pass) + int(Defer) + int(Fail)

    if Total == 120:
        Grade = g.compute_grade(Pass,Defer,Fail)
        print(Grade)
        Data_for_Histogram = hist.data_set(Grade)

#-------------------Write Data to Text File-------------------------------------------------
        
        with open('Text.txt','a') as T:
            T.write(f'{Grade} - {Pass},{Defer},{Fail}\n')

#-------------------Part 2 List Extension---------------------------------------------------

        List = []
        List = [Grade,Pass,Defer,Fail]
        Part2_List.append(List)
        
#-------------------Prompt to Run Again or Quit Program-------------------------------------
#-------------------If User Quits the program prints out the Histogram----------------------
#-------------------Additionally Prints List & Dictionary-----------------------------------
        
        print("____________________________________________________\n",
              "Would you like to enter another set of data?")
        
        Run_Again = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
        
        Options = ['y','q']
        
        while Run_Again not in Options:
            print("Invalid Input")
            Run_Again = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()

        if Run_Again == 'y':
            main()
            
        else:
            Histogram = hist.Outline(Data_for_Histogram)
            print("****************************************************")
            print("Part 2 List\n") 
            for i in Part2_List:
                print(i[0],' - ',i[1],i[2],i[3])
            print("****************************************************")
            pass
        
    else:
        print("Total Cannot be above or below 120")
        print("____________________________________________________\n")
        main()

#-------------------Calls the main function to initiate the program-------------------------
        
main()
