'''
Magic find
magic find w pet luck
eyes placed
'''

import random

def getDragType():
    dragRNG = random.randint(1, 25)

    match dragRNG:
        case drag if 0 < drag <= 4:
            return 'Protector'
        case drag if 4 < drag <= 8:
            return 'Strong'
        case drag if 8 < drag <= 12:
            return 'Young'
        case drag if 12 < drag <= 16:
            return 'Old'
        case drag if 16 < drag < 20:
            return 'Wise'
        case drag if 20 < drag < 24:
            return 'Unstable'
        case 25:
            return 'Superior'