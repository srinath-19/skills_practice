from fastapi import FastAPI
from models import Product

app = FastAPI()


products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get('/')
def root():
    return 'Welcome to FastAPI'

@app.get('/products')
def get_all_products():
    return products

@app.get('/products/{name}')
def get_product(name : str):
    for p in products:
        if p.name == name:
            return p
    return 'Product not found'

@app.post('/products')
def add_product(p : Product):
    products.append(p)
    return 'Product added successfully'

@app.put('/products/{name}')
def update_product(name: str, updated_product: Product):
    for i, p in enumerate(products):
        if p.name == name:
            products[i] = updated_product
            return 'Product updated successfully'
    return 'Product not found'
