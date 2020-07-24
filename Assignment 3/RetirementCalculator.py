def main():
    annual_deposit=float(input("Enter annual deposit:"))
    interest_rate=float(input("Enter annual interest rate:"))
    number_of_years=int(input("Enter number of years until retirement:"))
    principle=float(0)
    for i in range(number_of_years):
        principle=float(annual_deposit+principle)
        interest=float(principle*(interest_rate/100))
        principle=interest+principle
        print(round(principle,2))
             

main ()
