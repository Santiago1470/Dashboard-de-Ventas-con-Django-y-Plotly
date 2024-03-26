from django.shortcuts import render
from inventario.models import Carro
import pandas as pd
import plotly.express as px

def saludo(request):

    data = Carro.objects.all()
    df = pd.DataFrame({
        "marca": ['chevrolet', 'nissan', 'ferrari'],
        "cantidad": [20, 10, 3],
        "pais": ['Colombia', 'Mexico', 'Venezuela']
    })
    fig = px.bar(df, x='marca', y='cantidad', color='pais')
    mihtml = fig.to_html(full_html = False)
    print(mihtml)
    context = {
        "nombre": "santiago",
        "data": data,
        "mihtml": mihtml
    }
    return render(request, "inventario/index.html", context)
