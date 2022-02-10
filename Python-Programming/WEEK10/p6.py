#find the total profit or loss of each trader working in trading firm .information ragarding number of traders number of unknown transaction.

empid=input("enter the employee id :-")
while (empid!= '-1'):
      trade=int(input("Enter the trade amount:-"))
      profit_loss=0
      while(trade != 0):
           profit_loss = profit_loss + trade
           trade = int(input("enter the trade amount:-"))
      print(f'Profit/Loss for employee {empid} is {profit_loss}')
      empid=input("\n Enter the employee id:-")
           
        
