jug1=int(input("enter capacity of 1st Jug\n"))
jug2=int(input("enter Capacity of 2nd Jug\n"))
t1=int(input("enter goal state of first Jug\n"))
t2=int(input("enter goal state of second Jug\n"))

def water_jug(cap1,cap2):
    print("\n",cap1,cap2)
    
    if (cap1==t1 and cap2==t2) or (cap1==t2 and cap2==t1):
        return 
    
    elif cap2==jug2:
        water_jug(cap1,0)
    elif cap1!=0:
        if cap1 <= jug2-cap2:
            water_jug(0,cap1+cap2)
        elif cap1 > jug2-cap2:
            water_jug(cap1-(jug2-cap2), cap2+(jug2-cap2))
    else:
        water_jug(jug1,cap2)

water_jug(0,0)
      



