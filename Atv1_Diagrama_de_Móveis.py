import abc
from abc import ABC, abstractmethod

class AbstractCabinet(ABC):
    @abstractmethod
    def furniture_function(self) -> str:
        pass

    @abstractmethod
    def show_style(self) -> str:
        pass

class AbstractChair(ABC):
    @abstractmethod
    def furniture_function(self) -> str:
        pass

    @abstractmethod
    def show_style(self) -> str:
        pass

class AbstractDiningTable(ABC):
    @abstractmethod
    def furniture_function(self) -> str:
        pass

    @abstractmethod
    def show_style(self) -> str:
        pass

class FurnitureFactory(ABC):
    
    @abstractmethod
    def create_cabinet(self) -> AbstractCabinet: 
        pass
        
    @abstractmethod
    def create_chair(self) -> AbstractChair: 
        pass
        
    @abstractmethod
    def create_dining_table(self) -> AbstractDiningTable: 
        pass


class ScandinavianCabinet(AbstractCabinet):
    def furniture_function(self) -> str:
        return "Eu sou um armário guardando coisas."
    def show_style(self) -> str:
        return "Eu sou do estilo Escandinavo."

class ScandinavianChair(AbstractChair):
    def furniture_function(self) -> str:
        return "Eu sou uma cadeira para sentar."
    def show_style(self) -> str:
        return "Eu sou do estilo Escandinavo."

class ScandinavianDiningTable(AbstractDiningTable):
    def furniture_function(self) -> str:
        return "Eu sou uma mesa de jantar para refeições."
    def show_style(self) -> str:
        return "Eu sou do estilo Escandinavo."


class ScandinavianFactory(FurnitureFactory):
    def create_cabinet(self) -> AbstractCabinet:
        return ScandinavianCabinet()
        
    def create_chair(self) -> AbstractChair:
        return ScandinavianChair()
        
    def create_dining_table(self) -> AbstractDiningTable:
        return ScandinavianDiningTable()

class ClassicCabinet(AbstractCabinet):
    def furniture_function(self) -> str:
        return "Eu sou um armário guardando coisas."
    def show_style(self) -> str:
        return "Eu sou do estilo Clássico."

class ClassicChair(AbstractChair):
    def furniture_function(self) -> str:
        return "Eu sou uma cadeira para sentar."
    def show_style(self) -> str:
        return "Eu sou do estilo Clássico."

class ClassicDiningTable(AbstractDiningTable):
    def furniture_function(self) -> str:
        return "Eu sou uma mesa de jantar para refeições."
    def show_style(self) -> str:
        return "Eu sou do estilo Clássico."


class ClassicFactory(FurnitureFactory):
    def create_cabinet(self) -> AbstractCabinet:
        return ClassicCabinet()
        
    def create_chair(self) -> AbstractChair:
        return ClassicChair()
        
    def create_dining_table(self) -> AbstractDiningTable:
        return ClassicDiningTable()


class ContemporaryCabinet(AbstractCabinet):
    def furniture_function(self) -> str:
        return "Eu sou um armário guardando coisas."
    def show_style(self) -> str:
        return "Eu sou do estilo Contemporâneo."

class ContemporaryChair(AbstractChair):
    def furniture_function(self) -> str:
        return "Eu sou uma cadeira para sentar."
    def show_style(self) -> str:
        return "Eu sou do estilo Contemporâneo."

class ContemporaryDiningTable(AbstractDiningTable):
    def furniture_function(self) -> str:
        return "Eu sou uma mesa de jantar para refeições."
    def show_style(self) -> str:
        return "Eu sou do estilo Contemporâneo."


class ContemporaryFactory(FurnitureFactory):
    def create_cabinet(self) -> AbstractCabinet:
        return ContemporaryCabinet()
        
    def create_chair(self) -> AbstractChair:
        return ContemporaryChair()
        
    def create_dining_table(self) -> AbstractDiningTable:
        return ContemporaryDiningTable()


def client_program(factory: FurnitureFactory):
    cabinet = factory.create_cabinet()
    chair = factory.create_chair()
    
    print(f"--- Usando a fábrica: {factory.__class__.__name__} ---")
    print(f"Cadeira: {chair.show_style()} ({chair.furniture_function()})")
    print(f"Armário: {cabinet.show_style()} ({cabinet.furniture_function()})")
    print("-" * 30)

print("### Atividade 1: Fábrica de Móveis ###\n")
client_program(ClassicFactory())
client_program(ScandinavianFactory())
client_program(ContemporaryFactory())