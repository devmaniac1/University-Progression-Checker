Progress = "Progress"
ModuleTrailer = "Progress (Module Trailer)"
DonotProgress = "Do not Progress - Module Retriever"
Exclude = "Exclude"

def compute_grade(Pass,Defer,Fail):
    if Pass == 120:
        return Progress
    elif Pass == 100:
        return ModuleTrailer
    elif Pass <= 80 and Fail < 80:
        return DonotProgress
    elif Fail <=120:
        return Exclude
