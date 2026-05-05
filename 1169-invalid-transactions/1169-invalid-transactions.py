class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        by_name = {}
        invalid = set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",") 
            time = int(time)
            amount = int(amount)
            if name not in by_name:
                by_name[name] = []
            by_name[name].append((time, amount, city, i))
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",") 
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                invalid.add(i)
            
            for (other_time, other_amount, other_city, other_i) in by_name[name]:
                if city != other_city and abs(time - other_time) <= 60:
                    invalid.add(i)
                    invalid.add(other_i)
        return[transactions[i] for i in invalid]