import sys
i: int = 0


def main(args: list[str] = sys.argv[1:]) -> None:
    global i
    print(f"Program Name: {sys.argv[0]}")
    if len(args) > 0:
        print(f"Arguments Recieved: {len(args)}")
    else:
        print("No arguments provided!")
    for i in range(len(args)):
        print(f"Argument {(i+1)}: {args[i]}")
    print(f"Total Arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
