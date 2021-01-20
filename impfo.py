import shutil
from urllib.request import Request, urlopen, urlretrieve
from io import BytesIO
from openpyxl import load_workbook

XLSX_URL = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx?__blob=publicationFile"
PATH = "data.xlsx"

request = Request(XLSX_URL, headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(request).read()

wb = load_workbook(filename = BytesIO(f))

for sheet in wb: 
    print(sheet.title)
