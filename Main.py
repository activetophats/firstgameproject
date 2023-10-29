import Person
import Regions
import Food
person1 = Person.Person(30)
day = 1
hours = 0 #24 hour based clock
date = {
    0:"Monday",
    1:"Tuesdays",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
}

alive  = True
#day counter 
while alive:
    day = day%6
    print(f"Today is {date[day]}")
    
    #hour counter
    while hours <24:
        user_inp = input(f"""It is currently hour: {hours}
Please pick an action 
1) run,hour
2) sleep,hour
3) eat,food
4) stats
""")
        action,time = user_inp.split(",")
        time = int(time)
        if action == "run":
            alive = person1.run(time)
            
        if action == "sleep":
            person1.sleep(time)
        
        hours +=int(time)
    hours -=24
    day +=1
print("sadly you died")