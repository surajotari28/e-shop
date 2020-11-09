from .cart import Cart

def cart(request):
    '''to display the contents of cart in every webpage'''
    return {'cart': Cart(request)}