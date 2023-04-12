from abc import ABC, abstractmethod
from operator import index  

class Tour(ABC):
    @abstractmethod
    def create(self, cost, list, list_costs, list_tours):
        pass

class Turkey(Tour):
    name = "Turkey"
    def create(self, cost, list, list_costs, list_tours):
        print("The tour is created to : " + self.name)
        list.append(self.name + " " + str(cost))
        list_costs.append(int(cost))
        list_tours.append(self.name)


class Egypt(Tour):
    name = "Egypt"
    def create(self, cost, list, list_costs, list_tours):
        print("The tour is created to : " + self.name)
        list.append(self.name + " " + str(cost))
        list_costs.append(int(cost))
        list_tours.append(self.name)

class Vietnam(Tour):
    name = "Vietnam"
    def create(self, cost, list, list_costs, list_tours):
        print("The tour is created to : " + self.name)
        list.append(self.name + " " + str(cost))
        list_costs.append(int(cost))
        list_tours.append(self.name)

class Dubai(Tour):
    name = "Dubai"
    def create(self, cost, list, list_costs, list_tours):
        print("The tour is created to : " + self.name)
        list.append(self.name + " " + str(cost))
        list_costs.append(int(cost))
        list_tours.append(self.name)

class Agency(ABC):
    @abstractmethod
    def createTour(country):
        pass
    @abstractmethod
    def sellTour(list):
        pass
    @abstractmethod
    def buyTour(list1, list2, index):
        pass
    @abstractmethod
    def showTour(list):
        pass

class Agency1(Agency):
    def createTour(country):
        if country == "Turkey":
            return Turkey()
        if country == "Egypt":
            return Egypt()
        if country == "Vietnam":
            return Vietnam()
        if country == "Dubai":
            return Dubai()
    def showTour(list):
        for i,val in enumerate(list):
            print(i+1, val)
    def sellTour(list, index):
        list.pop(index)
    def buyTour(list1, list2, index):
        list1.append(list2[index])
        list2.pop(index)
             

class Agency2(Agency):
    def createTour(country):
        if country == "Turkey":
            return Turkey()
        if country == "Egypt":
            return Egypt()
        if country == "Vietnam":
            return Vietnam()
        if country == "Dubai":
            return Dubai()
    def showTour(list):
        for i,val in enumerate(list):
            print(i+1, val)
    def sellTour(list, index):
        list.pop(index)
    def buyTour(list1, list2, index):
        list2.append(list1[index])
        list1.pop(index)

class User:
    def getAgency(self, type_of_agency):
        if type_of_agency == "Agency1":
            return Agency1
        if type_of_agency == "Agency2":
            return Agency2
    def buyAgency1(self, list1, listUser, index):
        listUser.append(list1[index])
        list1.pop(index)
    def buyAgency2(self, list2, listUser, index):
        listUser.append(list2[index])
        list2.pop(index)
    def showUserTour(self, list):
        for i,val in enumerate(list):
            print(i+1, val)

user = User()
agency1 = user.getAgency("Agency1")
agency2 = user.getAgency("Agency2")
listUser = []
list1 = []
list2 = []
list1_costs = []
list2_costs = []
listUser_costs = []
list1_tours = []
list2_tours = []
optionUser = int(input("1 - Log in like User \n" 
                       + "2 - Log in like Agency1 \n"
                       + "3 - Log in like Agency2 \n"))
if optionUser == 1:
        tour = agency1.createTour("Turkey")
        tour.create(40, list1, list1_costs, list1_tours)
        tour = agency1.createTour("Dubai")
        tour.create(100, list1, list1_costs, list1_tours)
        tour = agency2.createTour("Vietnam")
        tour.create(55, list2, list2_costs, list2_tours)
        print("Enter your sum of money: ")
        sum = int(input())
        while(True):
           option1 = int(input("1 - show tours \n"
                       + "2 - buy tour from Agency1 \n"
                       + "3 - buy tour from Agency2 \n"
                       + "4 - show your tours \n"))
           if option1 == 1:
              print("Agency1: ")
              agency1.showTour(list1)
              print("Agency2: ")
              agency2.showTour(list2)
           if option1 == 2:
              agency1.showTour(list1)
              print("Enter index of tour from Agency1: ")
              index1_2 = int(input()) - 1
              sum -= list1_costs[index1_2]
              user.buyAgency1(list1, listUser, index1_2)
              if sum >= 0:
                  print("Remains - " + str(sum))
              if sum < 0:
                  print("Not enough money")
           if option1 == 3:
              agency2.showTour(list2)
              print("Enter index of tour from Agency2: ")
              index1_3 = int(input()) - 1
              sum -= list2_costs[index1_3]
              user.buyAgency2(list2, listUser, index1_3)
              if sum >= 0:
                  print("Remains - " + str(sum))
              if sum < 0:
                  print("Not enough money")
                  exit()
           if option1 == 4:
               user.showUserTour(listUser)
if optionUser == 2:
        print("Enter your sum of money: ")
        sum = int(input())
        while(True):
           option2 = int(input("1 - create tour \n"
                       + "2 - show tours \n"
                       + "3 - sell tour \n"
                       + "4 - buy tour from Agency2 \n"))
           if option2 == 1:
              option2_1 = int(input("1 - to Turkey \n"
                              + "2 - to Egypt \n"
                              + "3 - to Vietnam \n"
                              + "4 - to Dubai \n"))
              if option2_1 == 1:
                  tour = agency1.createTour("Turkey")
                  tour.create(40, list1, list1_costs, list1_tours)
                  sum -= 40;
                  print("Remains - " + str(sum))
              if option2_1 == 2:
                  tour = agency1.createTour("Egypt")
                  tour.create(30, list1, list1_costs, list1_tours)
                  sum -= 30;
                  print("Remains - " + str(sum))
              if option2_1 == 3:
                  tour = agency1.createTour("Vietnam")
                  tour.create(10, list1, list1_costs, list1_tours)
                  sum -= 10;
                  print("Remains - " + str(sum))
              if option2_1 == 4:
                  tour = agency1.createTour("Dubai")
                  tour.create(100, list1, list1_costs, list1_tours)
                  sum -= 100;
                  print("Remains - " + str(sum))
           if option2 == 2:
              agency1.showTour(list1)
           if option2 == 3:
               option2_3 = int(input("1 - to User \n"
                       + "2 - to Agency2 \n"))
               print("Enter your index of tour: ")
               index2_3 = int(input())-1
               if option2_3 == 1:
                   listUser.append(list1_tours[index2_3] + " " + str(list1_costs[index2_3] + 15))
                   listUser_costs.append(list1_costs[index2_3] + 15)
                   agency1.sellTour(list1, index2_3)
                   number = 15
                   number = int(list2_costs[-1])+number
                   sum +=  number
                   print("Remains - " + str(sum))
               if option2_3 == 2:
                   list2.append(list1_tours[index2_3] + " " + str(list1_costs[index2_3] + 15))
                   list2_costs.append(list1_costs[index2_3] + 15)
                   agency1.sellTour(list1, index2_3)
                   number = 15
                   number = int(list2_costs[-1])+number
                   sum +=  number
                   print("Remains - " + str(sum))
           if option2 == 4:
              agency2.showTour(list2)
              print("Enter index of tour from Agency2: ")
              index2_4 = int(input()) - 1
              number = 25
              list1_costs.append(str(list2_costs[index2_4]))
              number = int(list1_costs[-1])+number
              sum -= number
              agency1.buyTour(list1, list2, index2_4)
              if sum >= 0:
                  print("Remains - " + str(sum))
              if sum < 0:
                  print("Not enough money")
                  exit()
if optionUser == 3:
        print("Enter your sum of money: ")
        sum = int(input())
        while(True):
           option3 = int(input("1 - create tour \n"
                       + "2 - show tours \n"
                       + "3 - sell tour \n"
                       + "4 - buy tour from Agency1 \n"))
           if option3 == 1:
              option3_1 = int(input("1 - to Turkey \n"
                              + "2 - to Egypt \n"
                              + "3 - to Vietnam \n"
                              + "4 - to Dubai \n"))
              if option3_1 == 1:
                  tour = agency2.createTour("Turkey")
                  tour.create(70, list2, list2_costs, list2_tours)
                  sum -= 70;
                  print("Remains - " + str(sum))
              if option3_1 == 2:
                  tour = agency2.createTour("Egypt")
                  tour.create(15, list2, list2_costs, list2_tours)
                  sum -= 15;
                  print("Remains - " + str(sum))
              if option3_1 == 3:
                  tour = agency2.createTour("Vietnam")
                  tour.create(55, list2, list2_costs, list2_tours)
                  sum -= 55;
                  print("Remains - " + str(sum))
              if option3_1 == 4:
                  tour = agency2.createTour("Dubai")
                  tour.create(140, list2, list2_costs, list2_tours)
                  sum -= 140;
                  print("Remains - " + str(sum))
           if option3 == 2:
              agency2.showTour(list2)
           if option3 == 3:
               option3_3 = int(input("1 - to User \n"
                       + "2 - to Agency1 \n"))
               print("Enter your index of tour: ")
               index3_3 = int(input())-1
               if option3_3 == 1:
                   listUser.append(list2_tours[index3_3] + " " + str(list2_costs[index3_3] + 25))
                   listUser_costs.append(list2_costs[index3_3] + 25)
                   agency2.sellTour(list2, index3_3)
                   number = 25
                   number = int(list1_costs[-1])+number
                   sum +=  number
                   print("Remains - " + str(sum))
               if option3_3 == 2:
                   list1.append(list2_tours[index3_3] + " " + str(list2_costs[index3_3] + 25))
                   list1_costs.append(list2_costs[index3_3] + 25)
                   agency2.sellTour(list2, index3_3)
                   number = 25
                   number = int(list1_costs[-1])+number
                   sum +=  number
                   print("Remains - " + str(sum))
           if option3 == 4:
              agency1.showTour(list1)
              print("Enter index of tour from Agency1: ")
              index3_4 = int(input()) - 1
              number = 15
              list2_costs.append(str(list1_costs[index3_4]))
              number = int(list2_costs[-1])+number
              sum -= number
              agency2.buyTour(list1, list2, index3_4)
              if sum >= 0:
                  print("Remains - " + str(sum))
              if sum < 0:
                  print("Not enough money")
                  exit()
    