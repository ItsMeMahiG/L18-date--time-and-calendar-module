def hotelcost(days) :
    return 140*days

def planeridecost(city) :
    if "boston"==city :
        return 400
    elif "pittsburgh"==city :
        return 250
    elif "orlando" ==city :
        return 500

def rentcarcost(days) :
    if days>=7 :
        return 150*days
    elif days>=3 :
        return 100*days
    else :
        return 70*days
    
def tripcost(city, days, moneyspent) :
    return rentcarcost(days)+hotelcost(days)+planeridecost(city)+moneyspent

print(tripcost("boston",61,700))