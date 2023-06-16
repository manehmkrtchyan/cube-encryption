class Cube:
    count_of_not_none_vertexes = 0

    def __init__(self) -> None:
        '''self.cord_number_xyz'''
        self.cord_1_001 = None
        self.cord_2_101 = None
        self.cord_3_100 = None
        self.cord_4_000 = None
        self.cord_5_011 = None
        self.cord_6_111 = None
        self.cord_7_110 = None
        self.cord_8_010 = None
        self.subkey = None

    def rotate_left(self, times):
        for i in range(times):
            (self.cord_1_001, 
             self.cord_2_101,
             self.cord_3_100, 
             self.cord_4_000,
             self.cord_5_011,
             self.cord_6_111,
             self.cord_7_110,
             self.cord_8_010) = (self.cord_2_101,
                                 self.cord_6_111,
                                 self.cord_7_110,
                                 self.cord_3_100,
                                 self.cord_1_001,
                                 self.cord_5_011, 
                                 self.cord_8_010, 
                                 self.cord_4_000)
            
    def rotate_right(self, times):
        for i in range(times):
            (self.cord_1_001, 
             self.cord_2_101,
             self.cord_3_100, 
             self.cord_4_000,
             self.cord_5_011,
             self.cord_6_111,
             self.cord_7_110,
             self.cord_8_010) = (self.cord_5_011,
                                 self.cord_1_001,
                                 self.cord_4_000,
                                 self.cord_8_010,
                                 self.cord_6_111,
                                 self.cord_2_101, 
                                 self.cord_3_100, 
                                 self.cord_7_110)
            
    def rotate_up(self, times):
        for i in range(times):
            (self.cord_1_001, 
             self.cord_2_101,
             self.cord_3_100, 
             self.cord_4_000,
             self.cord_5_011,
             self.cord_6_111,
             self.cord_7_110,
             self.cord_8_010) = (self.cord_4_000,
                                 self.cord_3_100,
                                 self.cord_7_110,
                                 self.cord_8_010,
                                 self.cord_1_001,
                                 self.cord_2_101, 
                                 self.cord_6_111, 
                                 self.cord_5_011)
            
    def rotate_down(self, times):
        for i in range(times):
            (self.cord_1_001, 
             self.cord_2_101,
             self.cord_3_100, 
             self.cord_4_000,
             self.cord_5_011,
             self.cord_6_111,
             self.cord_7_110,
             self.cord_8_010) = (self.cord_5_011,
                                 self.cord_6_111,
                                 self.cord_2_101,
                                 self.cord_1_001,
                                 self.cord_8_010,
                                 self.cord_7_110, 
                                 self.cord_3_100, 
                                 self.cord_4_000)


    def add_value(self, value):
        if self.count_of_not_none_vertexes == 0:
            self.cord_1_001 = value
        if self.count_of_not_none_vertexes == 1:
            self.cord_2_101 = value
        if self.count_of_not_none_vertexes == 2:
            self.cord_3_100 = value
        if self.count_of_not_none_vertexes == 3:
            self.cord_4_000 = value
        if self.count_of_not_none_vertexes == 4:
            self.cord_5_011 = value
        if self.count_of_not_none_vertexes == 5:
            self.cord_6_111 = value
        if self.count_of_not_none_vertexes == 6:
            self.cord_7_110 = value
        if self.count_of_not_none_vertexes == 7:
            self.cord_8_010 = value
        self.count_of_not_none_vertexes += 1

    def get_attributes(obj):
        attributes = {}

        for item in dir(obj):
            if not item.startswith('__') and not callable(getattr(obj, item)):
                attributes[item] = getattr(obj, item)

        return attributes

    def __repr__(self) -> str:
        return str(self.get_attributes())
    
cube = Cube()
