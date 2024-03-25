Progress = 0
ModuleTrailer = 0
ModuleRetriever = 0
Exclude = 0

def Outline(data):
        
    print("\n\n----------------------------------------------------")
    print("Histogram\n")
    print(f"Progress  {data[0]} : {'*' * data[0]}")
    print(f"Trailer   {data[1]} : {'*' * data[1]}")
    print(f"Retriever {data[2]} : {'*' * data[2]}")
    print(f"Excluded  {data[3]} : {'*' * data[3]}\n")
    print(f"{data[0]+data[1]+data[2]+data[3]} outcomes in total.")
    print("----------------------------------------------------\n")

def data_set(G):
    if G == "Progress":
        global Progress
        Progress += 1
        
    elif G == "Progress (Module Trailer)":
        global ModuleTrailer
        ModuleTrailer += 1
        
    elif G == "Do not Progress - Module Retriever":
        global ModuleRetriever
        ModuleRetriever += 1
        
    else:
        global Exclude
        Exclude += 1

    return Progress,ModuleTrailer,ModuleRetriever,Exclude
