from socket import getservbyname, getservbyport

class colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ORANGE = '\033[38;5;208m'  
    RESET = '\033[0m'

print(rf'''{colors.ORANGE}
________                _____        ________       ________                      ______                
___  __ \______ __________  /_       ___  __ \_____ ___  __/_____________ ___________  /_ _____ ________
__  /_/ /_  __ \__  ___/_  __/       __  /_/ /_  _ \__  /_  __  ___/_  _ \__  ___/__  __ \_  _ \__  ___/
_  ____/ / /_/ /_  /    / /_         _  _, _/ /  __/_  __/  _  /    /  __/_(__  ) _  / / //  __/_  /    
/_/      \____/ /_/     \__/         /_/ |_|  \___/ /_/     /_/     \___/ /____/  /_/ /_/ \___/ /_/     
                                                                                                        
''')


while True:
    try:
        port = input(f"{colors.YELLOW}port: {colors.ORANGE}")
        
        try:
            response = getservbyport(int(port))
            print(f"{colors.YELLOW}---> {colors.ORANGE}{response}")

        except ValueError:
            try:
                response = getservbyname(port.lower())
                print(f"{colors.YELLOW}---> {colors.ORANGE}{response}")
            except OSError:
                print(f"{colors.RED}port {port} does not exist")

        except OSError:
            print(f"{colors.RED}port {port} does not exist")
    
    except KeyboardInterrupt:
            print("\nQuitting, have fun!"+colors.RESET)
            break

        