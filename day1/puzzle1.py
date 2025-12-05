import csv

def add_to_total(total, direction, value):
    """
    Adds or subtracts a value from the total based on the direction.

    Args:
        total (int): The current total.
        direction (str): 'R' to add or 'L' to subtract.
        value (int): The value to add or subtract.

    Returns:
        int: The updated total.
    """
    value = int(value)
    if direction == 'R':
        return total + value
    elif direction == 'L':
        return total - value
    else:
        raise ValueError("Direction must be either 'R' or 'L'")

def parse_combos_by_line(filepath):
    total = 50
    old = total
    count = 0
    wrap_count = 0
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue
            direction = row[0][0]
            value = int(row[0][1:])
            old = total
            
            new_total = add_to_total(total, direction, value)
            total = new_total % 100
            if direction == 'R':
                wrap_count += (old + value) // 100
                total = (old + value) % 100

            elif direction == 'L':
                wrap_count += (99 - old + value) // 100
                total = (old - value) % 100
            
            if total == 0:
                count += 1
    return wrap_count, count

if __name__ == "__main__":
    filepath = 'day1/combos.csv'
    print(parse_combos_by_line(filepath))
