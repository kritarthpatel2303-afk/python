hour =0
while hour<24:
    if hour ==0:
        print("12 midnight")
    elif hour== 12:
        print("12 noon")
    elif hour <12:
        print(hour, "AM")
    else:
        print(hour -12, "PM")
    hour+=1
    
