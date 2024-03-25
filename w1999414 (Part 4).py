import os
import validation as valid
import Grading as grade

Part2_List = []
Dictionary = {}
#-------------------Check if Text file Available in directory-------------------------------
#-------------------If Available remove text file-------------------------------------------

if os.path.exists('Text.txt'):
    os.remove('Text.txt')
    
#-------------------Main Enclosing Function-------------------------------------------------

def main():

    print("____________________________________________________\n")

    def getUow():
        UoW_Number = input("Please Enter your UoW student ID: ")
        Valid_UoW = valid.validateUow(UoW_Number)
        if Valid_UoW:
            return UoW_Number
        else:
            return False

    UoW = getUow()

    while UoW == False:
        UoW = getUow()

#-------------------Function to get Pass Credit---------------------------------------------
        
    def getPass():
        Pass = input("\nPlease Enter your credits at Pass:  ")
        Valid_Pass = valid.validate(Pass)
        if Valid_Pass == True:
            Pass=int(Pass)
            return Pass
        elif Valid_Pass == False:
            return 1

    Pass = getPass()
            
    while Pass == 1:
        Pass = getPass()

#-------------------Function to get Defer Credit--------------------------------------------
    
    def getDefer():
        Defer = input("Please Enter your credits at Defer: ")
        Valid_Defer = valid.validate(Defer)
        if Valid_Defer == True:
            Defer=int(Defer)
            return Defer
        elif Valid_Defer == False:
            return 1

    Defer = getDefer()
            
    while Defer == 1:
        Defer = getDefer()

#-------------------Function to get Fail Credit---------------------------------------------
        
    def getFail():
        Fail = input("Please Enter your credits at Fail:  ")
        Valid_Fail = valid.validate(Fail)
        if Valid_Fail == True:
            Fail=int(Fail)
            return Fail
        elif Valid_Fail == False:
            return 1

    Fail = getFail()
            
    while Fail == 1:
        Fail = getFail()

#-------------------Get Total of the input credits------------------------------------------
    
    Total = int(Pass) + int(Defer) + int(Fail)

    if Total == 120:
        Grade = grade.compute_grade(Pass,Defer,Fail)
        print(Grade)

#-------------------Part 4 Create Dictionary------------------------------------------------
        List = []
        List = [Grade,Pass,Defer,Fail]
        def createDictionary(UoW,List):
            Dictionary[UoW]=List
            return Dictionary
        Dict = createDictionary(UoW,List)
        
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
            print_dict = {}

            for key, value in Dict.items():
                print_dict[key] = (f'{value[0]} - {value[1]},{value[2]},{value[3]}')
            print(print_dict)
            pass
        
    else:
        print("Total Cannot be above or below 120")
        print("____________________________________________________\n")
        main()

#-------------------Calls the main function to initiate the program-------------------------
        
main()
