#!/usr/bin/python


import sys
from operator import mul

class DivFinder:

    pld = { \
        1: range(1, 10), \
        2: [2, 4, 6, 8], \
        3: range(1, 10), \
        4: [2, 4, 6, 8], \
        5: [5], \
        6: [6, 2, 8, 4], \
        7: [7, 4, 1, 8, 5, 2, 9, 6], \
        8: [2, 4, 6, 8], \
        9: range(1, 10) \
    }

    def __init__(self, number = False):
        self.number = number
        self.max_digits = 200

    def not_contains_zero(self, number):
        while number > 10:
            if number % 10 == 0:
                return False
            number //= 10
        return number % 10


    def is_sum_greater_mult(self, number):
        sum = 0
        mult = 1
        sn = str(number)
        for c in sn:
            sum += int(c)
            mult *= int(c)
            if mult > sum:
                return False
        return True


    def get_digits_count(self, number):
        return len(str(number))


    def get_non_one(self, digits_count):
        non_one = []
        dc = 1
        i = 1
        process = True
        pattern = [2]
        while process:
            start = pattern[i] if i < len(pattern) else 2
            for j in xrange(start, 10):
                pattern[0] = j
                if sum(pattern) + (digits_count - len(pattern)) >= reduce(mul, pattern):
                    non_one.append(pattern[::-1])
                else:
                    pattern[0] = 2
                    if j == 2:
                        process = False
                    break
            i = 1            
            while i < dc:
                if pattern[i] < 9:
                    pattern[i] += 1
                    for j in xrange(0, i):
                        pattern[j] = pattern[i]
                    break
                else:
                    pattern[i] = 2
                    i += 1
            if i >= dc:
                dc += 1
                i = 1
                pattern = [2]*dc
            if dc > digits_count:
                process = False
                break
        return non_one

    def get_ones(self, digits_count):
        """

        >>> df.get_ones(1)
        1
        >>> df.get_ones(2)
        11
        >>> df.get_ones(3)
        111
        >>> df.get_ones(8)
        11111111
        """
        res = 1
        for i in xrange(1, digits_count):
            res = res * 10 + 1
        return res

    def list_to_num(self, lst):
        """

        >>> df.list_to_num([1, 2, 3])
        123
        >>> df.list_to_num([])
        0
        >>> df.list_to_num([1])
        1
        """
        res = 0
        for d in lst:
            res = res*10+d
        return res


    def permutate(self, patterns, digits_count, allowed_last_digits):
        """
        >>> [x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 3], [3, 4], [3, 5], [2, 2, 2], [2, 2, 3], [2, 3, 7]], 6, [3, 7, 9])]
        [[1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 7], [1, 1, 1, 1, 1, 9], [1, 1, 1, 1, 2, 3], [1, 1, 1, 2, 1, 3], [1, 1, 2, 1, 1, 3], [1, 2, 1, 1, 1, 3], [2, 1, 1, 1, 1, 3], [1, 1, 1, 1, 2, 7], [1, 1, 1, 2, 1, 7], [1, 1, 2, 1, 1, 7], [1, 2, 1, 1, 1, 7], [2, 1, 1, 1, 1, 7], [1, 1, 1, 1, 2, 9], [1, 1, 1, 2, 1, 9], [1, 1, 2, 1, 1, 9], [1, 2, 1, 1, 1, 9], [2, 1, 1, 1, 1, 9], [1, 1, 1, 1, 3, 3], [1, 1, 1, 3, 1, 3], [1, 1, 3, 1, 1, 3], [1, 3, 1, 1, 1, 3], [3, 1, 1, 1, 1, 3], [1, 1, 1, 1, 4, 3], [1, 1, 1, 4, 1, 3], [1, 1, 4, 1, 1, 3], [1, 4, 1, 1, 1, 3], [4, 1, 1, 1, 1, 3], [1, 1, 1, 1, 5, 3], [1, 1, 1, 5, 1, 3], [1, 1, 5, 1, 1, 3], [1, 5, 1, 1, 1, 3], [5, 1, 1, 1, 1, 3], [1, 1, 1, 2, 2, 3], [1, 1, 2, 1, 2, 3], [1, 1, 2, 2, 1, 3], [1, 2, 1, 1, 2, 3], [1, 2, 1, 2, 1, 3], [1, 2, 2, 1, 1, 3], [2, 1, 1, 1, 2, 3], [2, 1, 1, 2, 1, 3], [2, 1, 2, 1, 1, 3], [2, 2, 1, 1, 1, 3], [1, 1, 1, 2, 7, 3], [1, 1, 1, 7, 2, 3], [1, 1, 2, 1, 7, 3], [1, 1, 2, 7, 1, 3], [1, 1, 7, 1, 2, 3], [1, 1, 7, 2, 1, 3], [1, 2, 1, 1, 7, 3], [1, 2, 1, 7, 1, 3], [1, 2, 7, 1, 1, 3], [1, 7, 1, 1, 2, 3], [1, 7, 1, 2, 1, 3], [1, 7, 2, 1, 1, 3], [2, 1, 1, 1, 7, 3], [2, 1, 1, 7, 1, 3], [2, 1, 7, 1, 1, 3], [2, 7, 1, 1, 1, 3], [7, 1, 1, 1, 2, 3], [7, 1, 1, 2, 1, 3], [7, 1, 2, 1, 1, 3], [7, 2, 1, 1, 1, 3], [1, 1, 1, 2, 3, 7], [1, 1, 1, 3, 2, 7], [1, 1, 2, 1, 3, 7], [1, 1, 2, 3, 1, 7], [1, 1, 3, 1, 2, 7], [1, 1, 3, 2, 1, 7], [1, 2, 1, 1, 3, 7], [1, 2, 1, 3, 1, 7], [1, 2, 3, 1, 1, 7], [1, 3, 1, 1, 2, 7], [1, 3, 1, 2, 1, 7], [1, 3, 2, 1, 1, 7], [2, 1, 1, 1, 3, 7], [2, 1, 1, 3, 1, 7], [2, 1, 3, 1, 1, 7], [2, 3, 1, 1, 1, 7], [3, 1, 1, 1, 2, 7], [3, 1, 1, 2, 1, 7], [3, 1, 2, 1, 1, 7], [3, 2, 1, 1, 1, 7]]
        >>> [x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 3], [3, 4], [3, 5], [2, 2, 2], [2, 2, 3], [2, 3, 7]], 6, [1, 3, 7, 9])]
        [[1, 1, 1, 1, 2, 3], [1, 1, 1, 2, 1, 3], [1, 1, 2, 1, 1, 3], [1, 2, 1, 1, 1, 3], [2, 1, 1, 1, 1, 3], [1, 1, 1, 1, 2, 7], [1, 1, 1, 2, 1, 7], [1, 1, 2, 1, 1, 7], [1, 2, 1, 1, 1, 7], [2, 1, 1, 1, 1, 7], [1, 1, 1, 1, 2, 9], [1, 1, 1, 2, 1, 9], [1, 1, 2, 1, 1, 9], [1, 2, 1, 1, 1, 9], [2, 1, 1, 1, 1, 9], [1, 1, 1, 1, 3, 3], [1, 1, 1, 3, 1, 3], [1, 1, 3, 1, 1, 3], [1, 3, 1, 1, 1, 3], [3, 1, 1, 1, 1, 3], [1, 1, 1, 1, 4, 3], [1, 1, 1, 4, 1, 3], [1, 1, 4, 1, 1, 3], [1, 4, 1, 1, 1, 3], [4, 1, 1, 1, 1, 3], [1, 1, 1, 1, 5, 3], [1, 1, 1, 5, 1, 3], [1, 1, 5, 1, 1, 3], [1, 5, 1, 1, 1, 3], [5, 1, 1, 1, 1, 3], [1, 1, 1, 2, 2, 3], [1, 1, 2, 1, 2, 3], [1, 1, 2, 2, 1, 3], [1, 2, 1, 1, 2, 3], [1, 2, 1, 2, 1, 3], [1, 2, 2, 1, 1, 3], [2, 1, 1, 1, 2, 3], [2, 1, 1, 2, 1, 3], [2, 1, 2, 1, 1, 3], [2, 2, 1, 1, 1, 3], [1, 1, 1, 2, 7, 3], [1, 1, 1, 7, 2, 3], [1, 1, 2, 1, 7, 3], [1, 1, 2, 7, 1, 3], [1, 1, 7, 1, 2, 3], [1, 1, 7, 2, 1, 3], [1, 2, 1, 1, 7, 3], [1, 2, 1, 7, 1, 3], [1, 2, 7, 1, 1, 3], [1, 7, 1, 1, 2, 3], [1, 7, 1, 2, 1, 3], [1, 7, 2, 1, 1, 3], [2, 1, 1, 1, 7, 3], [2, 1, 1, 7, 1, 3], [2, 1, 7, 1, 1, 3], [2, 7, 1, 1, 1, 3], [7, 1, 1, 1, 2, 3], [7, 1, 1, 2, 1, 3], [7, 1, 2, 1, 1, 3], [7, 2, 1, 1, 1, 3], [1, 1, 1, 2, 3, 7], [1, 1, 1, 3, 2, 7], [1, 1, 2, 1, 3, 7], [1, 1, 2, 3, 1, 7], [1, 1, 3, 1, 2, 7], [1, 1, 3, 2, 1, 7], [1, 2, 1, 1, 3, 7], [1, 2, 1, 3, 1, 7], [1, 2, 3, 1, 1, 7], [1, 3, 1, 1, 2, 7], [1, 3, 1, 2, 1, 7], [1, 3, 2, 1, 1, 7], [2, 1, 1, 1, 3, 7], [2, 1, 1, 3, 1, 7], [2, 1, 3, 1, 1, 7], [2, 3, 1, 1, 1, 7], [3, 1, 1, 1, 2, 7], [3, 1, 1, 2, 1, 7], [3, 1, 2, 1, 1, 7], [3, 2, 1, 1, 1, 7]]
        >>> [x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3]], 4, [1, 2])]
        [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [1, 1, 3, 1], [1, 3, 1, 1], [3, 1, 1, 1], [1, 1, 4, 1], [1, 4, 1, 1], [4, 1, 1, 1], [1, 1, 5, 1], [1, 5, 1, 1], [5, 1, 1, 1], [1, 1, 6, 1], [1, 6, 1, 1], [6, 1, 1, 1], [1, 1, 7, 1], [1, 7, 1, 1], [7, 1, 1, 1], [1, 1, 8, 1], [1, 8, 1, 1], [8, 1, 1, 1], [1, 1, 9, 1], [1, 9, 1, 1], [9, 1, 1, 1], [1, 2, 1, 2], [1, 1, 2, 2], [2, 1, 1, 2], [1, 2, 2, 1], [2, 1, 2, 1], [2, 2, 1, 1], [1, 3, 1, 2], [1, 1, 3, 2], [3, 1, 1, 2], [1, 2, 3, 1], [1, 3, 2, 1], [2, 1, 3, 1], [2, 3, 1, 1], [3, 1, 2, 1], [3, 2, 1, 1]]
        >>> [x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3]], 4, [3, 2])]
        [[1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 2], [1, 2, 1, 2], [2, 1, 1, 2], [1, 1, 3, 2], [1, 3, 1, 2], [3, 1, 1, 2], [1, 1, 2, 3], [1, 2, 1, 3], [2, 1, 1, 3]]
        """
        for p in patterns:
            if 1 in allowed_last_digits:
                p.append(1)
            vis_ld = []
            for ld in p:
                if not ld in allowed_last_digits or ld in vis_ld:
                    continue
                vis_ld.append(ld)
                p1 = p[:]
                p1.remove(ld)
                template = [1]*(digits_count-1-len(p1)) + p1
                import itertools
                vis_perm = []
                for p2 in itertools.permutations(template, len(template)):
                    p2 = list(p2)
                    if p2+[ld] in vis_perm:
                        continue
                    vis_perm.append(p2+[ld])
                    yield p2+[ld]


    def iterate(self, digits_count):
        non_one = self.get_non_one(digits_count)
        max = []
        for p in non_one:
            p_num = self.list_to_num(p)
            if not len(p)-1 in max:
                while len(max) < len(p):
                    max.append((0, 0))
            if max[len(p)-1][0] < p_num:
                max[len(p)-1] = (p_num, p)

            
        ones = self.get_ones(digits_count)
        to_go = self.number - ones % self.number
        if to_go <= max[self.get_digits_count(to_go) - 1][0]:
            return ones+to_go

        allowed_last_digits = self.pld[self.number%10]
        for n in self.permutate(non_one, digits_count, allowed_last_digits):
            n = self.list_to_num(n)
            if self.check_result(n):
                return n

        return False

    def find_divisible(self, number = False):
        if not number == False:
            self.number = number

        if self.check_result(self.number):
            return self.number
        else:
            digits_count = self.get_digits_count(self.number)
            i = self.number
            while self.get_digits_count(i) < digits_count * 2:
                i += self.number
                if self.check_result(i):
                    return i    
            result = False
            digits_count = self.get_digits_count(i)
            while result == False and digits_count < self.max_digits:
                result = self.iterate(digits_count)
                digits_count += 1
            return result


    def check_result(self, number):
        """

        >>> df.check_result(110)
        False
        >>> df.check_result(11214)
        True
        >>> df.check_result(84)
        False
        >>> df.check_result(420)
        False
        """
        return self.not_contains_zero(number) and self.is_sum_greater_mult(number) and \
            (number % self.number == 0)

if __name__ == '__main__':
    import sys
    if 'doctest' in sys.argv:
        import doctest
        doctest.testmod(extraglobs={'df': DivFinder(42)})
        sys.exit()

    finder = DivFinder()

    for i in xrange(1, 30000):
        if i % 10 == 0:
            continue;
        number = finder.find_divisible(i)
        print i, number, len(str(number))

    #print finder.find_divisible(sys.stdin.read())


