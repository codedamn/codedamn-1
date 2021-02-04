
"""
14) reassign increment inplace

"""


x = 4

x = x   # make x equal 10

new = x   # new equal 8

new   new   # use incrementing to increase new to 10

new   new     # use decrementing to decrease new to 5








def main():
    if x == 10:
        print(f"x: passed test, got {x}, expected 10")
    else:
        print(f"x: failed test, got {x}, expected 10")
    if new == 5:
        print(f"new: passed test, got {new}, expected 5")
    else:
        print(f"new: failed test, got {new}, expected 5")



if __name__ == "__main__":
    main()
