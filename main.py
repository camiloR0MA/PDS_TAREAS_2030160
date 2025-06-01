from src.activ1 import activ1

def main():
    actividad = input("Que actividad se vera?? (por ejemplo: 'activ1): ").strip().lower()

    if actividad == 'activ1':
        activ1()
    else:
        print("invalid")

if __name__ == "__main__":
    main()
