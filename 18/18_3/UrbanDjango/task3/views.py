from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')

def shop(request):
    title = 'Цветы'
    small = 'Небольшой'
    normal = 'Средний'
    big = 'Большой'
    context = {
        'title' : title,
        'small' : small,
        'normal' : normal,
        'big' : big
    }
    return render(request, 'shop.html', context)



def cart(request):

    return render(request, 'cart.html')
