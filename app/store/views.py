from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.http import JsonResponse
from .models import ShoppingCart, CartItem, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()

    return render(request, 'store/signup.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all()
    if request.headers.get('Accept') == 'application/json':
        product_data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
        return JsonResponse({'products': product_data}, status=200)
    return render(request, 'store/product_list.html', {'products': products})


# @csrf_exempt
# @login_required
# def add_to_cart(request, product_id):
#     if request.method == 'POST':
#         product = get_object_or_404(Product, id=product_id)
#         cart, created = ShoppingCart.objects.get_or_create(user=request.user)
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()

#         # Respond with a success message
#         return JsonResponse({'message': 'Product added to cart!'})
    
#     return JsonResponse({'error': 'Invalid request'}, status=400)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
@login_required
def add_to_cart(request):
    print(f"User: {request.user}") 
    if not request.user.is_authenticated:  
        return JsonResponse({'error': 'User is not authenticated'}, status=401)

    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            body_data = json.loads(request.body)
            product_id = body_data.get('productId', None)

            if not product_id:
                return JsonResponse({'error': 'Product ID is missing'}, status=400)

            # Get the product and the user's shopping cart
            product = Product.objects.get(id=product_id)
            cart, created = ShoppingCart.objects.get_or_create(user=request.user)

            # Add the product to the cart (or increase quantity if it already exists)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            if created:  # If the item is newly created, set the quantity to 1
                cart_item.quantity = 1
            else:  # If the item already exists, increase the quantity
                cart_item.quantity += 1
            
            cart_item.save()

            return JsonResponse({'success': 'Product added to cart successfully'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

 
 
@login_required
def cart_view(request):
    try:
        cart = ShoppingCart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except ShoppingCart.DoesNotExist:
        cart_items = []

    # Calculate the total price for the cart
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    # If the cart is empty, we can display a custom message
    empty_message = "Your cart is empty." if not cart_items else None

    return render(request, 'store/cart_view.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'empty_message': empty_message,
    })

@login_required
@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        # Fetch cart items from the session
        cart = ShoppingCart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        # If the cart is empty, return an error message
        if not cart_items:
            return JsonResponse({'error': 'Your cart is empty!'})

        grand_total = 0

        # Loop through the cart items and update the product quantities in the database
        for item in cart_items:
            try:
                product = item.product  # Get the product directly from the CartItem
                if product.stock >= item.quantity:  # Check if enough stock is available
                    product.stock -= item.quantity  # Deduct the quantity
                    product.save()  # Save the updated product
                    grand_total += product.price * item.quantity
                else:
                    return JsonResponse({'error': f'Not enough stock for {product.name}'})
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product not found'})

        # Clear the cart after successful checkout
        cart_items.delete()  # Remove all items from the cart

        # Send a success response back to the frontend with the total price
        return JsonResponse({'success': f'Your purchase was successful! Total: ${grand_total:.2f}'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})