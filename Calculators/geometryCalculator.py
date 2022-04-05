'''
ATL MARATHON
NAME: SOURAV
DOC: 5/4/2022
TOPIC: Geometry Calculator
'''

import math

mainLoop = True

print("***>GEOMETRY CALCULATOR***>","\n")

class Cube:

    def CSA(self):
        side = float(input("Enter the side ="))
        a = 4*(side*side)
        print(f"The CSA of a Cube is = {a}","\n")

    def TSA(self):
        side = float(input("Enter the side ="))
        a = 6*(side*side)
        print(f"The TSA of a Cube is = {a}","\n")

    def Volume(self):
        side = float(input("Enter the side ="))
        a = (side*side*side)
        print(f"The Volume of a Cube is = {a}","\n")

class Cuboid:

    def CSA(self):
        l = float(input("Enter the Length ="))
        b = float(input("Enter the Breadth ="))
        h = float(input("Enter the Height ="))
        a = 2*h*(l+b)
        print(f"The CSA of a Cuboid is = {a}","\n")

    def TSA(self):
        l = float(input("Enter the Length ="))
        b = float(input("Enter the Breadth ="))
        h = float(input("Enter the Height ="))
        a = 2*((l*b)*(b*h)*(h*l))
        print(f"The TSA of a Cuboid is = {a}", "\n")

    def Volume(self):
        l = float(input("Enter the Length ="))
        b = float(input("Enter the Breadth ="))
        h = float(input("Enter the Height ="))
        a =(l*b*h)
        print(f"The Velume of a Cuboid is = {a}", "\n")

class Cylinder:

    def CSA(self):
        r = float(input("Enter the Radius ="))
        h = float(input("Enter the Height ="))
        a = 2*math.pi*r*h
        print(f"The CSA of a Cylinder is = {a}","\n")

    def TSA(self):
        r = float(input("Enter the Radius ="))
        h = float(input("Enter the Height ="))
        a = 2*math.pi*r*(h*r)
        print(f"The TSA of a Cylinder is = {a}","\n")

    def Volume(self):
        r = float(input("Enter the Radius ="))
        h = float(input("Enter the Height ="))
        a = math.pi*(r*r)*h
        print(f"The Volume of a Cylinder is = {a}","\n")

class Cone:

    def CSA(self):
        r = float(input("Enter the Radius ="))
        l = float(input("Enter the Slant height ="))
        a = math.pi*r*l
        print(f"The CSA of a Cone is = {a}","\n")

    def TSA(self):
        r = float(input("Enter the Radius ="))
        l = float(input("Enter the Slant height ="))
        a = math.pi*r*(l+r)
        print(f"The TSA of a Cone is = {a}","\n")

    def Volume(self):
        r = float(input("Enter the Radius ="))
        h = float(input("Enter the Height ="))
        a = (1/3)*math.pi*(r*r)*h
        print(f"The Volume of a Cube is = {a}","\n")

class Sphere:

    def CSA(self):
        r = float(input("Enter the Radius ="))
        a = 4*math.pi*(r*r)
        print(f"The CSA of a Sphere is = {a}","\n")

    def TSA(self):
        r = float(input("Enter the Radius ="))
        a = 4 * math.pi * (r * r)
        print(f"The TSA of a Sphere is = {a}", "\n")

    def Volume(self):
        r = float(input("Enter the Radius ="))
        a = (4/3) * math.pi * (r * r * r)
        print(f"The Volume of a Sphere is = {a}","\n")

class HSphere:

    def CSA(self):
        r = float(input("Enter the Radius ="))
        a = 2*math.pi*(r*r)
        print(f"The CSA of a Hemisphere is = {a}","\n")

    def TSA(self):
        r = float(input("Enter the Radius ="))
        a = 3 * math.pi * (r * r)
        print(f"The TSA of a Hemisphere is = {a}", "\n")

    def Volume(self):
        r = float(input("Enter the Radius ="))
        a = (2/3) * math.pi * (r * r* r)
        print(f"The Volume of a Hemisphere is = {a}","\n")

cube = Cube()
cuboid = Cuboid()
cone = Cone()
cylinder = Cylinder()
sphere = Sphere()
hsphere = HSphere()

while mainLoop:

    try:

        print("***>PICK THE SHAPE***>")
        print("Cube, Cuboid, Cylinder, Cone, Sphere, Hemisphere","\n")

        shape = str(input("Write the shape name (ex: Cube,Cone) = "))

        print("\n")

        print("***>PICK THE FORMULA***>")
        print("Volume, TSA, CSA","\n")

        formula = str(input("Write the formula name (ex: Volume,CSA) = "))

        if shape == "Cube" or shape == "cube":
            if formula == "CSA" or shape == "csa":
                cube.CSA()
            if formula == "TSA" or shape == "tsa":
                cube.TSA()
            if formula == "Volume" or shape == "volume":
                cube.Volume()

        if shape == "Cuboid" or shape == "cuboid":
            if formula == "CSA" or shape == "csa":
                cuboid.CSA()
            if formula == "TSA" or shape == "tsa":
                cuboid.TSA()
            if formula == "Volume" or shape == "volume":
                cuboid.Volume()

        if shape == "Cone" or shape == "cone":
            if formula == "CSA" or shape == "csa":
                cone.CSA()
            if formula == "TSA" or shape == "tsa":
                cone.TSA()
            if formula == "Volume" or shape == "volume":
                cone.Volume()

        if shape == "Cylinder" or shape == "cylinder":
            if formula == "CSA" or shape == "csa":
                cylinder.CSA()
            if formula == "TSA" or shape == "tsa":
                cylinder.TSA()
            if formula == "Volume" or shape == "volume":
                cylinder.Volume()

        if shape == "Sphere" or shape == "sphere":
            if formula == "CSA" or shape == "csa":
                sphere.CSA()
            if formula == "TSA" or shape == "tsa":
                sphere.TSA()
            if formula == "Volume" or shape == "volume":
                sphere.Volume()

        if shape == "Hemisphere" or shape == "hemisphere":
            if formula == "CSA" or shape == "csa":
                hsphere.CSA()
            if formula == "TSA" or shape == "tsa":
                hsphere.TSA()
            if formula == "Volume" or shape == "volume":
                hsphere.Volume()

    except ValueError:
        print("NOTE: There was an error in the input. Please Try again.", "\n")