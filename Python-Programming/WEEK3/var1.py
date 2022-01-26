#variable is act as bucket which store value
#ram bank bank
ram_bank_balance=1000000
ram_loan=100000
laxman_bank_balance=2000000
laxman_loan=290000
# net income is total income by ram and laxman
net_income=ram_bank_balance+laxman_bank_balance
net_liablity=ram_loan+laxman_loan
final_amount=net_income-net_liablity
print(net_income)
print(net_liablity)
print("the total income is ",final_amount)