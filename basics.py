import time
import datetime
from datetime import date
from datetime import timedelta

#basics
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

jamamseconds = 8640 

birds = ["Vulture","Owl","Crow","Hen","Peacock"]

pirai = ["Valar","Thei"]

valarpatactivity = {"Rule":2880, "Eat":1800, "Walk":2160, "Sleep":1080, "Death":720}

theimornpatactivity = {"Rule":1080, "Eat":2880, "Walk":2160, "Sleep":720, "Death":1800}

theinightpatactivity = {"Rule":1080, "Eat":2520, "Walk":2520, "Sleep":1080, "Death":1440}

valarmornorder = ["Eat","Walk","Rule","Sleep","Death"]
valarnightorder = ["Eat","Rule","Death","Walk","Sleep"]

theimornorder = ["Eat","Death","Sleep","Rule","Walk"]
theinightorder = ["Eat","Sleep","Walk","Death","Rule"]

valarmornbirds = {"Monday":"Owl","Tuesday":"Vulture","Wednesday":"Owl","Thursday":"Crow","Friday":"Hen","Saturday":"Peacock","Sunday":"Vulture"}
 
valarnightbirds = {"Monday":"Hen","Tuesday":"Crow","Wednesday":"Hen","Thursday":"Peacock","Friday":"Vulture","Saturday":"Owl","Sunday":"Crow"}

theimornbirds = {"Monday":"Peacock","Tuesday":"Hen","Wednesday":"Crow","Thursday":"Owl","Friday":"Vulture","Saturday":"Peacock","Sunday":"Hen"} 

theinightbirds = {"Monday":"Hen","Tuesday":"Vulture","Wednesday":"Owl","Thursday":"Crow","Friday":"Peacock","Saturday":"Hen","Sunday":"Vulture"}


#inputs

bornyear = 1998
bornmonth = 7
borndate = 29
bornhour = 5
bornmin = 21
sunrisehour = 5
sunrisemin = 56
bornpirai = "Valar"
#"Generally it'll be the same date but for cases born before Sun rise we need to consider the previous date"
# sundate = borndate
sundate = 28

#logic implementation

borndatetime = datetime.datetime(bornyear, bornmonth, borndate, bornhour, bornmin, 00)

bornsunrise = datetime.datetime(bornyear, bornmonth, sundate, sunrisehour, sunrisemin, 00)

bornday = days[date.weekday(bornsunrise)]

print("Date and time when you were born : ",borndatetime)
print("Day in which you were born : ",bornday)
print("Sunrise on the Day of birth : " ,bornsunrise)

timediff = borndatetime-bornsunrise

jamamcount = 1

calcdiff = timediff

print("Difference in seconds ",timediff.seconds)

# Calculating the Exact Jamam occuring during your Birth
for i in range(1,10):
  if (calcdiff.seconds > 8640):
    calcdiffsecs = calcdiff.seconds - 8640
    calcdiff = timedelta(seconds=calcdiffsecs)
    jamamcount = i + 1
print("Jamam in which you were Born ",jamamcount)



if (pirai[0]==bornpirai):
  print("Born in Valar Pirai (Sukla Paksha) ")

  if(jamamcount>5):
    orderrule = valarnightorder
    jamamexact = jamamcount - 5
    birdrule = valarnightbirds
  else:
    orderrule = valarmornorder
    jamamexact = jamamcount
    birdrule = valarmornbirds

 
  athihara_bird_activity = orderrule[jamamexact-1]
  print("Athihara patchi is in activity : ",athihara_bird_activity)
  orderrule_numb = jamamexact-1
  
  #Now we need to subract the time ( in seconds ) for the previous Jamams so that we could split the existing Jamam according to activities of birds based on Athihara Patchi

  remainingsecs = timediff.seconds - ((jamamcount-1) * 8640)
  
  # print(remainingsecs)
  # print(valarpatactivity[athihara_bird_activity])
  
  sum_bird_activity = valarpatactivity[athihara_bird_activity] 
  
  skip = 0
  
  for i in range(1,5):
    if(remainingsecs>sum_bird_activity):
      skip = skip + 1
      if(orderrule_numb>=4):
        orderrule_numb = 0
      else:
        orderrule_numb = orderrule_numb + 1
      sum_bird_activity = sum_bird_activity + valarpatactivity[orderrule[orderrule_numb]]
      # print(sum_bird_activity)
  
  your_bird_activity = orderrule[orderrule_numb]    
  print("Your Destined Patchi is in Activity : ",your_bird_activity)
  
  # print("Skip ",skip)
  
  athihara_bird = birdrule[bornday]
  print("Athihara Patchi of that day : ",athihara_bird)

  #Loop for skiping and counting the exact Bird
  for idx, val in enumerate(birds):
    if val==athihara_bird:
      newidx = idx+skip
    #   print(newidx)
    # print(idx, val)
  
  # print("Length of Birds ",len(birds))
  
  if newidx>=len(birds):
    newidx = newidx - len(birds) 
  
  your_bird = birds[newidx]
  print("---------------------------------")
  print("Your Destined Bird is :",your_bird)
  print("---------------------------------")  

      
  
else:
  print("Born in Thei Pirai (Krishna Paksha) ")