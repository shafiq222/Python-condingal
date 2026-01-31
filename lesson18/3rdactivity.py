def hotel_cost(days):
    return 140*days
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "tampa"== city:
        return 220
    elif "pittsburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475
def rental_car_cost(days):

    if days>=7 :

        return 40*days - 50

    elif days>=3 :

        return 40*days - 20

    else:

        return 40*days

def trip_cost(city, days, spending_money):

    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print(trip_cost("Tampa",6,500))