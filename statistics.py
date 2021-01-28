
import math

def calculateStats(numbers):
  l=len(numbers)
  res={"avg":0,"max":0,"min":0}
  if l!=0:
    res["avg"]=(sum(numbers)/l)
    res["max"]=max(numbers)
    res["min"]=min(numbers)
  else:
    res["avg"]=res["max"]=res["min"]=math.nan
  return res
