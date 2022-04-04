import os

print(os.listdir("./Schocken/"))

# Regeln


def rules():
    print("\n ****************")
    print("\n ** Die Regeln **")
    print("\n **************** \n")

    with open("./Schocken/rules.txt", "r") as rls:
        print(rls.read())

    print("\n *****************")
    print("\n ** Regeln Ende **")
    print("\n ***************** \n")


rules()
