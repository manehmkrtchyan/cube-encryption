from cube import Cube
import random
class Text:
    def __init__(self, file_path) -> None:
        self.cube_list = []
        buffer = []

        def is_buffer_full(buff):
            return len(buff) == 8
        
        with open(file_path, 'r') as f:
            cube = Cube()
            string = f.read()
            for i in string:
                if not is_buffer_full(buffer):
                    buffer.append(i)
                    cube.add_value(i)
                    if len(string) - 1 < cube.count_of_not_none_vertexes: 
                        self.cube_list.append(cube)
                else:
                    self.cube_list.append(cube)
                    buffer = []
                    string = string[8:]
                    cube = Cube()
                    buffer.append(i)
                    cube.add_value(i)

    def key_parser(key):
        return key.split(':')
    
    def generate_random_key(self):
        directions = ['l', 'r', 'u', 'd']
        key_parts = []
        for _ in range(len(self.cube_list)):
            part = ''
            while len(part) < 10:
                direction = random.choice(directions)
                count = random.randint(1, 9)
                part += direction + str(count) + ','
            key_parts.append(part)
        result_key = ':'.join(key_parts)
        self.key = result_key
        return result_key

    def convert_to_str(self):
        result = ''
        for cube in self.cube_list:
            if cube.cord_1_001 is not None:
                result += cube.cord_1_001
            if cube.cord_2_101 is not None:
                result += cube.cord_2_101
            if cube.cord_3_100 is not None:
                result += cube.cord_3_100 
            if cube.cord_4_000 is not None:
                result += cube.cord_4_000
            if cube.cord_5_011 is not None:
                result += cube.cord_5_011
            if cube.cord_6_111 is not None:
                result += cube.cord_6_111
            if cube.cord_7_110 is not None:
                result += cube.cord_7_110
            if cube.cord_8_010 is not None:
                result += cube.cord_8_010
        return result
    
    def encode(self):
        self.key = self.generate_random_key()
        for idx,k in enumerate(self.key.split(':')):
            self.cube_list[idx].subkey = k
        for cube in self.cube_list:
            command_list = cube.subkey.split(',')
            for command in command_list:
                if str(command).startswith('l'):
                    cube.rotate_left(int(command[-1]))
                if str(command).startswith('r'):
                    cube.rotate_right(int(command[-1]))
                if str(command).startswith('u'):
                    cube.rotate_up(int(command[-1]))
                if str(command).startswith('d'):
                    cube.rotate_down(int(command[-1]))
                if str(command) == '' or ' ':
                    continue
        with open('encoded_file.txt', 'w+') as encoded_file:
            encoded_file.write(self.convert_to_str())

    def decode(self, file_with_encoded_text):
        new_text = Text(file_with_encoded_text)

        key = self.key
        for idx, k in enumerate(key.split(':')):
            self.cube_list[idx].subkey = k

        for idx, cube in enumerate(self.cube_list):
            command_list = cube.subkey.split(',')[::-1]
            for command in command_list:
                if str(command).startswith('l'):
                    new_text.cube_list[idx].rotate_right(int(command[-1]))
                elif str(command).startswith('r'):
                    new_text.cube_list[idx].rotate_left(int(command[-1]))
                elif str(command).startswith('u'):
                    new_text.cube_list[idx].rotate_down(int(command[-1]))
                elif str(command).startswith('d'):
                    new_text.cube_list[idx].rotate_up(int(command[-1]))
                elif str(command) == '' or ' ':
                    continue

        with open('decoded_file.txt', 'w+') as decoded_file:
            decoded_file.write(new_text.convert_to_str())


    def __iter__(self):
        return iter(self.cube_list)

    def __next__(self):
        return self.cube_list.__iter__().__next__()
                    
text = Text('initial_file.txt')

#print(text.generate_random_key())
text.encode()
(text.decode('encoded_file.txt'))
#print(text.cube_list[0].subkey)

