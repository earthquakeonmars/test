class Wolf:

    wolf: str = 'wolf'
    total: int = 0

    def __init__(self):
        Wolf.total += 1

wolf1 = Wolf()
print(Wolf.total)
