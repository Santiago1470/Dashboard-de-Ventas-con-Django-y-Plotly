from django.shortcuts import render
from ventas import models
import pandas as pd
import plotly.express as px


def inicio(request):
    return render(request, "ventas/inicio.html")

def mostrarVentas(request):
    data = models.Venta.objects.all()
    df = pd.DataFrame({
    'ID': [venta.id for venta in data],
    'Cantidad': [venta.cantidad for venta in data],
    'Barrio': [venta.barrio.nombre for venta in data]  
    })
    figura = px.bar(df, x='Barrio', y='Cantidad', color='ID')
    html = figura.to_html(full_html = False)
    print(html)
    context = {
        "nombre": "Usuario",
        "data": data,
        "mihtml": html
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