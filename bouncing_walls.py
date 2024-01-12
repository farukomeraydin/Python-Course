height = int(input('Enter height:'))
width = int(input('Enter width:'))
pos = 0
direction = 1

for _ in range(height):
    print('|' + ' ' * pos + '*' + ' ' * (width - pos - 1) + '|')
    if pos == width - 1:
        direction = -1
    elif pos == 0:
        direction = 1
    
    pos += direction
