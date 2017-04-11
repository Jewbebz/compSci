#Geek Translator
#Demonstrates using dictionaries

geek={"404": "clueless. From the web error message 404, meaning page not found.",
      "Googling": "searching the Internet for background information on a person."
      "": ""}

choice=None
while choice != "0":
    print("""
    Geek translator

    0 - Quit
    1 -
    2 -
    3 -
    4 -
    5 - Print the dictionary terms
    """)

    choice = input("Choice: ")
    choice = int(choice)
    print

    if choice == 0:
        print ("Good-bye.")
    elif choice == 1:
        term = input("What term do you want me to translate?")
        if term in geek:
            definition = geek[term]
    elif choice == 2:
    elif choice == 3:
    elif choice == 4:
    elif choice == 5:
