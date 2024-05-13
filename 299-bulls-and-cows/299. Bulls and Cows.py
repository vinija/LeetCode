class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_freq = {}
        guess_freq = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_digit = secret[i]
                guess_digit = guess[i]
                
                if secret_digit in guess_freq and guess_freq[secret_digit] > 0:
                    cows += 1
                    guess_freq[secret_digit] -= 1
                else:
                    secret_freq[secret_digit] = secret_freq.get(secret_digit, 0) + 1
                    
                if guess_digit in secret_freq and secret_freq[guess_digit] > 0:
                    cows += 1
                    secret_freq[guess_digit] -= 1
                else:
                    guess_freq[guess_digit] = guess_freq.get(guess_digit, 0) + 1
        
        return f"{bulls}A{cows}B"
