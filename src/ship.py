class Ship():
    def __init__(self, list, x1, y1, x2, y2):
        self.list_ship = list
        self.cnt_alive = len(list)
        self.head_x = x1
        self.head_y = y1
        self.tail_x = x2
        self.tail_y = y2