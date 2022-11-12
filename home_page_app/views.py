from django.shortcuts import render
 
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


    result = BinarySearch(numberList, int(searchValue))
    # print(result)
    return render(request, 'home.html', context={'result':result})


  return render(request, 'home.html', context={'result':None})
