


class Trades():
    def __init__(self, amount, fee):
        self.amount = amount
        self.fee = fee
        self.inTrade = False
        self.tradeNums = 0
        self.tradesWon = 0
    
    def makeBuyTrade(self, price : float,  amount= 0.0 , percent = 0.0) -> None:
        if amount==0 and  percent==0 or price: print("Trade failed!")

    def __str__(self) -> str:
        return f"{self.amount} from {self.tradeNums} trades. \n With a winrate of {self.tradesWon / self.tradeNums}%."

    def getTradeNums(self)->int:
        return self.tradeNums
        
        
