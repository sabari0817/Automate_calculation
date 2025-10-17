from django.shortcuts import render
from .models import Shawarma

def calculate_kubbos(request):
    shawarma_menu = [
        {"name": "Chicken Shawarma roll", "kubbos": 1},
        {"name": "Chicken Shawarma plate", "kubbos": 2},
        {"name": "Ghost Shawarma roll", "kubbos": 1},
        {"name": "Ghost Shawarma plate", "kubbos": 2},
        {"name": "Black Shawarma roll", "kubbos": 1},
        {"name": "Black Shawarma plate", "kubbos": 2},
        {"name": "Schezwan Shawarma roll", "kubbos": 1},
        {"name": "Schezwan Shawarma plate", "kubbos": 2},
        {"name": "Mexican Shawarma roll", "kubbos": 1},
        {"name": "Mexican Shawarma plate", "kubbos": 2},
        {"name": "Peri Peri Shawarma roll", "kubbos": 1},
        {"name": "Peri Peri Shawarma plate", "kubbos": 2},
        {"name": "Street Special Shawarma roll", "kubbos": 1},
        {"name": "Street Special Shawarma plate", "kubbos": 2},
        {"name": "Street Special flav Shawarma roll", "kubbos": 1},
        {"name": "Street Special flav Shawarma plate", "kubbos": 2},
        {"name": "Pushpa Shawarma roll", "kubbos": 1},
        {"name": "Pushpa Shawarma plate", "kubbos": 2},
        {"name": "Ghost Gopal Shawarma roll", "kubbos": 1},
        {"name": "Ghost Gopal Shawarma plate", "kubbos": 2},
        {"name": "Paprika Shawarma roll", "kubbos": 1},
        {"name": "Paprika Shawarma plate", "kubbos": 2},
        {"name": "Zaitoon Shawarma roll", "kubbos": 1},
        {"name": "Zaitoon Shawarma plate", "kubbos": 2},
        {"name": "Cheese Shawarma roll", "kubbos": 1},
        {"name": "Cheese Kebab Roll", "kubbos": 1},
        {"name": "Malai Cheese Kebab Roll", "kubbos": 1},
        {"name": "Hariyali Cheese Kebab Roll", "kubbos": 1},
        {"name": "Veg Shawarma roll", "kubbos": 1},
        {"name": "Paneer Tikka Shawarma roll", "kubbos": 1},
        {"name": "Peri peri Paneer Tikka Shawarma roll", "kubbos": 1},
        {'name':'street cheese roll','kubbos':1},
        {'name': 'free shawerma','kubbos':1},
        {'name': 'kubbose','kubbos':1}
    ]

    total_kubbos = 0
    results = []

    if request.method == "POST":
        for item in shawarma_menu:
            qty = int(request.POST.get(item["name"], 0))
            used = qty * item["kubbos"]
            results.append({
                "name": item["name"],
                "qty": qty,
                "kubbos_per_item": item["kubbos"],
                "used": used
            })
            total_kubbos += used

        return render(request, 'result.html', {
            'results': results,
            'total_kubbos': total_kubbos
        })

    return render(request, 'calculate.html', {'shawarma_menu': shawarma_menu})
