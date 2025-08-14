import streamlit as st
import joblib

# Cargar el modelo entrenado
modelo = joblib.load("primermillon.joblib")

# Título y autor
st.title("Predictor de Éxito Académico")
st.write("**Autor:** Alfredo Díaz")

# Imagen debajo del autor
st.image(
    "https://buscacarrera.com.co/public/content/articulos/la-clave-del-exito-academico-como-crear-un-plan-de-estudio-efectivo.jpg",
    use_container_width=True
)

# Introducción
st.markdown("""
Esta aplicación predice si un estudiante logrará graduarse y tener éxito académico 
en la Universidad en función de dos características:  
- **Nota IA** (de 0.0 a 1.0)  
- **GPA** (de 0.0 a 1.0)  

Ajusta los valores con los deslizadores y pulsa el botón **Predecir** para ver el resultado.
""")

# Sliders de entrada
nota_ia = st.slider("Nota IA", 0.0, 1.0, 0.5, step=0.1)
gpa = st.slider("GPA", 0.0, 1.0, 0.5, step=0.1)

# Botón para predecir
if st.button("Predecir"):
    prediccion = modelo.predict([[nota_ia, gpa]])[0]

    if prediccion == 0:
        st.markdown(
            "<span style='color:red; font-size:20px;'>❌ No se graduará</span>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<span style='color:green; font-size:20px;'>🎓 Felicitaciones, te vas a graduar con honores</span>",
            unsafe_allow_html=True
        )

# Footer con derechos de autor
st.markdown("---")
st.markdown("© 2025 UNAB")
