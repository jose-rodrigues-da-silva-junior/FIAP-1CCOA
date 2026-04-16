born_date = int(input("Enter your birth year: "))

match born_date:
    case 1995 | 1996 | 1997 | 1998 | 1999:
        print("You are a millennial.")
    case 2000 | 2001 | 2002 | 2003 | 2004 | 2005:
        print("You are a Gen Z.")
    case _:
        print("You are from another generation.")