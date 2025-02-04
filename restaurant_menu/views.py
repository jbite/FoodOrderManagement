from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Item, MEAL_TYPE, Order, OrderItem




class MenuList(generic.ListView):
    queryset =Item.objects.order_by("-date_created")
    template_name = "index.html" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context
    
class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"
    
        