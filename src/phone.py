from src.item import Item


class Phone(Item):
    """
    класс `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут,
    содержащий количество поддерживаемых сим-карт
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    # def add(self, other):
    #     if not isinstance(other, Item):
    #         raise ValueError('Нельзя складывать.')
    #     return int(self.quantity) + int(other.quantity)

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_number):
        if int(sim_number) > 0:
            self.number_of_sim = sim_number
            return self.number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
