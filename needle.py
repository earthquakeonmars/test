class Needle:

    pointed: bool = True
    total: int = 0

    def __init__(self, thickness: float):
        self.thickness = thickness  # Thickness in mm
        Needle.total += 1

needle1 = Needle(0.7)
print(Needle.total)
