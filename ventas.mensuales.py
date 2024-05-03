import pandas as pd
import matplotlib.pyplot as plt

ventas_mensuales = [
{"mes": "Enero", "total_ventas": 15000, "año": 2023},
{"mes": "Febrero", "total_ventas": 18000, "año": 2023},
{"mes": "Marzo", "total_ventas": 22000, "año": 2023},
{"mes": "Abril", "total_ventas": 19000, "año": 2023},
{"mes": "Mayo", "total_ventas": 25000, "año": 2023},
{"mes": "Junio", "total_ventas": 28000, "año": 2023},
{"mes": "Julio", "total_ventas": 32000, "año": 2023},
{"mes": "Agosto", "total_ventas": 30000, "año": 2023},
{"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
{"mes": "Octubre", "total_ventas": 31000, "año": 2023},
{"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
{"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
{"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
{"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
{"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
{"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
{"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
{"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
{"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
{"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
{"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
{"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
{"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
{"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]



lista_ventas = pd.DataFrame(ventas_mensuales)
def ventas():

  lista_ventas["total_ventas"]
  lista_ventas["total"] = lista_ventas["total_ventas"].cumsum()

  # filtrando total de ventas por mayor a 20000
  result = lista_ventas["total"] > 20000
  result = lista_ventas[result]
  print(result)
  
  # filtrando por la mayor venta del mes
  max_valor = max(lista_ventas["total_ventas"])

  print(f"mayor venta: {max_valor}")

  # obteniendo promedio de ventas
  promedio = sum(lista_ventas["total_ventas"])/len(lista_ventas["total_ventas"])
  print(f"promedio de ventas: {promedio}")

  # copia del dataframe
  mes_total = lista_ventas
  # eliminando columnas
  mes_total = mes_total.drop(["año"], axis=1)
  mes_total = mes_total.drop(["total"], axis=1)
  # mostrando dataframe con columnas 'mes' y 'total_ventas'
  print(mes_total)

  # asignando columnas a variables nuevas
  x = mes_total["mes"]
  y = mes_total["total_ventas"]

  # graficando y mostrando columnas con la librería matplotlib
  plt.plot(x, y)
  plt.show()

ventas()