from abc import ABC
from abc import abstractmethod
"""
Crear una clase abstracta informal y otra formal Auto con 2 metodos.

-adelante
-atras
Crear 2 clases que implementen la clase Auto (solo es necesario prints en el codigo).
"""

class auto_formal(ABC):
    @abstractmethod
    def auto_adelante_form(self):
        pass
    @abstractmethod
    def auto_atras_form(self):
        pass

class auto_informal:
    def auto_adelante_inf(self):
        pass
    def auto_atras_inf(self):
        pass


class ford_formal(auto_formal):
    def auto_adelante_form(self):
        print("Fort -> adelante")
    def auto_atras_form(self):
        print("Fort -> atras")

class fiat_informal(auto_informal):
    def auto_adelante_inf(self):
        print("Fiat -> adelante")
    def auto_atras_inf(self):
        print("Fiat -> atras")



auto_fiat = fiat_informal()
auto_fiat.auto_adelante_inf()
auto_fiat = fiat_informal()
auto_fiat.auto_atras_inf()
auto_ford = ford_formal()
auto_ford.auto_atras_form()
auto_ford = ford_formal()
auto_ford.auto_adelante_form()
