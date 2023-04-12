from abc import ABC, abstractmethod
from asyncio import SubprocessTransport

class Strategy(ABC):
    @abstractmethod
    def show(self, list):
        pass

class Strategy1(Strategy):
    def show(self, list):
        for i,value in enumerate(list):
            print(str(i+1) + "{" + value + "}")

class Strategy2(Strategy):
    def show(self, list):
        for i,value in enumerate(list):
            print(str(i+1) + "<element>" + value + "</element>")


class Context:
    def __init__(self, strategy : Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def show(self, list):
        return self._strategy.show(list)

print("Enter your Friday subjects: ")
list_subjects = input()
list = list_subjects.split(" ")
while(True):
    print("1 - json format \n"
      + "2 - XML format \n"
      + "5 - Exit() \n"
      + "3 - Add a subject \n"
      + "4 - Delete a subject")
    option = int(input())
    print("-----Friday-----")
    if option == 1:
        context = Context(Strategy1())
        context.show(list)
    if option == 2:
        context.strategy = Strategy2()
        context.show(list)
    if option == 5:
        exit()
    if option == 3:
        print("Enter name of subject: ")
        sub = input()
        list.append(sub)
    if option == 4:
        print("Enter index of subject: ")
        index = int(input())-1
        list.pop(index)


