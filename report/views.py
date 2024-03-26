from django.shortcuts import render
import pandas as pd
import plotly.express as px

def index(request):
    df = pd.DataFrame({
        "carros": ["Ford", "Mazda", "Toyota", "Chevrolet"],
        "cantidad": [4,2,4,5],
        "ciudad": ["Cali", "Bogota", "Manizales", "Yopal"]
    })


    fig =  px.bar(df, x="carros", y="cantidad", color="ciudad", barmode="group")

    plot_div = fig.to_html(full_html=False)

    return render(request, "report/index.html", context={'plot_div': plot_div, 'table': df.to_html()})
