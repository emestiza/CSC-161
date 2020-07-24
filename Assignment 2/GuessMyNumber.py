#Guess My Number with error checking

def main():
    print("Pick a number between 0-100.")
    High=100
    Low=0
    GuessStatus=False
    Guess=50
    answer=input("My guess is "+str(Guess)+"."+" ")
    while not GuessStatus:
        if answer=="H":
            print("Too high.")
            High=Guess
            Guess=(High+Low)//2
            answer=input("My guess is "+str(Guess)+"."+" ")
        elif answer=="L":
            print("Too low.")
            Low=Guess
            Guess=(High+Low)//2
            answer=input("My guess is "+str(Guess)+"."+" ")
        elif answer=="C":
            print("Guess is correct!")
            GuessStatus=True
        else :
            print ("Invalid response. Try again.")
            print ("Enter too high (H), too low (L), or correct (C).")
            answer=input("My guess is "+str(Guess)+"."+" ")

            
main()
