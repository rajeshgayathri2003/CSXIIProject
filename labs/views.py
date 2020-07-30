from django.shortcuts import render
from .models import Labs
# Create your views here.

def tests(request):
    obj1 = Labs.objects.get(testID=1)
    obj2 = Labs.objects.get(testID=2)
    obj3 = Labs.objects.get(testID=3)
    obj4 = Labs.objects.get(testID=4)
    obj5 = Labs.objects.get(testID=5)
    obj6 = Labs.objects.get(testID=6)
    obj7 = Labs.objects.get(testID=7)
    obj8 = Labs.objects.get(testID=8)
    obj9 = Labs.objects.get(testID=9)
    obj10 = Labs.objects.get(testID=10)
    obj11 = Labs.objects.get(testID=11)
    obj12 = Labs.objects.get(testID=12)
    obj13 = Labs.objects.get(testID=13)
    obj14 = Labs.objects.get(testID=14)
    obj15 = Labs.objects.get(testID=15)
    obj16 = Labs.objects.get(testID=16)
    obj17 = Labs.objects.get(testID=17)
    obj18 = Labs.objects.get(testID=18)
    obj19 = Labs.objects.get(testID=19)
    obj20 = Labs.objects.get(testID=20)
    obj21 = Labs.objects.get(testID=21)
    obj22 = Labs.objects.get(testID=22)
    obj23 = Labs.objects.get(testID=23)
    obj24 = Labs.objects.get(testID=24)
    obj25 = Labs.objects.get(testID=25)
    context = {
        'object1': obj1,
        'object2': obj2,
        'object3': obj3,
        'object4': obj4,
        'object5': obj5,
        'object6': obj6,
        'object7': obj7,
        'object8': obj8,
        'object9': obj9,
        'object10': obj10,
        'object11': obj11,
        'object12': obj12,
        'object13': obj13,
        'object14': obj14,
        'object15': obj15,
        'object16': obj16,
        'object17': obj17,
        'object18': obj18,
        'object19': obj19,
        'object20': obj20,
        'object21': obj21,
        'object22': obj22,
        'object23': obj23,
        'object24': obj24,
        'object25': obj25
    }
    return render(request,'labs/labs1.html', context)


