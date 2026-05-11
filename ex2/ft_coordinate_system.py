import math


class CreateCoordinates:
    def __init__(self, type):
        self.type = type
        self.coords = None

    def get_valid_input(self):
        success = False

        print(f"Get the {self.type} set of coordinates")
        while not success:
            user_input = (input("Enter new coordinates"
                                "as floats in format 'x,y,z': "))

            my_list = self.my_split(user_input)

            if len(my_list) != 3:
                print("Invalud syntax")
            else:
                try:
                    for num in my_list:
                        current_val = num
                        float(current_val)

                    self.coords = tuple(float(num) for num in my_list)
                    success = True

                except ValueError as e:
                    print(f"Error on parameter '{current_val}': {e}")
        return self.coords

    def my_split(self, string):
        seperator = ","
        buffer = ""
        split_stuff = []

        for char in string:
            if char == seperator:
                split_stuff.append(buffer)
                buffer = ""
            else:
                buffer += char
        split_stuff.append(buffer)
        return split_stuff


def get_player_pos() -> None:
    first_coords = CreateCoordinates("first")
    second_coords = CreateCoordinates("second")

    res1 = first_coords.get_valid_input()

    x1, y1, z1 = res1
    x2, y2, z2 = 0.0, 0.0, 0.0

    print(f"Got a first tuple: {res1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    res1_center: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance to center: {round(res1_center, 4)}")

    res2 = second_coords.get_valid_input()

    x2, y2, z2 = res2

    res1_res2: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of"
          f"coordinates: {round(res1_res2, 4)}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()
