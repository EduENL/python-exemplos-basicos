from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.__nome = nome

#metodo getter para acessar o atríbuto privado (Encapsulamento)
    def get_nome(self):
        return self.__nome

#Método abstrato (Abstração)
    @abstractmethod
    def fazer_som(self):
        pass
