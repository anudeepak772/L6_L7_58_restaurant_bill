def clean_dish_name(name):
    """
    Removes the chef's-special markers (*, #, ~) and title-cases the name.
    Safely handles None or non-string inputs.
    """
    if not isinstance(name, str):
        return ""
    name = name.strip()
    for ch in ['*', '#', '~']:
        name = name.replace(ch, '')
    return name.strip().title()


def parse_item_prices(text):
    """
    Parses comma-separated prices into a list of ints.
    Ignores invalid/non-numeric tokens and safely handles None or empty input.
    """
    if not isinstance(text, str) or not text.strip():
        return []
    prices = []
    for item in text.split(','):
        cleaned = item.strip()
        if cleaned:
            try:
                prices.append(int(cleaned))
            except ValueError:
                continue
    return prices


def split_amount(text):
    """
    Splits 'TOTAL/PEOPLE' into the amount each person pays.
    Safely returns 0 on invalid formats, non-integers, or division by zero.
    """
    if not isinstance(text, str) or '/' not in text:
        return 0
    parts = text.split('/')
    if len(parts) != 2:
        return 0
    try:
        total = int(parts[0].strip())
        people = int(parts[1].strip())
        if people <= 0:
            return 0
        return total // people
    except ValueError:
        return 0


def main():
    print("==== Running clean_dish_name ====")
    value = input("Enter a dish name from the menu (e.g. *paneer tikka*): ")
    print("Dish name:", clean_dish_name(value))

    print("\n==== Running parse_item_prices ====")
    value = input("Enter item prices separated by commas (e.g. 250,180,320): ")
    print("Item prices:", parse_item_prices(value))

    print("\n==== Running split_amount ====")
    value = input("Enter the bill and number of people as TOTAL/PEOPLE (e.g. 1200/4): ")
    print("Each person pays:", split_amount(value))


if __name__ == "__main__":
    main()