import abc
from abc import ABC, abstractmethod

class MotorVehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

class ElectricVehicle(ABC):
    @abstractmethod
    def charge(self) -> str:
        pass
    
    @abstractmethod
    def drive(self) -> str:
        pass


class Corporation(ABC):
    
    @abstractmethod
    def create_motor_vehicle(self) -> MotorVehicle: 
        pass
        
    @abstractmethod
    def create_electric_vehicle(self) -> ElectricVehicle: 
        pass


class FutureVehicleMotorcycle(MotorVehicle):
    def drive(self) -> str:
        return "Pilotando a moto FutureVehicle (combustão)"

class FutureVehicleElectricCar(ElectricVehicle):
    def charge(self) -> str:
        return "Carregando o carro elétrico FutureVehicle"
    def drive(self) -> str:
        return "Dirigindo o carro elétrico FutureVehicle (silencioso)"

 
class FutureVehicleCorporation(Corporation):
    def create_motor_vehicle(self) -> MotorVehicle:
        return FutureVehicleMotorcycle()
        
    def create_electric_vehicle(self) -> ElectricVehicle:
        return FutureVehicleElectricCar()

class NextGenMotorcycle(MotorVehicle):
    def drive(self) -> str:
        return "Pilotando a moto NextGen (combustão)"

class NextGenElectricCar(ElectricVehicle):
    def charge(self) -> str:
        return "Carregando o carro elétrico NextGen"
    def drive(self) -> str:
        return "Dirigindo o carro elétrico NextGen (silencioso)"


class NextGenCorporation(Corporation):
    def create_motor_vehicle(self) -> MotorVehicle:
        return NextGenMotorcycle()
        
    def create_electric_vehicle(self) -> ElectricVehicle:
        return NextGenElectricCar()



def client_program_vehicles(factory: Corporation):
    motor_vehicle = factory.create_motor_vehicle()
    electric_vehicle = factory.create_electric_vehicle()
    
    print(f"--- Usando a corporação: {factory.__class__.__name__} ---")
    print(f"Veículo a Motor: {motor_vehicle.drive()}")
    print(f"Veículo Elétrico: {electric_vehicle.drive()} | {electric_vehicle.charge()}")
    print("-" * 30)


print("\n### Atividade 2: Fábrica de Veículos ###\n")
client_program_vehicles(FutureVehicleCorporation())
client_program_vehicles(NextGenCorporation())