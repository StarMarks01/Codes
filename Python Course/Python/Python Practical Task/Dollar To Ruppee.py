while True:
    print("0.Exit")
    print("1.United States Of America")
    print("2.Australia")
    print("3.Canada")
    print("4.New Zealand")
    print("5.Singapore")
    print("6.Hong Kong")
    print("7.Taiwan")
    print("8.Fiji")
    print("9.Belize")
    print("10.Bahamas")
    print("11.Barbados")
    print("12.Brunei")
    print("13.Guyana")
    print("14.Jamaica")
    print("15.Namibia (alongside NAD)")
    print("16.Suriname")
    print("17.Trinidad and Tobago")

    ch = int(input("Enter The Country You want to calculate to rupees:"))
    if ch == 1:
        USD = int(input("Enter The US Dollar Value:"))
        INR = USD * 83.67
        print("Dollar to Indian Currency is:",INR)
    elif ch == 2:
        AUD = int(input("Enter Australia Dollar Value:"))
        INR = AUD * 86.67
        print("Dollar to Indian Currency is:",INR)
    elif ch == 3:
        CAD = int(input("Enter Canada Dollar Value:"))
        INR = CAD * 86.67
        print("Dollar to Indian Currency is:",INR)
    elif ch == 4:
        NZD = int(input("Enter New Zealand Dollar Value:"))
        INR = NZD * 48.37
        print("Dollar to Indian Currency is:",INR)
    elif ch == 5:
        SGD = int(input("Enter Singapore Dollar Value:"))
        INR = SGD * 63.76
        print("Dollar to Indian Currency is:",INR)
    elif ch == 6:
        HKD = int(input("Enter Hong Kong Dollar Value:"))
        INR = HKD * 11.17
        print("Dollar to Indian Currency is:",INR)
    elif ch == 7:
        TWD = int(input("Enter Taiwan Dollar Value:"))
        INR = TWD * 86.67
        print("Dollar to Indian Currency is:",INR)
    elif ch == 8:
        FJD = int(input("Enter Fiji Dollar Value:"))
        INR = FJD * 37.14
        print("Dollar to Indian Currency is:",INR)
    elif ch == 9:
        BZD = int(input("Enter Belize Dollar Value:"))
        INR = BZD * 43.16
        print("Dollar to Indian Currency is:",INR)
    elif ch == 10:
        BSD = int(input("Enter Bahamas Dollar Value:"))
        INR = BSD * 86.69
        print("Dollar to Indian Currency is:",INR)
    elif ch == 11:
        BBD = int(input("Enter Barbados Dollar Value:"))
        INR = BBD * 42.94
        print("Dollar to Indian Currency is:",INR)
    elif ch == 12:
        BND = int(input("Enter Brunei Dollar Value:"))
        INR = BND * 64.41
        print("Dollar to Indian Currency is:",INR)
    elif ch == 13:
        GYD = int(input("Enter Guyana Dollar Value:"))
        INR = GYD * 0.41
        print("Dollar to Indian Currency is:",INR)
    elif ch == 14:
        JMD = int(input("Enter Jamaica Dollar Value:"))
        INR = JMD * 0.55
        print("Dollar to Indian Currency is:",INR)
    elif ch == 15:
        NAD = int(input("Enter Namibia (alongside NAD) Dollar Value:"))
        INR = NAD * 0.051
        print("Dollar to Indian Currency is:",INR)
    elif ch == 16:
        SRD = int(input("Enter Suriname Dollar Value:"))
        INR = SRD * 2.35
        print("Dollar to Indian Currency is:",INR)
    elif ch == 17:
        TTD = int(input("Enter Trinidad and Tobago Dollar Value:"))
        INR = TTD * 12.71
        print("Dollar to Indian Currency is:",INR)
    elif ch == 0:
        print("Exiting...")
        break
