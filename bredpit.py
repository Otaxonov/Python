# Try...Except

def main():
    a = None
    n = input()
    try:
        n = int(n)
    except ValueError:
        print(f"{n} is not a number!")
    else:
        print(n ** 2)

if __name__ == "__main__":
    main()