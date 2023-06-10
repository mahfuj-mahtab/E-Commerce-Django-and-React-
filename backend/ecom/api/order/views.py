from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt

def validate_user_session(id,token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk= id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False
    
@csrf_exempt
def add(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error' : 'User Not Logged In','code' : '1'})
    if(request.method == 'POST'):
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']
        total_products = len(products.split(',')[:])
        UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk= user_id)
    except UserModel.DoesNotExist:
        return JsonResponse({'error' : 'User Doesnot Exists'})
    order = Order(user = user,products_name = products,total_products = total_products,transaction_id = transaction_id,total_amount = amount)
    order.save()
    return JsonResponse({"success" : True,'error': False,'msg' : 'order placed successfully'})
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer