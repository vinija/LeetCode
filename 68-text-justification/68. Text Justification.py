class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, current_line, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                res.append(''.join(current_line))
                current_line, num_of_letters = [], 0
            current_line.append(word)
            num_of_letters += len(word)
        
        res.append(' '.join(current_line).ljust(maxWidth))
        return res