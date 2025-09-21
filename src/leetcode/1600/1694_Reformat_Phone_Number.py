class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '')
        number = number.replace('-', '')
        new_number = [number[i:i+3] for i in range(0, len(number), 3)]
        if len(new_number[-1]) == 1:
            new_number[-1] = new_number[-2][-1] + new_number[-1]
            new_number[-2] = new_number[-2][:-1]
        return "-".join(new_number)
        