from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
    
    @abstractmethod
    def usar(self) -> str:
        pass

class Armor(ABC):
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        
    @abstractmethod
    def usar(self) -> str:
        pass


class EquipmentFactory(ABC):
    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass
        
    @abstractmethod
    def create_armor(self) -> Armor:
        pass


class Sword(Weapon):
    def __init__(self):
        super().__init__("Espada", "Uma lâmina afiada.")
    def usar(self) -> str:
        return "Cortando com a Espada!"

class Shield(Armor):
    def __init__(self):
        super().__init__("Escudo", "Defende ataques.")
    def usar(self) -> str:
        return "Bloqueando com o Escudo!"


class MeleeFactory(EquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Sword() 
        
    def create_armor(self) -> Armor:
        return Shield() 


class Bow(Weapon):
    def __init__(self):
        super().__init__("Arco", "Dispara flechas.")
    def usar(self) -> str:
        return "Atirando uma flecha com o Arco!"

class Helmet(Armor):
    def __init__(self):
        super().__init__("Capacete", "Protege a cabeça.")
    def usar(self) -> str:
        return "Protegendo a cabeça com o Capacete!"


class RangedFactory(EquipmentFactory):
    def create_weapon(self) -> Weapon:
        return Bow()
        
    def create_armor(self) -> Armor:
        return Helmet() 

class MagicStaff(Weapon):
    def __init__(self):
        super().__init__("Cajado Mágico", "Canaliza magia.")
    def usar(self) -> str:
        return "Lançando uma bola de fogo com o Cajado!"

class MagicFactory(EquipmentFactory):
    def create_weapon(self) -> Weapon:
        return MagicStaff()
        
    def create_armor(self) -> Armor:
        return Helmet() 



def client_program_equipment(factory: EquipmentFactory):
    weapon = factory.create_weapon()
    armor = factory.create_armor()
    
    print(f"--- Criando kit com a fábrica: {factory.__class__.__name__} ---")
    print(f"Arma: {weapon.nome} ({weapon.descricao}) -> {weapon.usar()}")
    print(f"Armadura: {armor.nome} ({armor.descricao}) -> {armor.usar()}")
    print("-" * 30)

# Demonstração
print("\n### Atividade 3: Fábrica de Equipamentos ###\n")
client_program_equipment(MeleeFactory())
client_program_equipment(RangedFactory())
client_program_equipment(MagicFactory())