from django.shortcuts import render
from django.views import generic
from .models import Item




class MenuList(generic.ListView):
    queryset =Item.objects.order_by("-date_created")
    template_name = "index.html" 
    
    def get_context_data(self):
        context = {"meals": "Pizaa"}
        return context
class MenuItemDetail(generic.DetailView):
    model = Item
    teplate_name = "menu_item_detail.html"