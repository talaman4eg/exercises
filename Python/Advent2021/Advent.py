#!/usr/bin/python3

import pprint
import re
import functools
import datetime
import heapq
import numpy
import math

class Advent:
    

    def solve(self):
        return self.d14_2()
    
    
    #day 15
    def d15_1(self):
        data = self.read_input('D14.txt')
        risk_matrix = [[int(x) for x in line.strip().split()] for line in data]
        routes = [[risk_matrix[0][0], (0, 0)]]
        end_point = (len(risk_matrix) - 1, len(risk_matrix[0]) - 1)
        
        class D15_vertex:
            x = 0
            y = 0
            visited = False
            distance = math.inf
            value = 0
            
        
        
        
    
    # day 14
    def d14_2(self):
        data = self.read_input('D14.txt')
        initial = data[0].strip()
        transition = {}
        self.d14_p_stat = {}
        for p in initial:
            if not p in self.d14_p_stat:
                self.d14_p_stat[p] = 0
            self.d14_p_stat[p] += 1
            
        
        for i in range(2, len(data)):
            parts = data[i].strip().split(' -> ')
            transition[parts[0]] = parts[1]
            
        current = initial[:]
        
        for i in range(len(initial) - 1):
            current_block = initial[i]+initial[i+1]
            print('Processing %s (%s) at %s' % (current_block, i, self.start_timer()))
            self.d14_insert_polymers(transition, current_block, 1)
            print('Starting letter %s completed in %s' % (current_block, self.get_timer()[0]))
        
        return max(self.d14_p_stat.values()) - min(self.d14_p_stat.values())
    
    d14_max_steps = 40
    d14_p_stat = {}
    d14_p_stat_cache = {}
    
    def d14_merge_stat(self, stat1, stat2):
        res = {}
        for pol in set(list(stat1.keys()) + list(stat2.keys())):
            res[pol] = (0 if not pol in stat1 else stat1[pol]) + (0 if not pol in stat2 else stat2[pol])
        return res
    
    def d14_insert_polymers(self, polymers, current_pol, depth = 1):
        cur_pol_stat = {}
        if depth > self.d14_max_steps:
            return {}
        block = current_pol[0]+current_pol[1]
        if not depth in self.d14_p_stat_cache:
            self.d14_p_stat_cache[depth] = {}
        if block in self.d14_p_stat_cache[depth]:
            print('Found cached results for block %s on depth %s. Time eplaced %s' % (current_pol, depth, self.get_timer()[0]))
            self.d14_p_stat = self.d14_merge_stat(self.d14_p_stat, self.d14_p_stat_cache[depth][block])
            return self.d14_p_stat_cache[depth][block]    

        if block in polymers:
            pol_to_add = polymers[block]
            if not pol_to_add in self.d14_p_stat:
                self.d14_p_stat[pol_to_add] = 0
            self.d14_p_stat[pol_to_add] += 1
            if not pol_to_add in cur_pol_stat:
                cur_pol_stat[pol_to_add] = 0
            cur_pol_stat[pol_to_add] += 1
            cur_pol_stat = self.d14_merge_stat(cur_pol_stat, self.d14_insert_polymers(polymers, current_pol[0] + pol_to_add, depth + 1))
            cur_pol_stat = self.d14_merge_stat(cur_pol_stat, self.d14_insert_polymers(polymers, pol_to_add + current_pol[1:], depth + 1))
            self.d14_p_stat_cache[depth][block] = cur_pol_stat
            return cur_pol_stat
            
        
        
    
    def d14_1(self):
        data = self.read_input('D14.txt')
        initial = data[0].strip()
        polymers = {}
        p_stat = {}
        for p in initial:
            if not p in p_stat:
                p_stat[p] = 0
            p_stat[p] += 1
            
        
        for i in range(2, len(data)):
            parts = data[i].strip().split(' -> ')
            polymers[parts[0]] = parts[1]
            
        current = initial
        cur_len = len(current)
        steps = 10
        for x in range(steps):
            print('Starting step %d at %s' % (x, self.start_timer()))
            i = 0
            while True:
                p = current[i] + current[i+1]
                if p in polymers:
                    current = current[:i+1]+polymers[p]+current[i+1:]
                    if not polymers[p] in p_stat:
                        p_stat[polymers[p]] = 0
                    p_stat[polymers[p]] += 1
                    i+=1
                
                
                i += 1
                if i >= len(current) - 1:
                    break

            timer = self.get_timer()
            print('Finished step %d in %s. Data len %d. Time %s' % (x, timer[0], len(current), timer[2]))
            self.start_timer()
                
        return max(p_stat.values()) - min(p_stat.values())
            
        

    # day 13
    def d13_1(self):
        data = self.read_input('D13.txt')
        matrix = {}
        folds = []
        fold_section = False
        for line in data:
            if line.strip() == '':
                fold_section = True
                continue
            if fold_section:
                words = line.strip().split(' ')
                folds.append(tuple(words[2].split('=')))
            else:
                (x, y) = line.strip().split(',')
                if not int(y) in matrix.keys():
                    matrix[int(y)] = []
                matrix[int(y)].append(int(x))
        
        cnt = sum([len(matrix[row]) for row in matrix])
        for fold in folds:
        #fold = folds[0]
            if fold[0] == 'x':
                matrix = self.d13_fold_x(matrix, int(fold[1]))
            elif fold[0] == 'y':
                matrix = self.d13_fold_y(matrix, int(fold[1]))
            
        max_x = max([max(matrix[row]) for row in matrix])
        out = {}
        for row in range(max(matrix.keys())+1):
            out[row] = []
            for col in range(max_x + 1):
                if row in matrix and col in matrix[row]:
                    out[row].append('#')
                else:
                    out[row].append('.')
            print(''.join(out[row]))
        
        return cnt
        
    def d13_fold_x(self, matrix, x):
        new_matrix = {}
        for y, row in matrix.items():
            new_matrix[y] = []
            for dot in row:
                if dot < x:
                    new_dot = dot
                elif dot > x:
                    new_dot = (x - (dot - x))
                if not new_dot in new_matrix[y]:
                    new_matrix[y].append(new_dot)
        return new_matrix
    
    def d13_fold_y(self, matrix, y):
        new_matrix = {}
        for row_num in matrix:
            if row_num < y:
                new_row_num = row_num
            elif row_num > y:
                new_row_num = y - (row_num - y)
            if not new_row_num in new_matrix:
                new_matrix[new_row_num] = []
            new_matrix[new_row_num] = list(set(new_matrix[new_row_num] + matrix[row_num]))
        return new_matrix
    
    # day 12
    def d12_2(self):
        data = self.read_input('D12.txt')
        relations = {}
        for line in data:
            (p1, p2) = line.strip().split('-')
            if p1 == 'start' or p2 == 'end':
                if not p1 in relations.keys():
                    relations[p1] = []
                if not p2 in relations[p1]:
                    relations[p1].append(p2)
            elif p2 == 'start' or p1 == 'end':
                if not p2 in relations.keys():
                    relations[p2] = []
                if not p1 in relations[p2]:
                    relations[p2].append(p1)
            else:
                if not p1 in relations.keys():
                    relations[p1] = []
                if not p2 in relations.keys():
                    relations[p2] = []
                if not p2 in relations[p1]:
                    relations[p1].append(p2)
                if not p1 in relations[p2]:
                    relations[p2].append(p1)

        routes = []
        for p in relations['start']:
            routes.append([0, 'start', p])
        fin = False
        while not fin:
            start = datetime.datetime.now()
            new_routes = []
            fin = True
            for r in routes:
                route = r[:]
                if route[-1] == 'end':
                    new_routes.append(route)
                    continue
                if route[-1] in relations:
                    for p in relations[route[-1]]:
                        new_route = self.d12_process_rel(p, route)
                        if len(new_route) > 1:
                            new_routes.append(new_route)
                            fin = False
            end = datetime.datetime.now()
            print('Iter in '+str(end-start))
                            
            routes = new_routes
            print(len(routes))
                
        res = 0
        for route in routes:
            if route[-1] == 'end':
                res += 1
        
        return res

    def d12_process_rel(self, p, route):
        res = []
        point = p
        
        if not point.lower() == point:
            res = route[:]
            res.append(point)
        else:
            if not point in route:
                res = route[:]
                res.append(point)
            elif route[0] == 0:
                res = route[:]
                res[0] = 1
                res.append(point)
            else:
                pass
        
        return res

    def d12_1(self):
        data = self.read_input('D12.txt')
        relations = [tuple(line.strip().split('-')) for line in data]
        routes = []
        for rel in relations:
            if rel[0] == 'start':
                routes.append([rel[0], rel[1]])
            if rel[1] == 'start':
                routes.append([rel[1], rel[0]])
        fin = False
        ri = 0
        while not fin:
            new_routes = []
            for r in routes:
                route = r[:]
                if route[-1] == 'end':
                    new_routes.append(route)
                    continue
                for rel in relations:
                    if rel[0] == 'start' or rel[1] == 'start':
                        continue
                    new_route = []
                    if rel[0] == route[-1]:
                        new_route = self.d12_append_point_to_route(rel[1], route)
                    if rel[1] == route[-1]:
                        new_route = self.d12_append_point_to_route(rel[0], route)
                    if len(new_route) > 0 and not new_route in new_routes:
                        new_routes.append(new_route)
                            
            if routes == new_routes:
                fin = True
            else:
                routes = new_routes
                
        res = 0
        for route in routes:
            if route[-1] == 'end':
                res += 1
        
        return res
                        
    def d12_append_point_to_route(self, point, route):
        res = []
        if (point.lower() == point and point in route) or route[-1] == 'end':
            pass
        else:
            res = route[:]
            res.append(point)
        return res
            
    
    # day 11
    def d11_2(self):
        data = self.read_input('D11.txt')
        energy_levels = [[int(x) for x in line.strip()] for line in data]
        flash_count = 0
        steps_count = 1000
        for step in range(steps_count):
            for row in range(len(energy_levels)):
                for col in range(len(energy_levels[0])):
                    energy_levels[row][col] += 1
                    if energy_levels[row][col] == 10:
                        flash_count += self.d11_flash(energy_levels, row, col)
            fin = True
            for row in range(len(energy_levels)):
                for col in range(len(energy_levels[0])):
                    if energy_levels[row][col] > 9:
                        energy_levels[row][col] = 0
                    else:
                        fin = False
            if fin:
                break
        return step+1
    
    def d11_1(self):
        data = self.read_input('D11.txt')
        energy_levels = [[int(x) for x in line.strip()] for line in data]
        flash_count = 0
        steps_count = 100
        for step in range(steps_count):
            for row in range(len(energy_levels)):
                for col in range(len(energy_levels[0])):
                    energy_levels[row][col] += 1
                    if energy_levels[row][col] == 10:
                        flash_count += self.d11_flash(energy_levels, row, col)
            for row in range(len(energy_levels)):
                for col in range(len(energy_levels[0])):
                    if energy_levels[row][col] > 9:
                        energy_levels[row][col] = 0
        return flash_count
                    
                        

    def d11_flash(self, levels, row, col):
        charge = [(row-1, col-1), (row-1, col), (row-1, col+1),
                    (row, col-1), (row, col+1),
                    (row+1, col-1), (row+1, col), (row+1, col+1)]
        flash_count = 1
        for (i, j) in charge:
            if i < 0 or i >= len(levels) or j < 0 or j >= len(levels[0]):
                continue
            else:
                levels[i][j] += 1
                if levels[i][j] == 10:
                    flash_count += self.d11_flash(levels, i, j)
        return flash_count
                
    
    # day 10
    def d10_2(self):
        data = self.read_input('D10.txt')
        scores = []
        for line in data:
            if self.d10_check_line(line) > 0:
                continue
            else:
                scores.append(self.d10_score_line(line))
        #pprint.pprint(scores)
        return sorted(scores)[int(len(scores)/2)]
                

    def d10_score_line(self, line):
        stack = []
        pairs = [
            ('(', '[', '{', '<'),
            (')', ']', '}', '>'),
            (1, 2, 3, 4),
            ]
        for symb in line:
            if symb in pairs[0]:
                stack.append(symb)
            elif symb in pairs[1]:
                opening = stack.pop()
                if not pairs[1].index(symb) == pairs[0].index(opening):
                    return 0
        res = 0
        print(stack)
        for symb in stack[::-1]:
            score = pairs[2][pairs[0].index(symb)]
            res = res * 5 + score
        print(res)
        return res
    
    def d10_1(self):
        data = self.read_input('D10.txt')
        res = 0
        for line in data:
            res += self.d10_check_line(line) 
        return res  
    
    def d10_check_line(self, line):
        stack = []
        pairs = [
            ('(', '[', '{', '<'),
            (')', ']', '}', '>'),
            (3, 57, 1197, 25137),
            ]
        for symb in line:
            if symb in pairs[0]:
                stack.append(symb)
            elif symb in pairs[1]:
                opening = stack.pop()
                if not pairs[1].index(symb) == pairs[0].index(opening):
                    return  pairs[2][pairs[1].index(symb)]
                
        return 0
            
        
    
    # day 9
    def d9_2(self):
        data = self.read_input('D9.txt')
        basins = []
        matrix = [[int(x) for x in row.strip()] for row in data]
        low_points = self.d9_find_low_points(matrix)
        for lp in low_points:
            basin = self.d9_find_basin(matrix, lp[1], lp[2])
            basins.append(len(basin))
        
        res = sorted(basins, reverse=True)[0:3]
        
        #pprint.pprint(res)
            
        return functools.reduce(lambda x, y: x*y, res)
                
        
        
    def d9_find_basin(self, matrix, i, j, basin = None):
        if basin == None:
            basin = [(i, j)]
        else:
            basin.append((i, j))
        col_cnt = len(matrix[0])
        row_cnt = len(matrix)
        if i > 0 and matrix[i-1][j] < 9 and not (i-1, j) in basin:
            self.d9_find_basin(matrix, i-1, j, basin)
        if i < row_cnt - 1 and matrix[i+1][j] < 9 and not (i+1, j) in basin:
            self.d9_find_basin(matrix, i+1, j, basin)
        if j > 0 and matrix[i][j-1] < 9 and not (i, j-1) in basin:
            self.d9_find_basin(matrix, i, j-1, basin)
        if j < col_cnt - 1 and matrix[i][j+1]  < 9 and not (i, j+1) in basin:
            self.d9_find_basin(matrix, i, j+1, basin)
        return basin
        
    
    def d9_find_low_points(self, matrix):
        low_points = []
        col_cnt = len(matrix[0])
        row_cnt = len(matrix)
        
        for i in range(row_cnt):
            for j in range(col_cnt):
                adj = []
                if i > 0 and matrix[i-1][j] <= matrix[i][j]:
                    continue
                if i < row_cnt - 1 and matrix[i+1][j] <= matrix[i][j]:
                    continue
                if j > 0 and matrix[i][j-1] <= matrix[i][j]:
                    continue
                if j < col_cnt - 1 and matrix[i][j+1] <= matrix[i][j]:
                    continue
                low_points.append((matrix[i][j], i, j))
        return low_points
        
    
    def d9_1(self):
        data = self.read_input('D9.txt')

        risk_lvl = 0
        
        matrix = [[int(x) for x in row.strip()] for row in data]
        
        low_points = self.d9_find_low_points(matrix)
        for lp in low_points:
            risk_lvl += lp[0] + 1
                
        return risk_lvl
        
    
    # day 8
    def d8_1(self):
        data = self.read_input('D8.txt')
        cnt = 0
        for line in data:
            parts = line.strip().split('|')
            cnt += len(re.findall(r'(?<=\s)([abcdefg]{2,4}|[abcdefg]{7})(?=\s|$)', parts[1]))
            
        return cnt
    
    
    
    def d8_decode(self, mapping, number):
        print(mapping, number)
        res = []
        one = ''
        four = ''
        seven = ''
        
        for d in mapping:
            len_d = len(d)
            if len_d == 2:
                one = d
            elif len_d == 4:
                four = d
            elif len_d == 3:
                seven = d
        in_five = list(set(four) - set(seven))
        
        print(one, seven, four, in_five)

        for d in number:
            digit = ''
            len_d = len(d)
            if len_d == 2:
                digit = 1
            elif len_d == 3:
                digit = 7
            elif len_d == 4:
                digit = 4
            elif len_d == 5: # 2, 3, 5, 
                if one[0] in d and one[1] in d:
                    digit = 3
                elif in_five[0] in d and in_five[1] in d:
                    digit = 5
                else:
                    digit = 2
            elif len_d == 6: #0, 9, 6
                if one[0] in d and one[1] in d:
                    if in_five[0] in d and in_five[1] in d:
                        digit = 9
                    else:
                        digit = 0
                else:
                    digit = 6
                
            elif len_d == 7:
                digit = 8
            res.append(digit)
            
        print(res)
        return int(''.join(map(str, res)))
        
        
    def d8_2(self):
        data = self.read_input('D8.txt')
        res = 0

        for line in data:
            parts = line.strip().split('|')
            
            num = self.d8_decode(parts[0].split(), parts[1].split())
            res += num
            
        
        
        
        return res

    # day 7
    def d7_calc_fuel_cost(self, positions, target):
        total_cost = 0
        for k, v in positions.items():
            #total_cost += abs(target - k) * v # part1
            total_cost += sum(range(abs(target - k) + 1)) * v # part2
        return total_cost

    def d7_1(self):
        data = self.read_input('D7.txt')
        positions = {}
        total = 0
        max = min = False
        for pos in map(int, data[0].strip().split(',')):
            if not pos in positions:
                positions[pos] = 0
            positions[pos] += 1
            if max == False or max < pos:
                max = pos
            if min == False or min > pos:
                min = pos
            
        min_cost = False
        for target in range(min, max):
            cost = self.d7_calc_fuel_cost(positions, target)
            if min_cost == False or min_cost > cost:
                min_cost = cost
            #print(target, cost)
        return min_cost

    # day 6
    def d6_1(self):
        data = self.read_input('D6.txt')
        ages = {}
        for age in map(int, data[0].strip().split(',')):
            if not age in ages.keys():
                ages[age] = 0
            ages[age] += 1
        #term = 80
        term = 256 # part 2
        for day in range(term):
            new_ages = {}
            for i in range(9):
                if not i in ages.keys():
                    ages[i] = 0
                if i == 0:
                    new_ages[8] = ages[0]
                    new_ages[6] = ages[0]
                else:
                    if not i-1 in new_ages:
                        new_ages[i-1] = 0
                    new_ages[i-1] += ages[i]
            ages = new_ages
                
            
            #print(day, ages)
                    
        return sum(ages.values())
                

    # Day 5
    def d5_1(self):
        data = self.read_input('D5.txt')
        points = {}
        for line in data:
            parts = line.strip().split()
            (x1, y1) = map(int, parts[0].split(','))
            (x2, y2) = map(int, parts[2].split(','))
            if x1 == x2:
                if not x1 in points.keys():
                    points[x1] = {}
                rng = range(y1, y2+1)
                if y2 < y1:
                    rng = range(y2, y1+1)

                for i in rng:
                    if not i in points[x1].keys():
                        points[x1][i] = 1
                    else:
                        points[x1][i] += 1 
                      
            if y1 == y2:
                rng = range(x1, x2+1)
                if x2 < x1:
                    rng = range(x2, x1+1)
                for i in rng:
                    if not i in points.keys():
                        points[i] = {}
                    if not y1 in points[i].keys():
                        points[i][y1] = 1
                    else:
                        points[i][y1] += 1

        num_points = 0;
        for num_row, row in points.items():
            for col_num, num in row.items():
                if num > 1:
                    num_points += 1

        return num_points


    def d5_mark_point(self, points, x, y):
        if not x in points.keys():
            points[x] = {}
        if not y in points[x].keys():
            points[x][y] = 1
        else:
            points[x][y] += 1
        
        
        
    def d5_2(self):
        data = self.read_input('D5.txt')
        points = {}
        for line in data:
            parts = line.strip().split()
            (x1, y1) = map(int, parts[0].split(','))
            (x2, y2) = map(int, parts[2].split(','))
            if x1 == x2:
                rng = range(min(y1, y2), max(y1, y2)+1)

                for i in rng:
                    self.d5_mark_point(points, x1, i)
                      
            elif y1 == y2:
                rng = range(min(x1, x2), max(x1, x2)+1)
                for i in rng:
                    self.d5_mark_point(points, i, y1)

            else:
                stepY = 1 if y1 < y2 else -1
                rngY = range(y1, y2+stepY, stepY)
                stepX = 1 if x1 < x2 else -1
                rngX = range(x1, x2+stepX, stepX)
                if len(rngX) == len(rngY):
                    for i in range(len(rngY)):
                        x = rngX[i]
                        y = rngY[i]
                        self.d5_mark_point(points, rngX[i], rngY[i])
                else:
                    print('non diag:', x1, y1, x2, y2)


        #pp = pprint.PrettyPrinter(indent = 4)
        #pp.pprint(points)

        num_points = 0;
        for num_row, row in points.items():
            for col_num, num in row.items():
                if num > 1:
                    num_points += 1

        return num_points



    

    # Day 4

    def d4_calc_score(self, board, num):
        res = 0
        for row in board:
            for val in row:
                if val[1] == 0:
                    res += val[0]
        return res * num

    def d4_read_boards(self, data):
        numbers = [int(x) for x in data[0].strip().split(',')]
        boards = []
        board = []

        for i in range(2, len(data)):
            line = data[i].strip()
            if line == '':
                boards.append(board)
                board = []
            else:
                board.append(list([[int(x), 0] for x in line.split()]))
        if len(board) > 0:
            boards.append(board)
        return (numbers, boards)

    def d4_1(self):
        data = self.read_input('D4.txt')
        
        (numbers, boards) = Advent.d4_read_boards(data)
        for num in numbers:
            for board in boards:
                for row in range(0, len(board)):
                    for col in range(0, len(board[row])):
                        if board[row][col][0] == num:
                            board[row][col][1] = 1
                            winner = True
                            for r in range(0, len(board)):
                                if board[r][col][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                return Advent.d4_calc_score(board, num)
                            for c in range(0, len(board[row])):
                                if board[row][c][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                return Advent.d4_calc_score(board, num)
        return ''

    def d4_2(self):
        data = self.read_input('D4.txt')
        
        (numbers, boards) = Advent.d4_read_boards(data)
        loosers = list(range(0, len(boards)))
        for num in numbers:
            for b in range(0, len(boards)):
                board = boards[b]
                for row in range(0, len(board)):
                    for col in range(0, len(board[row])):
                        if board[row][col][0] == num:
                            board[row][col][1] = 1
                            winner = True
                            for r in range(0, len(board)):
                                if board[r][col][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                if len(loosers) > 1:
                                    if b in loosers:
                                        loosers.remove(b)
                                else:
                                    return Advent.d4_calc_score(board, num)
                            for c in range(0, len(board[row])):
                                if board[row][c][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                if len(loosers) > 1:
                                    if b in loosers:
                                        loosers.remove(b)
                                else:
                                    return Advent.d4_calc_score(board, num)
        return ''

    # Day 3


    def read_input(self, filename):
        f = open(filename)
        try:
            data = f.readlines()
        finally:
            f.close()
        
        return data


    start_times = {}
    def start_timer(self, label = 'current'):
        self.start_times[label] = datetime.datetime.now()
        return self.start_times[label]
        
    def get_timer(self, label = 'current'):
        if label in self.start_times:
            return (datetime.datetime.now() - self.start_times[label], self.start_times[label], datetime.datetime.now())
        return (None, None, None)    
    

if __name__ == "__main__":
    start = datetime.datetime.now()
    print("Started at "+start.strftime('%X %x'))
    
    print("=====Solution=====")
    print(Advent().solve())
    
    end = datetime.datetime.now()
    print("Ended at "+end.strftime('%X %x'))
    print("Executed for "+str(end-start))



