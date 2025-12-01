import datetime
a=datetime.date.today()
b=datetime.date(a.year,12,31)
hmdl=(b-a).days
d="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
h={"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) ""AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/125.0.0.0 Safari/537.36")}
import requests
from io import StringIO
r=requests.get(d, headers=h)
rh=StringIO(r.text)
print("inputs:")
# Finland
# 269876
i=input()
dr=input()
dr=int(dr)
import pandas as pd
tbl=pd.read_html(rh)[2]
tbl=tbl.iloc[1:,:]
print(tbl)
#for i2 in tbl.index:
for ind,r in tbl.iterrows():
    if r.iloc[0]!=i: continue
    v1=r.iloc[0]
    v2=r.iloc[1]
    v3=r.iloc[2]
    v4=r.iloc[3]
    print(v1,v2,v3,v4)
    print()
    break
journees=365
procntsats=hmdl/journees
print("inc pd 2023")
print(int(v2)-dr)
print("inc pd 2022")
print(int(v3)-dr)
print("inc pd 2021")
print(int(v4)-dr)
sml=0
grd=-1
#confrontare i dati
if int(v2)-dr>sml:sml=int(v2)-dr
if int(v3)-dr>sml:sml=int(v3)-dr
if int(v4)-dr>sml:sml=int(v4)-dr
if int(v2)-dr<grd or grd==-1:grd= int(v2) - dr
if int(v3)-dr<grd:grd= int(v3) - dr
if int(v4)-dr<grd:grd= int(v4) - dr
print(sml)
print(grd)
print()
ms=hmdl/30
ms=int(ms)
if ms==0:ms=1
print(ms)
print("min")
print(str(sml/ms)+str(" -- per m inc req, at least"))
print("max")
print(str(grd / ms) + str(" -- per m inc req, record"))
print()
print()