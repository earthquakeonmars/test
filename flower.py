class Flower:
    flowers_total: int = 0

    def __init__(self, name: str):
        self._name: str = name
        Flower.flowers_total += 1

flower1 = Flower('Ромашка')
flower2 = Flower('tulip')
print(Flower.flowers_total)
flower3 = Flower('poppy')
print(Flower.flowers_total)
