class CircleExample:
    def __init__(self, diameter):  # Konstuktor
        print('CircleText loomine')
        self.diameter = diameter

    def radius(self):  # default argument on self
        print(f'CircleText raadius {self.diameter / 2}')

    @staticmethod  # temas ei toimu ühtegi arvutust, ta on staatiline
    def area():
        print('CircleText pindala')
