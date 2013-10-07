# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import models
from django.template import RequestContext
from django.shortcuts import redirect
from django.core.paginator import Paginator

def index(request):
    
    if request.REQUEST.has_key('pid'):
        pagenum = request.REQUEST['pid']
    else:
        pagenum = 1
    
    products = models.Product.objects.all()
    p = Paginator(products,2)
    page = p.page(pagenum)
    
    return render_to_response("index.html",{"user":request.user,
                                            "p":p,'products':page},
                              context_instance = RequestContext(request))

def query(request):
    
    if request.REQUEST.has_key('pid'):
        pagenum = request.REQUEST['pid']
    else:
        pagenum = 1    
    if request.REQUEST.has_key('Pname'):
        products = models.Product.objects.filter(name__contains = request.POST['Pname'])
    else:
        products = models.Product.objects.all()
    p = Paginator(products,2)
    page = p.page(pagenum)
            
    return render_to_response("index.html",{"user":request.user,
                                            "p":p,'products':page,
                                            "pagename":"query"},
                                            context_instance = RequestContext(request))
                                
def order(request):
    if not request.user.is_authenticated()： #if user is not authenticated,just redirect to login
        return redirect("/admin/")
    if request.REQUEST.has_key('pid'):
        pagenum = request.REQUEST['pid']
    else:
        pagenum = 1     
    if request.REQUEST.has_key('productID'):
        product = models.Product.objects.get(id=request.REQUEST['productID'])
        orderObj = models.Order.objects.create(product=product, user=request.user)
    if request.REQUEST.has_key('orderID'):
        orderID =request.REQUEST['orderID']
        orderObj = models.Order.objects.filter(id = orderID).delete()
    products = models.Order.objects.filter(user=request.user)
    p = Paginator(products,2)
    page = p.page(pagenum)          
    return render_to_response("order.html",{"user":request.user,
                                            "p":p,'products':page,
                                                "pagename":"order"},
                                                context_instance = RequestContext(request))    
