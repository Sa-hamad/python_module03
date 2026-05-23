import sys

def inventory_system(inventory: dict[str,int]) -> None:

    print(f"Items: {list(inventory.keys)}")
    return inventory

    inventory: dict[str, int] = {}
    valid = False

    while not valid:
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            valid = True

        item, raw_quantity = mysplit(arg)
    
        print(f"Items: {list(inventory.keys)}")
        return inventory

        def my_split(string):
        seperator = ":"
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

if __name__ == "__main__":
    inventory_system()




