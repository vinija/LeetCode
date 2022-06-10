class Solution:
    # T/S: O(n)
    def getFolderNames(self, names: List[str]) -> List[str]:
        words = {}
        for name in names:
            new_name = name
            if new_name in words:
                k = words[new_name]
                while new_name in words:
                    new_name = f'{name}({k})'
                    k += 1
                words[name] = k
            words[new_name] = 1
        return words.keys()