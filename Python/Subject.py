from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from random import randrange



class Subject(ABC):

    @abstractmethod
    def registerObserver(self, observer : Observer):
        pass

    @abstractmethod
    def removeObserver(self, observer : Observer) :
        pass

    @abstractmethod
    def notifyObservers(self):
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, subject : Subject):
        pass


class ConcreteSubject(Subject):
    _state: int = None;
    _observers: List[Observer] = []

    def registerObserver(self, observer : Observer):
        print("Subject: Attached")
        self._observers.append(observer)

    def removeObserver(self, observer : Observer):
        self._observers.remove(observer)

    def notifyObservers(self) -> None:
        print("Subject: Notfing observers")
        for observer in self._observers:
            observer.update(self)


    def temperatureChanged(self):
        self._state = randrange(0, 35)
        print("Subject: My state has changed to: " + str(self._state))
        self.notifyObservers()


    def gettemperature(self):
        return self._state


class ConcreteObservableMobile(Observer):

    def __init__(self, name):
        self._name = name
        self.temperature = int = None

    def update(self, subject : Subject):
        self.temperature = subject.gettemperature()
        self.notify()

    def notify(self):
        print(self._name + "Says: temperature changed to: " + str(self.temperature) + " C")

        if(self.temperature > 26):
            print("It is really hot there")

        elif(self.temperature > 15):
            print("Nice temp")

        else:
            print("Cold")


class ConcreteObserverLCDDIsplay(Observer):
    def init(self, name):
        self._name = "Desktop Display"
        self.temperature: int = None

    def update(self, subject: ConcreteSubject):
        self.temperature = subject.gettemperature()
        self.notify()

    def notify(self):
        print("------------------------------------------")




if __name__ == "__main__":
    # The client code

    subject = ConcreteSubject()
    iPhone = ConcreteObservableMobile("iPhone")
    desktopDisplay = ConcreteObserverLCDDIsplay()

    subject.registerObserver(iPhone)
    subject.registerObserver(desktopDisplay)

    subject.temperatureChanged()
    subject.temperatureChanged()

    subject.removeObserver(desktopDisplay)

    subject.temperatureChanged()
