

"""
22) input function

"""

# use an input function to ask for someones name and run srcipt


name = 


print(f"Hi {name} nice to meet you")






def main():
    if len(name) > 0 and name.isalpha():
        print("name: passed test")
    else:
        print("name: failed test\nplease try again")



if __name__ == "__main__":
    main()
