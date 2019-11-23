import pandas as pd

# Here are two DataFrames, products and invoices. The product DataFrame has an identifier and a sticker price. The
# invoices DataFrame lists the people, product identifiers, and quantity. Assuming that we want to generate totals,
# how do we join these two DataFrames together so that we have one which lists all of the information we need?
products = pd.DataFrame([pd.Series({'ProductID': 4109, 'Price': 5.0, 'Product': 'Sushi Roll'}),
                         pd.Series({'ProductID': 1412, 'Price': 0.5, 'Product': 'Egg'}),
                         pd.Series({'ProductID': 8931, 'Price': 1.5, 'Product': 'Bagel'})])
products = products.set_index('ProductID')
print(products)

invoices = pd.DataFrame([pd.Series({'Customer': 'Ali', 'ProductID': 4109, 'Quantity': 1}),
                         pd.Series({'Customer': 'Eric', 'ProductID': 1412, 'Quantity': 12}),
                         pd.Series({'Customer': 'Adam', 'ProductID': 8931, 'Quantity': 6}),
                         pd.Series({'Customer': 'Sam', 'ProductID': 4109, 'Quantity': 2})])
print(invoices)

# products=products.reset_index()
product_invoice = pd.merge(products, invoices, how='outer', left_index=True, right_on='ProductID')

print(product_invoice)