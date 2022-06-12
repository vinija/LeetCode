class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:        
        transactions_by_name = {}
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            if name in transactions_by_name:
                transactions_by_name[name].add((int(time), city))
            else:
                transactions_by_name[name] = {(int(time), city)}
        
        invalid = []
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            if int(amount) > 1000:
                invalid.append(transaction)
            elif self.isInvalid(int(time), city, transactions_by_name[name]):
                invalid.append(transaction) # Only want to append once because it will eventually get to the other transaction and look it up
            
        return invalid
    
    def isInvalid(self, time, city, transactions_by_name):
        for current_time, current_city in transactions_by_name:
            if city != current_city and time in range(current_time-60, current_time+61):
                return True
        return False
sol=Solution()
print(sol.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))