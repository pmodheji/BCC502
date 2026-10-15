"""Part 2, Module 2: Create a customer order (coffee shop order tracker)."""

MENU = {"latte": 4.50, "espresso": 3.00, "muffin": 3.25, "cookie": 2.00}


def receipt_lines(order, menu=MENU):
    """Return the receipt as a list of text lines."""
    lines = []
    total = 0
    for item in order:
        price = menu[item]
        lines.append(f"{item.title():<12} ${price:>6.2f}")
        total += price
    lines.append(f"{'Total':<12} ${total:>6.2f}")
    return lines


def main():
    order = []
    while True:
        item = input("Add an item (or type 'done'): ").strip().lower()
        if item == "done":
            break
        if item in MENU:
            order.append(item)
        else:
            print(f"Sorry, we do not have {item}.")
    print("\n".join(receipt_lines(order)))


if __name__ == "__main__":
    main()
