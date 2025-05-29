num = int(input("Enter A number:"))
if num <= 10:
    print("Too Low")
elif num <= 30:
    print("Low")
elif num <= 60:
    print("Medium")
elif num <= 90:
    print("High")
elif num > 91:
    print("Very High")