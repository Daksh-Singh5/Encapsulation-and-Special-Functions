class Computer:
    def __init__(self,Company,Maxprice,):
        self.Company = Company
        self.__Maxprice = Maxprice
        
    def getChangePrice(self,price):
        self.__Maxprice = price
    def getPrice(self):
        print(self.__Maxprice)

Daksh = Computer("Dell",10000)

print(Daksh.Company)
Daksh.getPrice()
Daksh.getChangePrice(1202412)
Daksh.getPrice()




