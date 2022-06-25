MORE50 = '<= 50%'
LESS50 = '> 50%'
SOLD_AUT = 'sold-out'


def places_left(even_seats, participants_number):
    if participants_number != 0:
        if even_seats/participants_number == 1:
            result = SOLD_AUT
        elif even_seats/participants_number <= 0.5:
            result = MORE50
        else:
            result = LESS50
        return result
    return f'{participants_number} = 0'
