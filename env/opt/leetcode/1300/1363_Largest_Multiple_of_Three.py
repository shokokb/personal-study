class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        group = defaultdict(lambda:[])
        for n in digits:
            group[n % 3].append(n)
        group[1].sort()
        group[2].sort()
        mod = sum(digits) % 3
        if mod == 2:
            try:
                group[2].pop(0)
                ret = sorted(reduce(lambda a, b: a + b, group.values()), reverse=True)
                return "".join([str(x) for x in ret])
            except:
                try:
                    group[1].pop(0)
                    group[1].pop(0)
                    ret = sorted(reduce(lambda a, b: a + b, group.values()), reverse=True)
                    return "".join([str(x) for x in ret])
                except:
                    return ""
        elif mod == 1:
            try:
                group[1].pop(0)
                ret = sorted(reduce(lambda a, b: a + b, group.values()), reverse=True)
                return "".join([str(x) for x in ret])
            except:
                try:
                    group[2].pop(0)
                    group[2].pop(0)
                    ret = sorted(reduce(lambda a, b: a + b, group.values()), reverse=True)
                    return "".join([str(x) for x in ret])
                except:
                    return ""
        else:
            ret = sorted(digits, reverse=True)
            if all([x == 0 for x in digits]):
                return "0"
            return "".join([str(x) for x in ret])
