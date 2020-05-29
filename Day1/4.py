cp=float(input("Enter Cost Price"))
sp=float(input("Enter Selling Price"))
profit=sp-cp
print("Profit: ", profit)
newsp=1.05*profit+sp-profit
print("NewSellingPrice: ",newsp)
