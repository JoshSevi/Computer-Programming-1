class CashRegister :
    #Construct a cash register with cleared item count and total
    def __init__(self) :
        self._itemCount = 0
        self._totalPrice = 0.0

    #adds an item to this cash register
    #@param price the price of this item
    def addItem(self,price) :
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    #Gets the price of all items in the current sale.
    #@retun the total price
    def getTotal(self) :
        return self._totalPrice

    #Gets the number of items in the current dale
    #@return the item count
    def getCount(self) :
        return self._itemCount

    #Clears the item count and the total
    def clear(self) :
        self._itemCount = 0
        self._totalPrice = 0.0
