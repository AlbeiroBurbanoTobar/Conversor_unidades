import streamlit as st

def convertir_temperatura(conversion: str, valor: float) -> float:
    """
    Convierte una temperatura de una unidad a otra.

    Args:
        conversion: Tipo de conversión ("Celsius a Fahrenheit", etc.).
        valor: Valor a convertir.

    Returns:
        Valor convertido a la unidad objetivo.
    """

    if conversion == "Celsius a Fahrenheit":
        return (valor * 9/5) + 32
    elif conversion == "Fahrenheit a Celsius":
        return (valor - 32) * 5/9
    elif conversion == "Celsius a Kelvin":
        return valor + 273.15
    elif conversion == "Kelvin a Celsius":
        return valor - 273.15
    else:
        raise ValueError(f"Conversión de temperatura no válida: {conversion}")


def convertir_longitud(conversion: str, valor: float) -> float:
    """
    Convierte una longitud de una unidad a otra.

    Args:
        conversion: Tipo de conversión ("Pies a Metros", etc.).
        valor: Valor a convertir.

    Returns:
        Valor convertido a la unidad objetivo.
    """

    if conversion == "Pies a Metros":
        return valor * 0.3048
    elif conversion == "Metros a Pies":
        return valor / 0.3048
    elif conversion == "Pulgadas a Centímetros":
        return valor * 2.54
    elif conversion == "Centímetros a Pulgadas":
        return valor / 2.54
    else:
        raise ValueError(f"Conversión de longitud no válida: {conversion}")


# Funciones similares para las demás categorías (peso/masa, volumen, etc.)

# Configuración de la aplicación
st.title("Conversor Universal by Albeiro B.")

# Selección de la categoría
categoria = st.selectbox("Selecciona una categoría:",
                        ("Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos"))

# Lógica para cada categoría
if categoria == "Temperatura":
    # Selección del tipo de conversión
    conversion_temperatura = st.selectbox("Selecciona el tipo de conversión:",
                                         ("Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"))
    # Ingreso del valor a convertir
    valor_temperatura = st.number_input("Ingresa el valor a convertir:")
    # Cálculo del resultado
    resultado_temperatura = convertir_temperatura(conversion_temperatura, valor_temperatura)
    # Visualización del resultado
    st.write("Resultado:", resultado_temperatura)

elif categoria == "Longitud":
    # ... (Lógica similar para las demás categorías)

# ... (Lógica similar para las demás categorías)


# Se pueden agregar comentarios y documentación a las demás funciones de conversión

