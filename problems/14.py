class Collatz:
    max_length = dict()
    longest = 0
    next_in_chain = dict()

    def nextElement(n):
        if n in self.next_in_chain:
            return self.next_in_chain[n]
        forEven = lambda n: n // 2
        forOdd = lambda n: (3 * n) + 1
        if n % 2 == 0:
            self.next_in_chain[n] = forEven(n)
        else:
            self.next_in_chain[n] = forOdd(n)
        return self.next_in_chain[n]

    def lengthOf(i):
        if i in self.max_length:
            return self.max_length[i]
        stack = []
        while next_up:=self.nextElement(i) > 1:
            if next_up in self.max_length:
                self.max_length[i] = self.max_length[next_up] + 1
                return self.max_length[i]
            stack.append(i)
            i = next_up

    def longestChainBelow(max_seed_exclusive=1_000_000):
        for i in range(1, max_seed_exclusive):
            self.lengthOf(i)
        return self.longest



def nextCollatzElement(n):
    forEven = lambda n: n // 2
    forOdd = lambda n: (3 * n) + 1
    if n % 2 == 0:
        return forEven(n)
    else:
        return forOdd(n)

# def collatzLength(i):
#     max_length = dict()
#     def helper(i):
#         if i in max_length:
#             return max_length[i]
#         else:
#             max_length[i] = collatzLength(nextCollatzElement(i)) + 1


def longestCollatz(max_seed_exclusive=1_000_000):
    biggest = 0
    max_length = dict()
    def collatzLength(i):
        if i == 1:
            max_length[i] = 1
        elif i not in max_length:
            max_length[i] = collatzLength(nextCollatzElement(i)) + 1
        return max_length[i]
    for i in range(1, max_seed_exclusive):
        length = collatzLength(i)
        biggest = biggest if biggest >= length else length
    return biggest
