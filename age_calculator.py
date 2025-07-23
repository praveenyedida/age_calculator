from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust if the current month/day is before birth month/day
    if days < 0:
        months -= 1
        days += (birth_date.replace(month=birth_date.month % 12 + 1, day=1) - birth_date.replace(day=1)).days
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    print("📅 Welcome to the Age Calculator!")
    dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")

    try:
        birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(birth_date)
        print(f"\n🎉 You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
