def add_mul(choice, *args):
    if choice == "add":
        result = sum(args)
    elif choice == "mul":
        result = 1
        for e in args:
            result *= e
    return result

print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))