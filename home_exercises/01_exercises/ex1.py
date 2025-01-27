def main():
    input_str = input("Give input:")
    b = int(input_str)
    kbytes = b / (2 ** 10)
    mbytes = b / (2 ** 20)
    gbytes = b / (2 ** 30)

    print(f"bytes \t\t {b} B")
    print(f"Kilobytes\t {(kbytes):.6f} KB")
    print(f"Megabytes\t {(mbytes):.6f} MB")
    print(f"Gigabytes\t {(gbytes):.6f} GB")

if __name__ == '__main__': 
    main()