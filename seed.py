# para leer y transformar los datos
import pandas as pd

# para cargar el proyecto Django en este script
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paqueteria.settings")
import django
django.setup()

#  Django models
from zipcodes.models import *

""" leemos el archivo con los datos """
excel = pd.ExcelFile('./data/CPdescarga.xls')

states = excel.sheet_names[1::]  # la posición 0 contiene una hoja llamada 'notas'
state_codes = [x for x in range(1, 33)]  # codigos del 1 al 32 como SEPOMEX

""" Solo necesitamos correr esto una vez """

# inserta estados
# for (name, code) in zip(states, state_codes):
#     s = State()
#     s.name = name
#     s.state_code = code
#     s.save()

# inseta municipios
# for s in states:
#     df = excel.parse(s)
#     """ existen columnas que no aportan informacion, asi que las eliminamos """
#     df = df.drop(columns=["d_codigo", "id_asenta_cpcons", "c_cve_ciudad", "c_CP", "d_ciudad"])
#     # print(df.info())
#     muns = df.loc[:, 'D_mnpio'].unique()
#     code_muns = df.loc[:, 'c_mnpio'].unique()
#     state_code = df.loc[:, 'c_estado'].unique()[0]
#     state = State.objects.get(state_code=state_code)
#     for (name, code) in zip(muns, code_muns):
#         m = Municipality()
#         m.name = name
#         m.municipality_code = code
#         m.state = state
#         m.save()

# inserta colonias
# for s in states:
#     df = excel.parse(s)
#     df = df.drop(columns=["d_codigo", "id_asenta_cpcons", "c_cve_ciudad", "c_CP", "d_ciudad"])
#     muns = Municipality.objects.filter(state__name=s)
#     # print(muns)
#     for m in muns:
#         # print (m)
#         colonias = df[df.loc[:, 'D_mnpio'] == m.name]
#         # print(colonias.shape)
#         for i in range(colonias.shape[0]):
#             sub = colonias.iloc[i]
#             nsub = Suburb()
#             nsub.name = sub.d_asenta
#             nsub.zip_code = sub.d_CP
#             nsub.zone_type = sub.d_zona
#             nsub.settlement_type = sub.d_tipo_asenta
#             nsub.municipality = m
#             nsub.save()
