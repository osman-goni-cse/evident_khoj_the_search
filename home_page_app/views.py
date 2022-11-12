import json
from django.shortcuts import render
from home_page_app.models import StoreNumber
from home_page_app.serializers import StoreNumberSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
from django.contrib.auth.models import User

def BinarySearch(numberList, target):  
  low = 0  
  high = len(numberList) - 1  
  mid = 0  

  while low <= high:  
    # for get integer result   
    mid = (high + low) // 2  

    print(numberList[mid], target)
    # Check if n is present at mid   
    if numberList[mid] < target:  
      high = mid - 1  

    # If n is greater, compare to the right of mid   
    elif numberList[mid] > target:  
      low = mid + 1  

    # If n is smaller, compared to the left of mid  
    else:  
      return mid  

      # element was not present in the list, return -1  
  return -1  
  

def home_page_view(request):
  if request.method == "POST":
   
    numberList = request.POST.get('numberList') 
    searchValue = request.POST.get('search_value')

    numberList = list(numberList.split(','))
    numberList = [int(i) for i in numberList]
    numberList = sorted(numberList, reverse=True) 

    StoreNumber.objects.create(
      user=request.user,
      numberList=json.dumps(numberList)
    )

    result = BinarySearch(numberList, int(searchValue))


    # print(result)
    return render(request, 'home.html', context={'result':result})


  return render(request, 'home.html', context={'result':None})


@api_view(['GET'])
def getRoutes(request):
  routes = [  
    {  
    'Endpoint': '/notes/',  
    'method': 'GET',  
    'body': None,  
    'description': 'Returns an array of notes'  
    },
  ]
  return Response(routes)


@api_view(['GET'])
def notesList(request, user_id):
  print(start_datetime)
  user = User.objects.get(id=user_id)
  numberList = StoreNumber.objects.filter(
    user=user,
    timestamp__gte=datetime.datetime(start_datetime),
    timestamp__lte=datetime.datetime(end_datetime)

  )

  serializer = StoreNumberSerializer(numberList, many=True)
  return Response(serializer.data) 