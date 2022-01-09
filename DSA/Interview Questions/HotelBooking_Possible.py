import types


def HotelBooking(arrival, depart, K):

    event = []
    
    # for i in range(0, len(arrival)):
    #     T_arrival = ()
    #     T_arrival  = T_arrival + (arrival[i], "RED")
    #     event.append(T_arrival)

    # for i in range(0, len(depart)):
    #     T_depart = ()
    #     T_depart  = T_depart + (depart[i], "BLUE")
  
    #     event.append(T_depart)   

# OR 

    event = [(t,"RED") for t in arrival] + [(t,"BLUE") for t in depart]

    event = sorted(event)
    print(event)

    guest = 0
    for e  in event:
        if(e[1] == "RED"):
            guest = guest+1
        else:
            guest = guest-1

        if(guest > K):
            return 0
    return 1  


arrival = [1,3,5]
depart = [2,6,8]

print(HotelBooking(arrival,depart,1))