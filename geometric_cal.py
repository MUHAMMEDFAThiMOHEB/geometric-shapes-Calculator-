class GeometricShape:
    def calculates(self):
        raise NotImplementedError("Will be implemented in subclass")
    def info(self):
        raise NotImplementedError("Will be implemented in subclass")
    def user_input(self):
        raise NotImplementedError("Will be implemented in subclass")
    
class Square(GeometricShape):

    def __init__(self):
        self.side = None

    def user_input(self):
        self.side = int(input("Enter the length of square side: "))
        return self.side
    
    def info(self):
        print(f"Square: A quadrilateral with four equal sides and four right angles.")
        print(f"Square Perimeter = 4 × side, Area = side² ")
    
    def calculates(self):
        perimeter = self.side * 4
        area = self.side ** 2
        return f"Square perimeter = {perimeter}\nSquare area = {area}"
    
class Triangle(GeometricShape):

    def __init__(self):
        self.side1 = None
        self.side2 = None
        self.base = None
        self.height = None

    def user_input(self):
        self.side1 = int(input("Enter the length of the first side: "))
        self.side2 = int(input("Enter the length of the second side: "))
        self.base = int(input("Enter the length of the triangle base: "))
        self.height = int(input("Enter the height of the triangle: "))
        return self.side1, self.side2, self.side3
    
    def info(self):
        print(f"Triangle: A polygon with three sides;")
        print(f"Perimeter = sum of all sides, Area = (base × height) ÷ 2")
    
    def calculates(self):
        perimeter = sum(self.side1, self.side2, self.side3)
        area = (self.base * self.height)/2
        return f"triangle perimeter = {perimeter}\ntriangle area = {area}"
    
    
    
def take_user_choice(self):
    while True:
        try:
            choice = int(input("Choose a shape: "))
            if choice <= 0 or choice > 5:
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
        4: "Rhombus",
        5: 'Circle'
    }
    for key, value in shapes.items():
        print(f"[{key}]: {value}")


# Square: A quadrilateral with four equal sides and right angles;
# Perimeter = 4 × side, Area = side²

# Triangle: A polygon with three sides;
# Perimeter = sum of all sides, Area = (base × height) ÷ 2

# Rectangle: A quadrilateral with opposite sides equal and right angles;
# Perimeter = 2 × (length + width), Area = length × width

# Circle: A round shape with all points equidistant from the center;
# Perimeter (Circumference) = 2 × π × radius, Area = π × radius²

# Rhombus: A quadrilateral with all sides equal and opposite angles equal;
# Perimeter = 4 × side, Area = (diagonal₁ × diagonal₂) ÷ 2