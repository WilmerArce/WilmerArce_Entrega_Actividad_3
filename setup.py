from setuptools import setup, find_packages

setup(
    name="actividad3", # Nombre del proyecto
    version="0.0.1",
    author="wilmer arce",
    author_email="wilmer.arce@est.iudigital.edu.co",
    description="",
    py_modules=["actividad_3"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests", # Paquete separado
        "matplotlib",  # Paquete separado
        "numpy",  # Paquete separado
        "seaborn"  # Paquete separado

    ]   
)