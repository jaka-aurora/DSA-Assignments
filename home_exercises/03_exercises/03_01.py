
def generate_multiplication_table(n):
    multiplication_table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        multiplication_table.append(row)

    return multiplication_table

def print_multiplication_table(table):
    for row in table:
        for item in row:
            print(f"{item:>5}", end="")
        print()

def main():
    n = 12
    table = generate_multiplication_table(n)
    return print_multiplication_table(table)

main()