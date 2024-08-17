class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        secret_counter = Counter()
        guess_counter = Counter()

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_counter[secret[i]] += 1
                guess_counter[guess[i]] += 1
        
        for digit in guess_counter:
            if digit in secret_counter:
                cows += min(secret_counter[digit], guess_counter[digit])
        return f"{bulls}A{cows}B"