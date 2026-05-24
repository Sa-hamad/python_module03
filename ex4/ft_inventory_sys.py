import sys

    
def create_inventory(args: list[str]) -> None:
    items: dict[str, int] = {}
    keys: list[str] = []

    for item in args:
            
            parts = item.split(":")
            if len(parts) != 2:
                print(f"Error - invalid paramater '{item}'")
                continue
            key = parts[0]
            value = parts[1]
            try:
                value = int(value)
            except ValueError as e:
                print(f"Quantity error for 'key': {e}")
                continue
            if value < 0:
                print("Error: negative value")
                continue

            if items.get(key) is not None:
                print(f"Redundant item '{key}' - discarding")
                continue
            items[key] = value
            keys.append(key)
    return (items, keys)

#def calculate(inventory):
    

# loop through the dictionary
   
if __name__ == "__main__":
    
    print("=== Inventory System Analysis ===")

    inventory, item_keys = create_inventory(sys.argv[1:])
    total = sum(inventory.values())
    number = len(inventory)

    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_keys}")
    print(f"Total quantity of the {number} items: {total}")
    
    for key in item_keys:
        print(f"Item sword represents {(inventory[key] / total) * 100}")






