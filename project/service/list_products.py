# service/routes.py
@app.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')

    query = Product.query

    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))
    if category:
        query = query.filter(Product.category.ilike(f'%{category}%'))
    if availability:
        query = query.filter(Product.availability == (availability == 'true'))

    products = query.all
