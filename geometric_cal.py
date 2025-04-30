class RegularShapes:
    
    def __init__(self,perimeter,area,sides,side_value):
        self.sides = sides
        self.perimeter = perimeter
        self.area = area
        self.side_value = side_value
    
    def take_user_input(self):
        while True:
            try:
                choice = int(input("Choose a shape: "))
                if choice <= 0:
                    print("No such choice! Try again.")
                else:
                    return choice
            except ValueError:
                print("Invalid input! Numeric input only accepted.")

    def display_choicess(self):
        shapes = {
            1: 'Square',
            2: 'Rectangle',
            3: 'Triangle',
            4: 'Circle',
            5: 'Other'
        }
        for key, value in shapes.items():
            print(f"[{key}]: {value}")
    
    def square(self):
        print(f"### -- Square: A quadrilateral with four equal sides and four right angles.".title())
        self.perimeter = self.sides*4
        self.area = self.sides*self.side_value


