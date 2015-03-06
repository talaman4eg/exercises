#!/usr/bin/python


import sys
from operator import mul

class Primes(object):
    """docstring for Primes"""
    def __init__(self, arg):
        super(Primes, self).__init__()
        self.arg = arg

    @staticmethod
    def prime_candidates(number, start = 0):
        if number >= 2 and number >= start:
            if start <= 2:
                yield 2
            if start <= 3:
                yield 3
            range_start = 6 if start < 12 else 6*(start//6)
            for x in xrange(range_start, number+2, 6):
                if x > start:
                    yield x - 1
                if x < number and x + 1 >= start:
                    yield x + 1

    @staticmethod
    def primes_gen(number):
        if number >= 2:
            yield 2
            yield 3
            i_sqrt = 2
            sq = 4
            for x in prime_candidates(number, 5):
                if sq < x:
                    i_sqrt += 1
                    sq += i_sqrt + i_sqrt - 1
                add = all(x % f != 0 for f in prime_candidates(i_sqrt))
                if add:
                    yield x 
    
    @staticmethod
    def prime_dividers(number):
        found = {}
        while number != 1 and number != -1:
            for p in primes_gen(number):
                if number % p == 0:
                    if not p in found:
                        found[p] = 1
                    else:
                        found[p] += 1
                    number = number / p
                    break
        return found
    
    @staticmethod
    def sum_digits(number):
        """
        >>> Primes.sum_digits(12345)
        15
        >>> Primes.sum_digits(12)
        3
        >>> Primes.sum_digits(987)
        24
        """
        result = 0
        while number > 0:
            result += number % 10
            number = number // 10
        return result

    filters = [3, 7, 9, 25, 27, 4, 8]
    sum_filters = [3, 9]
    number_filters = [7, 27]
    last_digits_filters = [25, 4, 8]

    @staticmethod
    def is_divisible(number, divider):
        """
        >>> [Primes.is_divisible(n, d) for n, d in [(999,3), (998,3), (990,9), (991,9), (6318,27), (6319,27), (615055,7), (615058,7), (1025,25), (1027,25)]]
        [True, False, True, False, True, False, True, False, True, False]
        """
        result = None
        if divider == 3 or divider == 9:
            result = Primes.sum_digits(number) % divider == 0
        elif divider == 27:
            result = Primes.is_divisible_by_27(number)
        elif divider == 7:
            result = Primes.is_divisible_by_7(number)
        elif divider == 25:
            result = (number % 100) % 25 == 0
        elif divider == 4:
            ld = number % 10
            pld = (number // 10) % 10
            if (pld % 2 == 0 and ld % 4 == 0) or (pld % 2 == 1 and ld in [2, 6]):
                return True
            else:
                return False
        elif divider == 8:
            return (number % 1000) % 8 == 0
        return result

    @staticmethod
    def is_divisible_by_27(number):
        sum = 0
        while number > 0:
            sum += number % 1000
            number = number // 1000
        return sum % 27 == 0

    @staticmethod
    def is_divisible_by_7(number):
        sum = 0
        sign = 1
        while not number == 0:
            sum += sign * (number % 1000)
            number = number // 1000
            sign *= -1
        return sum % 7 == 0



class DivFinder:
    """
    Solution for https://www.hackerrank.com/challenges/divisible-numbers
    """

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
        self.applicable_filters = []

    def detect_filters(self):
        self.applicable_filters = []
        for f in Primes.filters:
            if self.number % f == 0:
                self.applicable_filters.append(f)

    def check_filters(self, number, type = False):
        filters = Primes.filters
        if type == 'sum':
            filters = Primes.sum_filters
        elif type == 'last_digits':
            filters = Primes.last_digits_filters
        elif type == 'number':
            filters = Primes.number_filters
        for f in self.applicable_filters:
            if f in filters:
                if not Primes.is_divisible(number, f):
                    return False
        return True



    def not_contains_zero(self, number):
        """
        >>> df.not_contains_zero(1)
        True
        >>> df.not_contains_zero(12)
        True
        >>> df.not_contains_zero(10)
        False
        >>> df.not_contains_zero(0)
        False
        >>> df.not_contains_zero(101)
        False
        """
        while number > 10:
            if number % 10 == 0:
                return False
            number //= 10
        return number % 10 != 0


    def is_sum_greater_mult(self, number):
        """
        >>> df.is_sum_greater_mult(1)
        True
        >>> df.is_sum_greater_mult(12)
        True
        >>> df.is_sum_greater_mult(8)
        True
        >>> df.is_sum_greater_mult(88)
        False
        >>> df.is_sum_greater_mult(231)
        True
        >>> df.is_sum_greater_mult(2114)
        True
        """
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
        """
        >>> df.get_digits_count(12345)
        5
        >>> df.get_digits_count(232323)
        6
        >>> df.get_digits_count(555555555)
        9
        """
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
        >>> #[x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 3], [3, 4], [3, 5], [2, 2, 2], [2, 2, 3], [2, 3, 7]], 6, [3, 7, 9])]
        [[1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 7], [1, 1, 1, 1, 1, 9], [1, 1, 1, 1, 2, 3], [1, 1, 1, 2, 1, 3], [1, 1, 2, 1, 1, 3], [1, 2, 1, 1, 1, 3], [2, 1, 1, 1, 1, 3], [1, 1, 1, 1, 2, 7], [1, 1, 1, 2, 1, 7], [1, 1, 2, 1, 1, 7], [1, 2, 1, 1, 1, 7], [2, 1, 1, 1, 1, 7], [1, 1, 1, 1, 2, 9], [1, 1, 1, 2, 1, 9], [1, 1, 2, 1, 1, 9], [1, 2, 1, 1, 1, 9], [2, 1, 1, 1, 1, 9], [1, 1, 1, 1, 3, 3], [1, 1, 1, 3, 1, 3], [1, 1, 3, 1, 1, 3], [1, 3, 1, 1, 1, 3], [3, 1, 1, 1, 1, 3], [1, 1, 1, 1, 4, 3], [1, 1, 1, 4, 1, 3], [1, 1, 4, 1, 1, 3], [1, 4, 1, 1, 1, 3], [4, 1, 1, 1, 1, 3], [1, 1, 1, 1, 5, 3], [1, 1, 1, 5, 1, 3], [1, 1, 5, 1, 1, 3], [1, 5, 1, 1, 1, 3], [5, 1, 1, 1, 1, 3], [1, 1, 1, 2, 2, 3], [1, 1, 2, 1, 2, 3], [1, 1, 2, 2, 1, 3], [1, 2, 1, 1, 2, 3], [1, 2, 1, 2, 1, 3], [1, 2, 2, 1, 1, 3], [2, 1, 1, 1, 2, 3], [2, 1, 1, 2, 1, 3], [2, 1, 2, 1, 1, 3], [2, 2, 1, 1, 1, 3], [1, 1, 1, 2, 7, 3], [1, 1, 1, 7, 2, 3], [1, 1, 2, 1, 7, 3], [1, 1, 2, 7, 1, 3], [1, 1, 7, 1, 2, 3], [1, 1, 7, 2, 1, 3], [1, 2, 1, 1, 7, 3], [1, 2, 1, 7, 1, 3], [1, 2, 7, 1, 1, 3], [1, 7, 1, 1, 2, 3], [1, 7, 1, 2, 1, 3], [1, 7, 2, 1, 1, 3], [2, 1, 1, 1, 7, 3], [2, 1, 1, 7, 1, 3], [2, 1, 7, 1, 1, 3], [2, 7, 1, 1, 1, 3], [7, 1, 1, 1, 2, 3], [7, 1, 1, 2, 1, 3], [7, 1, 2, 1, 1, 3], [7, 2, 1, 1, 1, 3], [1, 1, 1, 2, 3, 7], [1, 1, 1, 3, 2, 7], [1, 1, 2, 1, 3, 7], [1, 1, 2, 3, 1, 7], [1, 1, 3, 1, 2, 7], [1, 1, 3, 2, 1, 7], [1, 2, 1, 1, 3, 7], [1, 2, 1, 3, 1, 7], [1, 2, 3, 1, 1, 7], [1, 3, 1, 1, 2, 7], [1, 3, 1, 2, 1, 7], [1, 3, 2, 1, 1, 7], [2, 1, 1, 1, 3, 7], [2, 1, 1, 3, 1, 7], [2, 1, 3, 1, 1, 7], [2, 3, 1, 1, 1, 7], [3, 1, 1, 1, 2, 7], [3, 1, 1, 2, 1, 7], [3, 1, 2, 1, 1, 7], [3, 2, 1, 1, 1, 7]]
        >>> #[x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 3], [3, 4], [3, 5], [2, 2, 2], [2, 2, 3], [2, 3, 7]], 6, [1, 3, 7, 9])]
        [[1, 1, 1, 1, 2, 3], [1, 1, 1, 2, 1, 3], [1, 1, 2, 1, 1, 3], [1, 2, 1, 1, 1, 3], [2, 1, 1, 1, 1, 3], [1, 1, 1, 1, 2, 7], [1, 1, 1, 2, 1, 7], [1, 1, 2, 1, 1, 7], [1, 2, 1, 1, 1, 7], [2, 1, 1, 1, 1, 7], [1, 1, 1, 1, 2, 9], [1, 1, 1, 2, 1, 9], [1, 1, 2, 1, 1, 9], [1, 2, 1, 1, 1, 9], [2, 1, 1, 1, 1, 9], [1, 1, 1, 1, 3, 3], [1, 1, 1, 3, 1, 3], [1, 1, 3, 1, 1, 3], [1, 3, 1, 1, 1, 3], [3, 1, 1, 1, 1, 3], [1, 1, 1, 1, 4, 3], [1, 1, 1, 4, 1, 3], [1, 1, 4, 1, 1, 3], [1, 4, 1, 1, 1, 3], [4, 1, 1, 1, 1, 3], [1, 1, 1, 1, 5, 3], [1, 1, 1, 5, 1, 3], [1, 1, 5, 1, 1, 3], [1, 5, 1, 1, 1, 3], [5, 1, 1, 1, 1, 3], [1, 1, 1, 2, 2, 3], [1, 1, 2, 1, 2, 3], [1, 1, 2, 2, 1, 3], [1, 2, 1, 1, 2, 3], [1, 2, 1, 2, 1, 3], [1, 2, 2, 1, 1, 3], [2, 1, 1, 1, 2, 3], [2, 1, 1, 2, 1, 3], [2, 1, 2, 1, 1, 3], [2, 2, 1, 1, 1, 3], [1, 1, 1, 2, 7, 3], [1, 1, 1, 7, 2, 3], [1, 1, 2, 1, 7, 3], [1, 1, 2, 7, 1, 3], [1, 1, 7, 1, 2, 3], [1, 1, 7, 2, 1, 3], [1, 2, 1, 1, 7, 3], [1, 2, 1, 7, 1, 3], [1, 2, 7, 1, 1, 3], [1, 7, 1, 1, 2, 3], [1, 7, 1, 2, 1, 3], [1, 7, 2, 1, 1, 3], [2, 1, 1, 1, 7, 3], [2, 1, 1, 7, 1, 3], [2, 1, 7, 1, 1, 3], [2, 7, 1, 1, 1, 3], [7, 1, 1, 1, 2, 3], [7, 1, 1, 2, 1, 3], [7, 1, 2, 1, 1, 3], [7, 2, 1, 1, 1, 3], [1, 1, 1, 2, 3, 7], [1, 1, 1, 3, 2, 7], [1, 1, 2, 1, 3, 7], [1, 1, 2, 3, 1, 7], [1, 1, 3, 1, 2, 7], [1, 1, 3, 2, 1, 7], [1, 2, 1, 1, 3, 7], [1, 2, 1, 3, 1, 7], [1, 2, 3, 1, 1, 7], [1, 3, 1, 1, 2, 7], [1, 3, 1, 2, 1, 7], [1, 3, 2, 1, 1, 7], [2, 1, 1, 1, 3, 7], [2, 1, 1, 3, 1, 7], [2, 1, 3, 1, 1, 7], [2, 3, 1, 1, 1, 7], [3, 1, 1, 1, 2, 7], [3, 1, 1, 2, 1, 7], [3, 1, 2, 1, 1, 7], [3, 2, 1, 1, 1, 7]]
        >>> #[x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3]], 4, [1, 2])]
        [[1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1], [1, 1, 3, 1], [1, 3, 1, 1], [3, 1, 1, 1], [1, 1, 4, 1], [1, 4, 1, 1], [4, 1, 1, 1], [1, 1, 5, 1], [1, 5, 1, 1], [5, 1, 1, 1], [1, 1, 6, 1], [1, 6, 1, 1], [6, 1, 1, 1], [1, 1, 7, 1], [1, 7, 1, 1], [7, 1, 1, 1], [1, 1, 8, 1], [1, 8, 1, 1], [8, 1, 1, 1], [1, 1, 9, 1], [1, 9, 1, 1], [9, 1, 1, 1], [1, 2, 1, 2], [1, 1, 2, 2], [2, 1, 1, 2], [1, 2, 2, 1], [2, 1, 2, 1], [2, 2, 1, 1], [1, 3, 1, 2], [1, 1, 3, 2], [3, 1, 1, 2], [1, 2, 3, 1], [1, 3, 2, 1], [2, 1, 3, 1], [2, 3, 1, 1], [3, 1, 2, 1], [3, 2, 1, 1]]
        >>> #[x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3]], 4, [3, 2])]
        [[1, 1, 1, 2], [1, 1, 1, 3], [1, 1, 2, 2], [1, 2, 1, 2], [2, 1, 1, 2], [1, 1, 3, 2], [1, 3, 1, 2], [3, 1, 1, 2], [1, 1, 2, 3], [1, 2, 1, 3], [2, 1, 1, 3]]
        >>> #[x for x in df.permutate( [[1], [2], [3], [4], [5], [6], [7], [8], [9], [2, 2], [2, 3]], 4, [3, 2])]
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
                if 1 in p1:
                    p1.remove(1)
                if 25 in self.applicable_filters:
                    if not 2 in p1 and not 7 in p1:
                        continue;
                ones_count = digits_count - len(p1) - 1
                sum = sum(p1)+ld+ones_count
                if 3 in applicable_filters and not sum % 3 == 0:
                    continue
                if 9 in applicable_filters and not sum % 9 == 0:
                    continue
                if p1 == []:
                    yield [1]*(digits_count-1)+[ld]
                    continue
                import itertools
                vis_perm = []
                cnt = 0
                for p2 in itertools.permutations(p1, len(p1)):
                    p2 = list(p2)
                    if p2+[ld] in vis_perm:
                        continue
                    vis_perm.append(p2+[ld])
                    for i, k in enumerate(p2):
                        moving = p2[:i+1]
                        staying = p2[i+1:]
                        for j in range(0, ones_count+1):
                            x = [1]*(ones_count - j) + moving + [1]*j + staying + [ld]
                            yield x
                            cnt += 1


    def iterate(self, digits_count):
        non_one = self.get_non_one(digits_count)
        allowed_last_digits = self.pld[self.number%10]
        for n in self.permutate(non_one, digits_count, allowed_last_digits):
            n = self.list_to_num(n)
            if self.check_result(n):
                return n

        return False


    def find_divisible(self, number = False):
        """
        >>> df.get_digits_count(df.find_divisible(542))
        23
        >>> df.get_digits_count(df.find_divisible(3885))
        109
        """
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
                #print digits_count
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

    if 'enum' in sys.argv:
        start = sys.argv[2] if len(sys.argv) > 2 else 1
        for i in xrange(int(start), 30000):
            if i % 10 == 0:
                continue;
            number = finder.find_divisible(i)
            print i, number, len(str(number))

        sys.exit()

    print finder.get_digits_count( finder.find_divisible(int(sys.stdin.read())))


