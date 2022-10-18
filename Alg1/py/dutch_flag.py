from sys import argv
import random


class DutchFlagSort:
    color_calls = 0
    swap_calls = 0
    
    pebbles = []
    each_cnt = 0
    
    def __init__(self, cnt):
        if not cnt % 3 == 0:
            raise ValueError("Count must be divisible to 3")
        self.each_cnt = cnt // 3
        self.pebbles = ['red'] * self.each_cnt + ['white'] * self.each_cnt + ['blue'] * self.each_cnt
        self.shuffle_list()

    def shuffle_list(self):
        list_len = len(self.pebbles)
        for i in range(list_len):
            rnd_i = random.randrange(i+1)
            self.pebbles[i], self.pebbles[rnd_i] = self.pebbles[rnd_i], self.pebbles[i]

        
    def color(self, i):
        self.color_calls += 1
        return self.pebbles[i]

    def swap(self, i, j):
        self.swap_calls += 1
        self.pebbles[i], self.pebbles[j] = self.pebbles[j], self.pebbles[i]
        
    def check_red(self, i):
        if i < self.each_cnt:
            return self.color(i)
        else:
            return ''
        
    def check_white(self, i):
        if i < self.each_cnt*2:
            return self.color(i)
        else:
            return ''
        
    def check_blue(self, i):
        if i < self.each_cnt*3:
            return self.color(i)
        else:
            return ''
        
    def sort(self):
        red_ind = 0
        white_ind = self.each_cnt
        blue_ind = self.each_cnt*2
        
        current_red = self.check_red(red_ind)
        current_white = self.check_white(white_ind)
        current_blue = self.check_blue(blue_ind)
            
        while red_ind < self.each_cnt or white_ind < self.each_cnt*2 or blue_ind < self.each_cnt*3:
            while current_red == 'red':
                red_ind+=1
                current_red = self.check_red(red_ind)
            while current_white == 'white':
                white_ind+=1
                current_white = self.check_white(white_ind)
            while current_blue == 'blue':
                blue_ind+=1
                current_blue = self.check_blue(blue_ind)
                
            if current_blue == 'white' and current_white == 'blue':
                self.swap(blue_ind, white_ind)
                blue_ind += 1
                white_ind += 1
                current_white = self.check_white(white_ind)
                current_blue = self.check_blue(blue_ind)
                
            elif current_blue == 'red' and current_red == 'blue':
                self.swap(blue_ind, red_ind)
                blue_ind += 1
                red_ind += 1
                current_red = self.check_red(red_ind)
                current_blue = self.check_blue(blue_ind)
                
            elif current_white == 'red' and current_red == 'white':
                self.swap(white_ind, red_ind)
                white_ind += 1
                red_ind += 1
                current_red = self.check_red(red_ind)
                current_white = self.check_white(white_ind)

            elif current_white == 'red' and current_red == 'blue' and current_blue == 'white':
                self.swap(white_ind, blue_ind)
                self.swap(red_ind, blue_ind)
                white_ind += 1
                red_ind += 1
                blue_ind += 1
                current_red = self.check_red(red_ind)
                current_white = self.check_white(white_ind)
                current_blue = self.check_blue(blue_ind)

            elif current_white == 'blue' and current_red == 'white' and current_blue == 'red':
                self.swap(white_ind, blue_ind)
                self.swap(red_ind, white_ind)
                white_ind += 1
                red_ind += 1
                blue_ind += 1
                current_red = self.check_red(red_ind)
                current_white = self.check_white(white_ind)
                current_blue = self.check_blue(blue_ind)


if __name__ == "__main__":
    cnt = int(argv[1])
    sorter = DutchFlagSort(cnt)
    print(sorter.pebbles)
    sorter.sort()

    print(sorter.pebbles)
    print("color calls = %s, swap calls = %s" % (sorter.color_calls, sorter.swap_calls))        
