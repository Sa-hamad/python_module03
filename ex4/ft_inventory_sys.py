import sys


class InventoryInfo:
    def __init__(self, args: list[str] = []):
        self.args = args
        self.stuff, self.names = self.create_inventory()
        self.total = sum(self.stuff.values())
        self.most = self.most_abundant()
        self.least = self.least_abundant()

    def create_inventory(self) -> tuple[dict[str, int], list[str]]:

        stuff: dict[str, int] = {}
        names: list[str] = []

        for item in self.args:

            parts = item.split(":")
            if len(parts) != 2:
                print(f"Error - invalid paramater '{item}'")
                continue
            key = parts[0]
            value = parts[1]
            try:
                int_value = int(value)
            except ValueError as e:
                print(f"Quantity error for 'key': {e}")
                continue
            if int_value < 0:
                print("Error: negative value")
                continue

            if stuff.get(key) is not None:
                print(f"Redundant item '{key}' - discarding")
                continue
            stuff[key] = int_value
            names.append(key)
        return (stuff, names)

    def percent(self) -> float:

        for key in self.stuff.values():
            result = (key / self.total) * 100
            rnd_result = round(result, 1)
            print(f"Item {key} represents {rnd_result}%")
        return (0)

    def most_abundant(self) -> tuple[str, int]:

        if not self.stuff:
            return ("", 0)
        value = max(self.stuff.values())
        name = [n for n, v in self.stuff.items() if v == value][0]
        return (name, value)

    def least_abundant(self) -> tuple[str, int]:

        if not self.stuff:
            return ("", 0)
        value = min(self.stuff.values())
        name = [n for n, v in self.stuff.items() if v == value][0]
        return (name, value)


if __name__ == "__main__":

    print("=== Inventory System Analysis ===")

    info = InventoryInfo(sys.argv[1:])
    number = len(info.stuff)
    max_n, max_v = info.most_abundant()
    min_n, min_v = info.least_abundant()

    print(f"Got inventory: {info.stuff}")
    print(f"Item list: {info.names}")
    print(f"Total quantity of the {number} items: {info.total}")

    info.percent()
    print(f"Item most abundant: {max_n} with quantity {max_v}")
    print(f"Item least abundant: {min_n} with quantity {min_v}")

    info.stuff.update({"magic_item": 1})
    print(f"Updated inventory: {info.stuff}")
