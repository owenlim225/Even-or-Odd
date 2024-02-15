while True:
        try:
                char = int(input("Enter an integer: "))
                
                if char % 2 != 0:
                    print("Odd")
                    
                elif char == 0:
                    print("Zero")
                    print()
                    
                else:
                    print("Even")
                    print()
                    
        except ValueError:
                print("Invalid input")
                break
