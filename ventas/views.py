from django.shortcuts import render
from ventas import models
import pandas as pd
import plotly.express as px


def inicio(request):
    return render(request, "ventas/inicio.html")

def mostrarVentas(request):
    if request.method == 'POST':
        mes_selec = request.POST.get('mes')
        if mes_selec == "all":
            data = models.Venta.objects.all()
        else:
            data = models.Venta.objects.filter(mes=mes_selec)
    else:
        data = models.Venta.objects.all()
        
    figura = None
    if data:
        df = {
            'ID': [venta.id for venta in data],
            'Cantidad': [venta.cantidad for venta in data],
            'Barrio': [venta.barrio.nombre for venta in data],
            'Mes': [venta.mes for venta in data]
        }
        figura = px.bar(df, x='Barrio', y='Cantidad', color='Mes')

    context = {
        "nombre": "Usuario",
        "data": data,
        "mihtml": figura.to_html(full_html=False) if figura else None
    }
    return render(request, "ventas/index.html", context)


# def saludo(request):
#     data = models.Barrio.objects.all()
#     df = pd.DataFrame({
#         "marca": ['chevrolet', 'nissan', 'ferrari'],
#         "cantidad": [20, 10, 3],
#         "pais": ['Colombia', 'Mexico', 'Venezuela']
#     })
#     fig = px.bar(df, x='marca', y='cantidad', color='pais')
#     mihtml = fig.to_html(full_html = False)
#     print(mihtml)
#     context = {
#         "nombre": "santiago",
#         "data": data,
#         "mihtml": mihtml
#     }
#     return render(request, "ventas/index.html", context)