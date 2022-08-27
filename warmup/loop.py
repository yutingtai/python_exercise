if __name__ == '__main__':
    is_alive = True
    while is_alive:
        answer = input('should I quit?')
        is_alive = answer == 'n'
    print('good bye')
