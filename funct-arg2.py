
def status(**kwargs):
    print('\nReport\n')

    for key, value in kwargs.items():
        print(key + ':' + value)

    print('\nEnd Report\n')

status(name='Oki', stat='Ganteng', edu='engineering')

