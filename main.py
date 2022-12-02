# Program to calculate insurance policy for One Stop Insurance Company
# Author: Taylor F. Date: 2022/11/20

import FormatValues as FV

f = open("OSICDef.dat", "r")

NEXT_POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
DISC_ADDIT_CARS = float(f.readline())
COST_LIAB_COV = float(f.readline())
COST_GLASS_COV = float(f.readline())
COST_LOANER_CAR_COV = float(f.readline())
HST_RATE = float(f.readline())
PROFEE_MON_PAY = float(f.readline())

f.close()

while True:

    # Program Inputs
    CustFN = input("Enter the customers first name (End to quit): ").title()
    if CustFN == "End":
        break

    CustLN = input("Enter the customers last name: ").title()
    StAdd = input("Enter the street address: ")
    City = input("Enter the city: ")
    Prov = input("Enter the province: ")
    PostCode = input("Enter the postal code: ")
    PhoneNum = input("Enter the phone number: ")

    AmtCarInsured = int(input("Enter the amount of cars being insured: "))
    ExtLiability = input("Enter if you want liability up to $1,000,000 (Y for Yes or N for No): ").upper()
    OptGlassCov = input("Enter if you want glass coverage (Y or N): ").upper()
    OptLoanerCarCov = input("Enter if you want optional loaner car coverage (Y or N): ").upper()
    FullOrMon = input("Do you wish to pay in full or monthly (F or M): ").upper()

    ReducedRate = BASIC_PREM - (BASIC_PREM * .25)
    ExtraCars = AmtCarInsured - 1
    InsPrem = BASIC_PREM + (ExtraCars * ReducedRate)

    if ExtLiability == "Y":
        ExtLiabCost = AmtCarInsured * 130.00
    else:
        ExtLiabCost = 0

    if OptGlassCov == "Y":
        OptGlassCost = AmtCarInsured * 86.00
    else:
        OptGlassCost = 0

    if OptLoanerCarCov == "Y":
        OptLoanerCost = AmtCarInsured * 58.00
    else:
        OptLoanerCost = 0

    TotExtCost = ExtLiabCost + OptGlassCost + OptLoanerCost

    TotInsurancePrem = InsPrem + TotExtCost

    HST = TotInsurancePrem * HST_RATE

    TotCost = TotInsurancePrem + HST

    MonthlyPay = (PROFEE_MON_PAY + TotCost) / 8

    print("One Stop Insurance Company")
    print()
    print(f"Customer first name: {CustFN:<10s} Customer last name: {CustLN:<10s}")
    print()
    print(f"Street address: {StAdd}  City: {City}    Province: {Prov}")
    print()
    print(f"Postal Code: {PostCode}        Phone number: {PhoneNum}")
    print("=====================================================================")
    print(f"Amount of cars being insured:   {AmtCarInsured}")
    print(f"Extra liability:                {ExtLiability}")
    print(f"Optional glass coverage:        {OptGlassCov}")
    print(f"Optional loaner car coverage:   {OptLoanerCarCov}")
    print("=====================================================================")
    print(f"Insurance premium:      {FV.FDollar2(InsPrem):>9s}")
    print(f"Extra liability cost:   {FV.FDollar2(ExtLiabCost):>9s}")
    print(f"Optional glass cost:    {FV.FDollar2(OptGlassCost):>9s}")
    print(f"Optional loaner cost:   {FV.FDollar2(OptLoanerCost):>9s}")
    print()
    print(f"Total extra costs:       {FV.FDollar2(TotExtCost):>9s}")
    print(f"Total insurance premium: {FV.FDollar2(TotInsurancePrem):>9s}")
    print(f"HST:                     {FV.FDollar2(HST):>9s}")
    if FullOrMon == "M":
        print(f"Monthly payment:         {FV.FDollar2(MonthlyPay):>9s}")
    print(f"Total cost:              {FV.FDollar2(TotCost):>9s}")
    print("=====================================================================")

    f = open("Policies.dat", "a")

    f.write("{}, ".format(str(NEXT_POL_NUM)))
    f.write("{}, ".format(CustFN, CustLN))
    f.write("{}, ".format(StAdd))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(str(AmtCarInsured)))
    f.write("{}, ".format(ExtLiability))
    f.write("{}, ".format(OptGlassCov))
    f.write("{}, ".format(OptLoanerCarCov))
    f.write("{}, ".format(FullOrMon))
    f.write("{}\n".format(float(TotCost)))

    f.close()

    print()
    print("Policy information processed and saved.")
    NEXT_POL_NUM += 1

    f = open("")