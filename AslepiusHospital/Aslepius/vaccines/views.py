from django.shortcuts import render

def vaccines(request):
    return render(request,'vaccines/Vaccines.html')

def birth(request):
    return render(request, 'vaccines/Birth.html')

def two_Months(request):
    return render(request,'vaccines/2Months.html')

def four_Months(request):
    return render(request,'vaccines/4Months.html')

def six_Months(request):
    return render(request,'vaccines/6Months.html')

def nine_twelve_Months(request):
    return render(request,'vaccines/9-12Months.html')

def fifteen_eighteen_Months(request):
    return render(request,'vaccines/15-18Months.html')

def two_three_Years(request):
    return render(request,'vaccines/2-3Years.html')

def five_Years(request):
    return render(request,'vaccines/5Years.html')

def seven_seventeen_Years(request):
    return render(request,'vaccines/7-17Years.html')

def ThankYou(request):
    return render(request,'vaccines/ThankYou.html')

# def CSV_read():
#     import pandas as pd
#     df = pd.read_csv("Vaccine_Table.csv")


