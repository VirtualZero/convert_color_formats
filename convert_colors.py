def rgb2hex():
    
    try:
        def check_length(x):
            if len(str(x)) > 3:
                return "\nInvalid number of characters.\n"
        
            else:
                return False
    
        try:
            r = int(input("\nEnter the RED value: "))
            r_error = check_length(r)
            
            if r_error != False:
                print(r_error)
                return "Input Error"
            
        except ValueError:
            print("\nInput must be digits.\n")
            return "Input Error"
            
        try:
            g = int(input("Enter the GREEN value: "))
            g_error = check_length(g)
            
            if g_error != False:
                print(g_error)
                return "Input Error"
        
        except ValueError:
            print("\nInput must be digits.\n")
            return "Input Error"
        
        try:
            b = int(input("Enter the BLUE value: "))
            b_error = check_length(b)
            
            if b_error != False:
                print(b_error)
                return "Input Error"
        
        except ValueError:
            print("\nInput must be digits.\n")
            return "Input Error"
            
        hex_value = f"#{r:02x}{g:02x}{b:02x}"
        print(f"\nThe hex value for ({r}, {g}, {b}) is {hex_value}.\n")
        greeting()

    except KeyboardInterrupt:
        print("\nGoodbye.\n")
        exit()    

def hex2rgb():
    
    try:
        hex_input = input("\nEnter a hex color value: ").lower().lstrip('#')
        
        if not hex_input:
            print("\nNo input detected.\n")
            return "Input Error"
            
        if len(hex_input) != 6:
            print("\nInvalid number of characters.\n")
            return "Input Error"
            
        hexidecimal_letters = ['a', 'b', 'c', 'd', 'e', 'f']
        hexidecimal_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            
        for character in hex_input:
            if character not in hexidecimal_digits \
            and character not in hexidecimal_letters:
                print(f"\n{character} is not a valid hexidecimal character.\n")
                return "Input Error"
            
        rgb_value = tuple(int(hex_input[i:i+2], 16) for i in (0, 2 ,4))
        print(f"\nThe RGB value for #{hex_input} is {rgb_value}.\n")
        greeting()

    except KeyboardInterrupt:
        print("\nGoodbye.\n")
        exit()

def greeting():
    
    try:
        try:
            choice = int(input(("Enter your choice:\n"
                                "1) Convert hex to RGB\n"
                                "2) Convert RGB to hex\n"
                                "3) Exit\n"
                                "Your choice: ")))
        
        except ValueError:
            print("\nInput must be a digit.\n")
            return "Input Error"
        
        if 1 > choice or choice > 3:
            print("\nInvalid choice.\n")
            return "Input Error"

        if choice == 1:
            hex_error = hex2rgb()
            while hex_error == "Input Error":
                hex_error = hex2rgb()
            
        if choice == 2:
            rgb_error = rgb2hex()
            while rgb_error == "Input Error":
                rgb_error = rgb2hex()
            
        if choice == 3:
            print("\nGoodbye.\n")
            exit(0)

    except KeyboardInterrupt:
        print("\nGoodbye.\n")
        exit()

def main():
    
    print("\nWelcome!\n")
    greeting()

if __name__ == "__main__":
    main()
