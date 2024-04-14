# Credits to where credit's due (Me ofc :) 1yoob)

# Importing the libraries
from socket import getservbyname, getservbyport
from time import sleep
# Colors to beautify the program
class colors:
    MAGENTA = '\033[95m'
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

# Formatting game inputs and outputs
def respond(response):
    print(f'''\033[F{colors.MAGENTA}║ {colors.YELLOW}port: {colors.YELLOW}{port}{(length-9-len(str(port)))*" "}{colors.MAGENTA}║''')
    print(f'''{colors.MAGENTA}║ {colors.ORANGE}{response}{(length-3-len(str(response)))*" "}{colors.MAGENTA}║\n{colors.MAGENTA}╚{(length-2)*'═'}╝{colors.RESET}''')

# The main program
while True:
    length = 40
    # Taking input
    try:
        print(f"{colors.MAGENTA}╔{(length-2)*'═'}╗")
        port = input(f"{colors.MAGENTA}║ {colors.YELLOW}port: {colors.YELLOW}")
        
        # distinguishing input between "str" or "int"
        try:
            response = getservbyport(int(port))
            # Answering with name of port
            respond(response)
        except (ValueError, OverflowError, OSError):
            try:
                #  Answering with number of port
                response = getservbyname(port.lower())
                respond(response)
                # Handling exception where port name doesn't exist
            except (ValueError, OverflowError, OSError):
                response=f"port {port} does not exist"
                respond(response)
            
    # Exiting the program
    except KeyboardInterrupt:
            port = "quit"
            response = "Quitting, have fun!"
            respond(response)
            sleep(2)
            break
