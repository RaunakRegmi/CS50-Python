def main():
    user_time = input("What time is it?: ")

    time = convert(user_time)

    if 7.0 <= time <= 8.0:
        print("Breakfast Time")
    elif 12.0 <= time <= 13.0:
        print("Lunch Time")
    elif 18.0 <= time <= 19.0:
        print("Dinner Time")


def convert(converted_time):
    global total

    converted_time = converted_time.replace(":", ' ')

    before, after = converted_time.split()

    before = int(before)

    after = int(after)

    after = after / 60

    total = before + after

    return total

if __name__ == "__main__":
    main()
