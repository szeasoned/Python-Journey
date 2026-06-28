import datetime

FILE_PATH = "study_log.txt"
SEPARATOR = "=" * 40


def get_datetime():
    current_datetime = datetime.datetime.now()

    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")

    return date, time


def log_session():
    print(SEPARATOR)

    subject = input("Subject studied: ")
    topic = input("Topic covered: ")

    while True:
        try:
            duration = int(input("Duration of study (minutes): "))

            if duration <= 0:
                print("Did you really study?")
                continue

            break

        except ValueError:
            print("Enter a valid duration!")

    date, time = get_datetime()

    file_output = (
        f"{SEPARATOR}\n"
        f"Date: {date}\n"
        f"Time: {time}\n"
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Duration: {duration} minutes\n"
        f"{SEPARATOR}\n"
    )

    with open(FILE_PATH, "a") as file:
        file.write(file_output)

    print("Study session logged successfully!")
    print(SEPARATOR)


def view_session():
    print(SEPARATOR)

    try:
        with open(FILE_PATH, "r") as file:
            content = file.read()

            if content.strip():
                print(content)
            else:
                print("No study sessions have been recorded yet.")

    except FileNotFoundError:
        print("No study sessions have been recorded yet.")

    print(SEPARATOR)


def startup():
    print(
        "=== STUDY SESSION TRACKER ===\n"
        "1. Log a study session\n"
        "2. View study history\n"
        "3. Exit\n"
        f"{SEPARATOR}"
    )

    while True:
        try:
            user_choice = int(input("Select an option (1-3): "))

            if 1 <= user_choice <= 3:
                return user_choice

            print("Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    while True:
        choice = startup()

        if choice == 1:
            log_session()

        elif choice == 2:
            view_session()

        elif choice == 3:
            print(SEPARATOR)
            print("Thank you for using the Study Session Tracker.")
            print("Keep learning!")
            print(SEPARATOR)
            break


if __name__ == "__main__":
    main()