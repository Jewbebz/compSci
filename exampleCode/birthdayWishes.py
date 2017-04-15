# Birthday Wishes

# positional parameters
def birthday1(name, age):
    print ("Happy birthday,", name, "!", " I hear you're", age, "today.\n")

# parameters with default values
def birthday2(name = "Connor", age = 16):
    print ("Happy birthday,", name, "!", " I hear you're", age, "today.\n")


birthday1("Jackson", 1)
birthday1(1, "Jackson")
birthday1(name = "Jackson", age = 1)
birthday1(age = 1, name = "Jackson")

print()
print ()

birthday2()
birthday2(name = "Kolton")
birthday2(age = 15)
birthday2(name = "Kolton", age = 16)
birthday2("Kolton", 12)

input("\n\nPress the enter key to exit.")



