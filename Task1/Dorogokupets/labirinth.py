import random

class DoorV:
    '''случайный выбор позиции вертикальных дверей'''
    def get_v_door_pos(self):
        position = random.randint(0, 1)
        if position == 1:
            return '   '
        elif position == 0:
            return ' | '
    
class DoorH:
    '''случайный выбор позиции горизонтальных дверей'''
    def get_h_door_pos(self):
        position = random.randint(0, 1)
        if position == 1:
            return '-  -'
        elif position == 0:
            return '----'

v = DoorV()
h = DoorH()

print(f'|---  ---|--------|--------|--------|')
print(f'|   01  {v.get_v_door_pos()}  02  {v.get_v_door_pos()}  03  {v.get_v_door_pos()}  04   |')
print(f'|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|')
print(f'|   05  {v.get_v_door_pos()}  06  {v.get_v_door_pos()}  07  {v.get_v_door_pos()}  08   |')
print(f'|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|')
print(f'|   09  {v.get_v_door_pos()}  10  {v.get_v_door_pos()}  11  {v.get_v_door_pos()}  12   |')
print(f'|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|--{h.get_h_door_pos()}--|')
print(f'|   13  {v.get_v_door_pos()}  14  {v.get_v_door_pos()}  15  {v.get_v_door_pos()}  16   |')
print(f'|--------|--------|--------|---  ---|')

