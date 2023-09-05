import csv
import subprocess

ad_list,wsus_list = [],[]

with open('DIRETORIO DO EXPORT AD', mode='r') as csv_wsus:
    csv_reader = csv.DictReader(csv_wsus, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        ad_list.append(row['cn'].upper())
        line_count += 1

with open('DIRETORIO DO EXPORT WSUS', mode='r') as csv_wsus:
    csv_reader = csv.DictReader(csv_wsus, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        #ESSA LINHA ALTERA DADOS DO EXPORT DO WSUS, VERIFIQUE SE NO SEU E NECESSARIO!
        wsus_list.append(row['FullDomainName'].replace('.DOMINIO','').upper())
        line_count += 1

diff = frozenset(ad_list).difference(wsus_list)

f = open(".\\names.txt", "w")

for item in diff:
    f.write(item+'\n')
f.close()


subprocess.Popen(".\\start.bat") 