from os import name

def extract_message(file: str) -> str:
    with open(file, 'rb') as f:
        result = ''
        data = f.read()
        data_list = list(data)             # all bytes
        list_of_bytes = data_list[138::]    # cut header bytes

        # list of tuples with pixels (1 pixel = 4 bytes)
        list_of_pixels = []
        for x in range(0,len(list_of_bytes),4):
            new_pixel = [list_of_bytes[x],list_of_bytes[x+1], list_of_bytes[x+2], list_of_bytes[x+3]]
            list_of_pixels.append(tuple(new_pixel))
        
        # Iterating through every next pair of pixels
        for z in range(0,len(list_of_pixels)-1, 2):
            paired_bits = []
            result_bit = ''                                   # bits from pair of pixels
            for i in range(len(list_of_pixels[z])):
                paired_bits.append(bin(list_of_pixels[z][i]))
            for i in range(len(list_of_pixels[z+1])):
                paired_bits.append(bin(list_of_pixels[z+1][i]))

            for x in range(len(paired_bits)):                  # bit made from LSB of 8 bytes from pair of pixels 
                result_bit += paired_bits[x][-1]

            ascii_int = int(result_bit,2)                   #result bit converted to intege

            if ascii_int >= 32 and ascii_int <= 126:
                letter = chr(ascii_int)              #letter from ASCII asociated with int
                result += letter
                if "EOF" in result:
                    return result


