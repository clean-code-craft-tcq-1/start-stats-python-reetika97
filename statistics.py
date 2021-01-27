
def calculateStats(numbers):
  l=len(numbers)
  res={"avg":0,"max":0,"min":0};
  if l!=0:
    sum=0; max=numbers[0]; min=numbers[0];
    for i in range(0,l):
      sum+=numbers[i];
      if numbers[i]<min:
        min=numbers[i];
      if numbers[i]>max:
        max=numbers[i];
    avg1=sum/l;
    res["avg"]=avg1
    res["max"]=max
    res["max"]=min
  
  
  #use dictionary for returning the function ; avg, min and max? 
  #define email and led alert functions with only print statements
  return res
