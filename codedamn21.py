
"""
21) slicing with step


"""



letters = "abcdefghijk"


every_other =           # assign every other letter from letters

every_third =           #  assign every 3rd letter from letters

first_3_every_other =   # assign the three letter everyother 1 eg. ace 










def main():
    if every_other == "acegik":
        print(f"every_other: passed test, got {every_other} expected acegik")
    else:
        print(f"every_other: failed test, got {every_other} expected acegik")
    if every_third == "adgj":
        print(f"every_third: passed test, got {every_third} expected acegik")
    else:
        print(f"every_other: failed test, got {every_third} expected acegik")
    if first_3_every_other == "ace":
        print(f"every_other: passed test, got {first_3_every_other} expected acegik")
    else:
        print(f"first_3_every_other: failed test, got {first_3_every_other} expected acegik")



if __name__ == "__main__":
    main()
