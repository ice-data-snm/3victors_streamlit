#%%
import pandas as pd
import streamlit as st
from datetime import date
from united_airlines import get_info_on_threads
# st.set_page_config(page_title="Colector Mercadolibre", page_icon="img/favicon.ico")
# import streamlit_authenticator as stauth
# import yaml

# from main import run
from PIL import Image
#%%


# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=yaml.SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )
# name, authentication_status, username = authenticator.login('Login', 'main')


# if authentication_status:
#     authenticator.logout('Logout', 'main')
#     st.write(f'Bienvenido *{name}*')
    
image_ice = Image.open('img/Iceberg-Data-Final-Logo.png')
image_procol = Image.open('img/3victors.png')

# col1, col2, col3 = st.columns(2)
# col1, col2, col3 = st.columns([1, 1, 1])
# col1.image(image_ice, height=150)
# # col1.image( width=150)
# col3.image(image_procol, height=150)

col1, col2, col3 = st.columns(3)

with col1:
    st.image(image_procol, width=150, use_column_width=True)

with col2:
    # Add content to the second column if desired
    pass

with col3:
    st.image(image_ice, width=150, use_column_width=True)

# st.header("*Kiruna*")# - Extractor de información de propiedades")
st.header("Flights information getter")
st.write("Tool to get the flights information based on the Origin, destination and dates")
# st.write("Bogotá y Soacha")
st.write('***')
st.write('**Inputs**')

option_origin = st.selectbox(
    'Select the origin',
    ('','BOG', 'JFK', 'MAD', 'WAS'))
st.write('You selected:', option_origin)

option_destination = st.selectbox(
    'Select the origin',
    ('','MEX', 'YYZ', 'YVR', 'SEA'))
st.write('You selected:', option_destination)


d = st.date_input("Search flights starting from", min_value=date.today())
st.write('You selected:', d)

number = st.number_input("Enter a number", min_value=0, value=2, step=1)
print(d.strftime("%m/%d/%Y"))
if st.button('Collect info'):
    with st.spinner(text='Running'):
        # try:
            # Buscar la fila correspondiente al valor options_cat_r en la columna "subcategoryName"
            # print(options_cat_r)
            get_info_on_threads(option_origin, option_destination, str(d.strftime("%m/%d/%Y")), number)
            st.success('Terminado')
            st.write(f'Find you results in: https://console.cloud.google.com/storage/browser/ice-3-victors/info_ua/{option_origin}_{option_destination}_{d}')

            # with open('Surtiapp.csv') as f:
            #     st.download_button('Download CSV R', f, file_name='Surtiapp.csv',mime='text/csv')
        # except Exception as e:
        #     print('---')
        #     print(e)
        #     st.warning('No se encontraron datos con los terminos de busqueda', icon="⚠️")
        # st.success('Terminado')


# get_info_on_threads (country_oringin, airportsDestination, Date_mm_dd_yyyy, num_days):


# st.write('You selected:', option_origin, option_destination, d, number)




    # col1, col2, col3, col4 = st.columns(4)
    # with col1:
    #     st.write('')
    # with col2:
    #     st.image(image_r, width=300)
    # with col3:
    #     st.write('')
    # with col4:
    #     st.write('')
        
        
    # st.header("Kiruna - Extractor de información de propiedades")
    # st.write("Herramienta para obtener información de las propiedades de Finca Raíz y Metro cuadrado de")
    # st.write("Bogotá y Soacha")
    # st.write('***')
    # st.write('*Instrucciones*')
    # st.write('*Instrucciones*')    


    # tab1, tab2 = st.tabs(['Herramienta', 'Diccionario de columnas'])
    
    # # Tab 1
    # with tab1:
    #     search_r = st.text_input('Nombre producto', '').strip()
    #     start_r = st.number_input('Páginas de Busqueda', min_value=1, max_value=10, value=1,step=1)
    #     st.write('')
    #     st.write("Califica el producto dando clik [aquí](https://docs.google.com/forms/d/e/1FAIpQLSdqeZQrmJL3DGWU3Edn0kSB-Xi5niHQDoZN1TVbR4SbHr48Ew/viewform?usp=pp_url)")
    #     st.write('')
    #     st.markdown("1 Página de búsqueda = 50 items")
        
    #     if st.button('Recolectar datos'):
    #         with st.spinner('Recolectando datos...'):
    #             try:
    #                 data_r = run(search_r,start_r)
    #                 st.dataframe(data_r) 
                    
    #                 # Descargar los datos recolectados
    #                 with open('output/pdp/data.csv') as f:
    #                     st.download_button('Download CSV f', f, file_name='output/pdp/data.csv',mime='text/csv')
    #                 st.success('Done')
                    
                    
    #             except Exception as e:
    #                 st.warning('No se encontraron datos con los terminos de busqueda', icon="⚠️")
    #                 print(e)
                
                    
    # # Tab 2
    # with tab2:
    #     st.title('Catálogo de datos')
    #     st.write('**ingestion_time**: Indica la fecha y hora en la que se recolectó la información en formato unix. El formato unix es un sistema de numeración que representa una fecha y hora como un número entero.')
    #     st.write('**producto_id**: Columna única que identifica a cada producto en la base de datos de mercadolibre.')
    #     st.write('**nombre_producto**: Contiene el nombre del producto que se vende.')
    #     st.write('**precio_producto**: Representa el precio de venta de cada producto en pesos colombianos.')
    #     st.write('**categoria_producto**: Indica la categoría a la que pertenece cada producto.')
        
    #     st.write('**inventario_producto**: Representa la cantidad de unidades de cada producto que se encuentran en stock.')
    #     st.write('**productos_vendidos**: Indica la cantidad de unidades vendidas del producto.')
    #     st.write('**pais_producto**: Representa el país donde se encuentra el producto.')
    #     st.write('**departamento_producto**: Indica el departamento del país donde se encuentra el producto.')
    #     st.write('**ciudad_producto**: Indica la ciudad donde se encuentra el producto.')
    
    #     st.write('**procedencia_producto**: Indica la fuente de origen del producto. Esta puede ser local o importado.')
    #     st.write('**id_proveedor**: Columna única que identifica a cada proveedor en la base de datos de mercadolibre.')
    #     st.write('**fecha_registro_proveedor**: Indica la fecha en que el proveedor se registró en la plataforma de mercadolibre.')
    #     st.write('**clasificacion_proveedor**: Indica la clasificación a la que pertenece el proveedor, puede ser silver, gold o platino.')
    #     st.write('**ventas_totales**: Representa la cantidad total de ventas realizadas por el proveedor, incluyendo las ventas completadas y pendientes.')
        
        
    #     st.write('**ventas_canceladas_proveedor**: Representa la cantidad de ventas que el proveedor ha cancelado o que han sido canceladas por los compradores.')
    #     st.write('**ventas_completas_proveedor**: Indica la cantidad de ventas que el proveedor ha completado satisfactoriamente hasta la fecha.')
    #     st.write('**calificación_vendedor**: Indica la calificación promedio del proveedor basada en las calificaciones positivas, negativas y neutrales que ha recibido.')
        
    #     st.write('**calificaciones_positivas**: Representa el porcentaje de calificaciones positivas que el proveedor ha recibido de los compradores.')
    #     st.write('**calificaciones_negativas**: Representa el porcentaje de calificaciones negativas que el proveedor ha recibido de los compradores.')
    #     st.write('**calificaciones_neutrales**: representa el porcentaje de calificaciones neutrales que el proveedor ha recibido de los compradores.')
        
        
        
        