import requests
import pandas as pd
import time

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
          'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

years = ['2017']

title = 'Lista de Funcionários da Prefeitura Municipal de Independência'
print("{0:{1}^100}".format(title.upper(), "="))
print("{0:{1}^100} \n".format(years[0], "="))

start_time = time.time()
writer = pd.ExcelWriter('lista_funcionarios.xlsx')
for i in range(1, 13):
    url = "http://www.independencia.ce.gov.br/recursoshumanos.php?nome=&funcao=&lotacao=&vinculo=&MES={0}&ANO=2017".format(i)
    html = requests.get(url).content
    dataframe_list = pd.read_html(html)
    table = dataframe_list[0]
    table.to_excel(writer, sheet_name=months[i-1])
    print("Mês: {0} ==> {1}".format(months[i - 1], 'OK'))
writer.save()
writer.close()
elapsed = time.time() - start_time
print("Tempo: {0} min - {1} s".format(elapsed/60, elapsed))
print("Fonte: http://www.independencia.ce.gov.br")