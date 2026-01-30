def cToFConverter():
    while True:
        cTemp = input("Please enter C degree: ") # if you put int(input()) here, then you can not use while loop if user input None/leave it empty
                                                # as none/empty is not int, it will cause error
        if cTemp:
            cTemp = float(cTemp)
            fTemp = 9*cTemp/5 + 32
            print(f"{cTemp}C is converted to {fTemp}F")
            break #if users input cTemp = true
        else:
            print(f"cTemp input is empty")
            continue #if users does not input cTemp, it will give you another chance to do


def main():
    cToFConverter()


if __name__ == "__main__":
    main()