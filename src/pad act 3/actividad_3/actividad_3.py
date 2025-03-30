import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import csv

class actividad3:
    def __init__(self, ruta_dataset):
        self.ruta_raiz = os.path.abspath(os.getcwd())
        self.ruta_act2 = "{}/src/pad act 3/actividad_3/".format(self.ruta_raiz)
        datos = {
            "n_punto": [0,1,2,3,4,5,6,7,8,9,10,11],
            "detalle":["Crea un DataFrame frutas que luzca así","","","","","","","","","","",""],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],      
        }
        self.df = pd.DataFrame(datos)
        self.df["resultado"] = self.df["resultado"].astype(object) # Convertimos a tipo de object
        print(self.ruta_raiz)

        try:
            self.review = pd.read_csv(ruta_dataset)
            print("Dataset 'Wine Reviews' cargado con exito")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{ruta_dataset}'")
            self.review = pd.DataFrame() # Inicializa un DataFrame vacio para evitar errores posteriores 
        except Exception as e: 
            print(f"Error al cargar el dataset: {e}")
            self.review = pd.DataFrame()     

    def punto_1(self):
        # Crear el diccionario de datos
        datos = {
            "Granadilla": [20],
            "Tomates": [50]
        }

        # Crear el DataFrame
        frutas = pd.DataFrame(datos)

        # Imprimir el DataFrame para verificar
        print(frutas)
        
        # Guardar el DataFrame en un archivo CSV
        frutas.to_csv(f"{self.ruta_act2}punto_1.csv", index=False)
        
        self.df.loc[0, "resultado"] = f"{self.ruta_act2}punto_1.csv" # Guardar la ruta del archivo en el DataFrame principal


    def punto_2(self):
        # Crear el diccionario de datos
        datos_ventas = {
            "Granadilla": [20, 49],
            "Tomates": [50, 100]
        }

        # Crear el DataFrame
        ventas_frutas = pd.DataFrame(datos_ventas, index=["ventas 2021", "ventas 2022"])

        # Imprimir el DataFrame para verificar
        print(ventas_frutas)
        
        # Guardar el DataFrame en un archivo CSV
        ventas_frutas.to_csv(f"{self.ruta_act2}punto_2.csv")
        
        self.df.loc[1, "resultado"] = f"{self.ruta_act2}punto_2.csv" # Guardar la ruta del archivo en el DataFrame principal

    def punto_3(self):
        os.makedirs(self.ruta_act2, exist_ok=True)
        utensilios = pd.Series(
            data=["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
            index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
            name="Cocina",
            dtype="object"
        )
        print(utensilios)

        # Modificar la ruta de guardado
        ruta_guardado = f"{self.ruta_act2}punto_3.csv"

        # Imprimir la ruta de guardado
        print(f"Intentando guardar en: {ruta_guardado}")

        # Guardar la Serie en un archivo CSV
        try:
            utensilios.to_csv(ruta_guardado, header=True)
            print("Archivo punto_3.csv guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar punto_3.csv: {e}")
            print(e)

        # Guardar la ruta del archivo en el DataFrame principal
        self.df.loc[2, "resultado"] = ruta_guardado  

    def punto_4(self):
        if not self.review.empty:
        # Obtener las primeras 5 filas y seleccionar las columnas
            primeras_filas = self.review.head()[["country", "variety", "winery"]]
        # Obtener las últimas 5 filas y seleccionar las columnas
            ultimas_filas = self.review.tail()[["country", "variety", "winery"]]
        # Concatenar las primeras y últimas filas
            filas_combinadas = pd.concat([primeras_filas, ultimas_filas])
        
        # Convertir el DataFrame concatenado a texto sin el índice
            resultado_texto = filas_combinadas.to_string(index=False)
        
        # Guardar el resultado en self.df
            self.df.loc[3, "resultado"] = resultado_texto
            self.df.loc[3, "detalle"] = "Primeras y últimas filas del DataFrame Wine Reviews"
        
        # Imprimir el resultado para verificar que está bien
            print(f"Resultado del punto 4:\n{resultado_texto}")
        
        # Guardar el DataFrame completo en un archivo CSV
            self.df.to_csv(f"{self.ruta_act2}actividad3_resultados.csv", index=False)
        
        else:
            self.df.loc[3, "resultado"] = "Dataset no cargado"
            self.df.loc[3, "detalle"] = "Dataset no cargado"
    
        print("punto_4 ejecutado con éxito")
     

    def punto_5(self):
        self.df.loc[4,"resultado"] = len(self.df)+4
        print("punto_5")

    def punto_6(self):
        self.df.loc[5,"resultado"] = "punto_5.csv"
        print("punto_6")

    def punto_7(self):
        self.df.loc[6,"resultado"] = len(self.df)+6
        print("punto_7") 

    def punto_8(self):
        self.df.loc[7,"resultado"] = len(self.df)+7
        print("punto_8")

    def punto_9(self):
        self.df.loc[8,"resultado"] = len(self.df)+8
        print("punto_9")

    def punto_10(self):
        self.df.loc[9,"resultado"] = len(self.df)+9
        print("punto_10") 

    def punto_11(self):
        self.df.loc[10,"resultado"] = len(self.df)+10
        print("punto_11") 

    def punto_12(self,num=100):
        self.df.loc[11,"resultado"] = len(self.df)+11
        print("punto_12") 
        
    def ejecutar(self):
        # self.punto_1()     
        self.punto_2() 
        self.punto_3() 
        # self.punto_4() 
        # self.punto_5() 
        # self.punto_6() 
        # self.punto_7() 
        # self.punto_8() 
        # self.punto_9() 
        # self.punto_10()
        # self.punto_11()
        # self.punto_12()
        # self.df.to_csv("actividad3.csv", index=False) # Guarda sin el indice

if __name__ == "__main__":
    act = actividad3(r"C:\repositorios\WilmerArce_Entrega_Actividad_3\src\pad act 3\archivo-act-3\winemag-data-130k-v2.csv")
    act.ejecutar()
