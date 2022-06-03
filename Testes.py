Title = input("Enter the name of The plataorm: ")
EMail = input("What email did you used? ")
UserName = input("What username did you used? ")
Password = input("What is the password? ")

if __name__ == "__main__":
    file = open(Title + ".txt", "a")
    file.write("Plataform: " + Title + "\n")
    file.write("E-Mail Aderess: " + EMail + "\n")
    file.write("Username: : " + UserName + "\n")
    file.write("Password: " + UserName + "\n")
    file.write("\n")