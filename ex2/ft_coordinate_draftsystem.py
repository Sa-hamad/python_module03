import math

def get_player_pos():
    print("=== Get the first set of coordinates ===")
    res1 = coords_first()
        
    print("\n=== Get the second set of coordinates ===")
    res2 = coords_second(res1)

def coords_first():
    success = False
    result = None

    print("Get the first set of coordinates")
    while not success:
        user_input = (input("Enter new coordinates as floats in format 'x,y,z': "))
    
        seperator = ","
        buffer = ""
        my_list =[]
        for char in user_input:
            if char == seperator:
                my_list.append(buffer)
                buffer = ""
            else:
                buffer += char
        my_list.append(buffer)

        if len(my_list) == 3:
            try: 
                for num in my_list:
                    current_check = num
                    float(current_check)   

                result = tuple(float(num) for num in my_list)
                sucess = True

                x1, y1, z1 = result
                x2, y2, z2 = 0.0, 0.0, 0.0

                print(f"Got a first tuple: {result}")
                print(f"It includes: X={x1}, Y={y1}, Z={z1}")

                center_dist: float = math.sqrt((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)
                print(f"Distance to center: {round(center_dist, 4)}")
                return result

            except ValueError as e:
                print(f"Error on parameter '{current_check}': {e}")
                return coords_first()
        else:
            print("Invalid syntax")
    
    return result


def coords_second(first_coords):
    success = False
    result = None

    print("Get the second set of coordinates")
    while not success:
        user_input = (input("Enter new coordinates as floats in format 'x,y,z': "))
        
        seperator = ","
        buffer = ""
        my_list =[]
        for char in user_input:
            if char == seperator:
                my_list.append(buffer)
                buffer = ""
            else:
                buffer += char
        my_list.append(buffer)

        if len(my_list) == 3:
            try: 
                for num in my_list:
                    current_check = num
                    float(current_check) 

                result = tuple(float(num) for num in my_list)
                success = True

                x1, y1, z1 = first_coords
                x2, y2, z2 = result

                center_dist: float = math.sqrt((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)
                print(f"Distance between the 2 sets of coordinates: {round(center_dist, 4)}")
                return result

            except ValueError as e:
                print(f"Error on parameter '{current_check}': {e}")
        else:
            print("Invalid syntax")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    get_player_pos()