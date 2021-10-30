def number_input(msg='', err_msg='Digite um número válido'):
    while True:
        try:
            return int(input(msg))
        except:
            print(err_msg)
