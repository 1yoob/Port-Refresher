# Credits to where credit's due (Me ofc :) 1yoob)

# Importing the libraries
from socket import getservbyname, getservbyport

# Colors to beautify the program
class colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ORANGE = '\033[38;5;208m'  
    RESET = '\033[0m'

# Printing the Banner
print(rf'''{colors.ORANGE}
________                _____        ________       ________                      ______                
___  __ \______ __________  /_       ___  __ \_____ ___  __/_____________ ___________  /_ _____ ________
__  /_/ /_  __ \__  ___/_  __/       __  /_/ /_  _ \__  /_  __  ___/_  _ \__  ___/__  __ \_  _ \__  ___/
_  ____/ / /_/ /_  /    / /_         _  _, _/ /  __/_  __/  _  /    /  __/_(__  ) _  / / //  __/_  /    
/_/      \____/ /_/     \__/         /_/ |_|  \___/ /_/     /_/     \___/ /____/  /_/ /_/ \___/ /_/     
                                                                                                        
''')

# The main program
while True:
    # Taking input
    try:
        port = input(f"{colors.YELLOW}port: {colors.ORANGE}")
        
        # distinguishing input between "str" or "int"
        try:
            response = getservbyport(int(port))
            # Answering with name of port
            print(f"{colors.YELLOW}---> {colors.ORANGE}{response}")

        except ValueError:
            try:
                #  Answering with number of port
                response = getservbyname(port.lower())
                print(f"{colors.YELLOW}---> {colors.ORANGE}{response}")
                # Handling exception where port name doesn't exist
            except OSError:
                print(f"{colors.RED}port {port} does not exist")

        # Handling exception where port number doesn't exist
        except OSError:
            print(f"{colors.RED}port {port} does not exist")
            
    # Exiting the program
    except KeyboardInterrupt:
            print("\nQuitting, have fun!"+colors.RESET)
            break        
