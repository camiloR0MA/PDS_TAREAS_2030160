import sys
from src.activ1 import signals1
from src.activ2 import signals2
from src.activ3 import signals3
from src.activ4 import dac_bits

def main(options):
    if len(options) < 2:
        print("Please provide an option.")
        return

    option = options[1]

    if option == "activ1":
        if len(options) > 2:
            signals1(options[2])
        else:
            print("Please provide the frequency. Example: python main.py activ1 freq")
    elif option == "activ2":
        if len(options) > 2:
            signals2(options[2])
        else:
            print("Please provide the frequency. Example: python main.py activ2 freq")
    elif option == "activ3":
        if len(options) > 4:
            signals3(options[2], options[3], options[4])
        else:
            print("Please provide amplitude, frequency and phase. Example: python main.py activ3 amp freq phas")
    elif option == "activ4":
        if len(options) > 2:
            dac_bits(options[2])
        else:
            print("Please provide the number of bits. Example: python main.py activ4 bits")
    else:
        print("Invalid option. Use 'activ1', 'activ2', 'activ3', 'activ4', etc.")

if __name__ == '__main__':
    main(sys.argv)
