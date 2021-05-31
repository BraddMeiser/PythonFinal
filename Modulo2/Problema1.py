while True:
    n = input("\nIngrese una altura entre 1 y 8: ")
    if n.isdigit():
        n = int(n)
        if n in range(1, 9) :
            for i in range(1, n + 1):
                print(" " * (n - i) + '#' * i)
            break
        else:
            print("\nERROR!! vuelva a ingresar la altura")
    else:
            print("\nComando INVALIDO... vuelva a ingresar la altura")
