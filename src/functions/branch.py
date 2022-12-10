import requests

def get_branch(message):

    # База данных всех адресов учебных центров
    address = {'москва': 'Красная Пресня 31',
               'самара': 'Невский проспект 114',
               'екатеринбург': 'Московская 50',
               'киров': 'Октябрьский проспект 111',
               'сургут': 'Проспект мира 16'}

    locality = message.lower()
    answer_address = address.get(locality, '-')
    if (answer_address == '-'):
        return ('В данном городе нет филилала')
    else:
        return ('В городе ' + message[0].upper() + message[1:len(message)] + ' филиал находится по адресу: ' + answer_address)