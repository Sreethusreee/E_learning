from  instructorApp.models import Cart,Order

def cart_count(request):
    if request.user.is_authenticated:
        count=Cart.objects.filter(user_instance=request.user).count()
    else:
        count=0
    return {'cart_count':count}


def course_count(request):
    if request.user.is_authenticated:
        orders=Order.objects.filter(user_instance=request.user,is_paid=True).count()
        return {'order_count':orders}
    else:
        return {'order_count':0}