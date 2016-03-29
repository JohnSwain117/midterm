# A credit card company computes a customer's "minimum payment" according to the following rule. The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater; however, if a $10 minimum payment exceeds the balance, then the minimum payment is the balance. Write a program to return the minimum payment. Assume that the variable balance contains the customer's balance.
#   Example 1: if your balance is 1000, then your program should return 21. 
#   Example 2: if your balance is 600, then your program should return 12.6. 
#   Example 3: if your balance is 25, then your program should return 10. 
#   Example 4: if your balance is 8, then your program should return 8. 

#the minimum payment is 10 dollars or 2.1% of the balance so if the customers balance is below 10 it will automatically be 10

def computeMinimumPayment( balance ):
    #TODO write code inside this function that achieves the functionality described above
    percentage = balance * 0.021
    if balance < 10:
        return balance
    elif percentage < 10:
        return 10
    else:
        return percentage
