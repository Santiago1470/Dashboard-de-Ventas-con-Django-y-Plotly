from django.shortcuts import render
from ventas import models
import pandas as pd
import plotly.express as px


def inicio(request):
    return render(request, "ventas/inicio.html")

def mostrarVentas(request):
    mes_selec = ""
    barrio_selec = ""
    
    barrios = models.Barrio.objects.all()
    
    if request.method == 'POST':
        mes_selec = request.POST.get('mes')
        barrio_selec = request.POST.get('barrio')
        
        if mes_selec == "all" and barrio_selec == "all":
            data = models.Venta.objects.all()
        elif mes_selec == "all":
            data = models.Venta.objects.filter(barrio=barrio_selec)
        elif barrio_selec == "all":
            data = models.Venta.objects.filter(mes=mes_selec)
        else:
            data = models.Venta.objects.filter(mes=mes_selec, barrio=barrio_selec)
    else:
        data = models.Venta.objects.all()
        
    figura = None
    figura2 = None
    figura3 = None
    figura4 = None
    if mes_selec == "all" and barrio_selec != "all" and data:
        df_all_months = {
            'ID': [venta.id for venta in data],
            'Cantidad': [venta.cantidad for venta in data],
            'Barrio': [venta.barrio.nombre for venta in data],
            'Mes': [venta.mes for venta in data]
            # 'Mes': ["Todos los meses" for _ in range(len(data))]
        }
        figura = px.bar(df_all_months, x='Mes', y='Cantidad', color='Barrio', title='Ventas')
        figura2 = px.scatter(df_all_months, x='Mes', y='Cantidad' , title='Ventas')
        figura3 = px.line(df_all_months, x='Mes', y='Cantidad', color='Barrio', symbol='Barrio' , title='Ventas')
        ##figura4 = px.pie(df, values='Cantidad', names='Barrio' , title='Ventas')
    else :
        if data:
            df = {
                'ID': [venta.id for venta in data],
                'Cantidad': [venta.cantidad for venta in data],
                'Barrio': [venta.barrio.nombre for venta in data],
                'Mes': [venta.mes for venta in data]
            }
            figura = px.bar(df, x='Barrio', y='Cantidad', color='Mes')
            figura2 = px.scatter(df, x='Barrio', y='Cantidad')
            figura3 = px.line(df, x='Barrio', y='Cantidad', color='Barrio', symbol='Barrio')
            ##figura4 = px.pie(df, values='Cantidad',names='Mes' , title='Ventas')
            
        # figura = figura_all_months if figura is None else figura.add_traces(figura_all_months.data)
    barrio_selec = int(barrio_selec) if barrio_selec != "" and barrio_selec != "all" else 0
    context = {
        "nombre": "Usuario",
        "data": data,
        "mihtml": figura.to_html(full_html=False) if figura else None,
        "mihtml2":figura2.to_html(full_html=False) if figura2 else None,
        "mihtml3":figura3.to_html(full_html=False) if figura3 else None,
        "mihtml4":figura4.to_html(full_html=False) if figura4 else None,
        "mes_selec": mes_selec,
        "barrio_selec": barrio_selec,
        "barrios": barrios
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