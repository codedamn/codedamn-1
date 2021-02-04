
"""
17) modulo operator


eg. r_1 = 3 % 2 # to assign a remainder of 1
"""

r_2 = 5 %    # enter a number to assign a remainder of 2

r_5 = 11 %   # enter a number to assign a remainder of 5

r_3 = 10 %   # enter a number to assign a remainder of 3



def main():
    if r_2 == 2:
        print(f"r_2: passed test, got {r_2} expected 2")
    else:
        print(f"r_2: failed test, got {r_2} expected 2 ")
    if r_5 == 5:
        print(f"r_5: passed test, got {r_5} expected 5")
    else:
        print(f"r_5: failed test, got {r_5} expected 5")
    if r_3 == 3:
        print(f"r_3: passed test, got {r_3} expected 3")
    else:
        print(f"r_3: failed test, got {r_3} expected 3")




if __name__ == "__main__":
    main()
