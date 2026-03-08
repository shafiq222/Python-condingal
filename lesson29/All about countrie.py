class Algeria():
    def capital(self):
        print("Algiers is the capital of Algeria")
    def laguage(self):
        print("Arabic and Tamazight are the language used in Algria")
    def type(self):
        print("Algeria is a semi-presidential republic country")
    
class Nigeria():
    def capital(self):
        print("Abuja is the capital of Nigeria")
    def laguage(self):
        print("English is the official language used in Nigeria . Nigeria is exceptionally linguistically diverse, with over 500 indigenous languages spoken across the country")
    def type(self):
        print("Nigeria is a federal presidential republic")

obj_ind = Algeria()
obj_usa = Nigeria()
for country in (obj_ind,obj_usa):

    country.capital()
    country.laguage()
    country.type()