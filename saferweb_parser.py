import sys
import os

base_usdot_website = "https://safer.fmcsa.dot.gov/query.asp?searchtype=ANY&query_type=queryCarrierSnapshot&query_param=USDOT&query_string="
usdot_link = ""

arguments = sys.argv

if len(arguments) > 1:
    input_usdot = arguments[1]
    usdot_link = base_usdot_website + input_usdot
    print(usdot_link)

lines = []

usdot_number = ""
company_name = ""

inspections_vehicle = 0
inspections_driver = 0
inspections_hazmat = 0
inspections_IEP = 0

oos_vehicle = 0
oos_driver = 0
oos_hazmat = 0
oos_IEP = 0

power_units = 0
drivers = 0
mileage = 0

inspections_captured = False
oos_captured = False

if usdot_link == "":
    print("No USDOT number was specified")
    raise SystemExit
else:
    os.system('curl -s "'+usdot_link+'" > temporary_html.html')
    with open('temporary_html.html','r') as file:
        lines = file.readlines()
        file.close()
    os.remove('temporary_html.html')

for x,line in enumerate(lines):
    if "USDOT Number: " in line:
        usdot_number = line.split("USDOT Number: ")[1].split("<br>")[0]
    if "<TITLE>SAFER Web - Company Snapshot" in line:
        company_name = line.split("<TITLE>SAFER Web - Company Snapshot ")[1].split("</TITLE>")[0]
    elif '<TH SCOPE="ROW" align="right" class="querylabelbkg">Inspections</TH>' in line and inspections_captured == False:
        inspections_vehicle = int(lines[x+1].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        inspections_driver = int(lines[x+2].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        inspections_hazmat = int(lines[x+3].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        inspections_IEP = int(lines[x+4].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        inspections_captured = True
    elif '<TH SCOPE="ROW" align="right" class="querylabelbkg">Out of Service</TH>' in line and oos_captured == False:
        oos_vehicle = int(lines[x+1].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        oos_driver = int(lines[x+2].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        oos_hazmat = int(lines[x+3].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        oos_IEP = int(lines[x+4].split('<TD align="center" class="queryfield">')[1].split('</TD')[0])
        oos_captured = True
    elif '<TH SCOPE="ROW" class="querylabelbkg" align=right><A class="querylabel" href="saferhelp.aspx#PowerUnits">Power Units:</A></TH>' in line:
        power_units = int(''.join(lines[x+1].split('<TD class="queryfield" valign=top>')[1].split('&nbsp;</TD>')[0].split(',')))
    elif '<TH SCOPE="ROW" class="querylabelbkg" align=right><A class="querylabel" href="saferhelp.aspx#Drivers">Drivers:</A></TH>' in line:
        drivers = int(''.join(lines[x+1].split('<TD valign=top><FONT style=font-size:80% face=arial color=#0000C0><B>')[1].split('&nbsp;</TD>')[0].split(',')))
    elif '<TH SCOPE="ROW" class="querylabelbkg" align=right><A class="querylabel" href="saferhelp.aspx#">MCS-150 Mileage (Year):</A></TH>' in line:
        mileage = int(''.join(lines[x+1].split('<TD valign=top><FONT style=font-size:80% face=arial color=#0000C0><B>')[1].split(' ')[0].split(',')))


print("")

print("-------------------------")
print("          DATA")
print("-------------------------")

print("USDOT Number: "+usdot_number)
print("Company Name: "+company_name)


print("Power Units: "+str(power_units))
print("Drivers: "+str(drivers))
print("Mileage: "+str(mileage))


print("Inspections Vehicle: "+str(inspections_vehicle))
print("Inspections Driver: "+str(inspections_driver))
print("Inspections Hazmat: "+str(inspections_hazmat))
print("Inspections IEP: "+str(inspections_IEP))


print("OOS Vehicle: "+str(oos_vehicle))
print("OOS Driver: "+str(oos_driver))
print("OOS Hazmat: "+str(oos_hazmat))
print("OOS IEP: "+str(oos_IEP))

print("-------------------------")
print("        ANALYSIS")
print("-------------------------")


if inspections_vehicle == 0:
    oos_rate_vehicle = 0
else:
    oos_rate_vehicle = oos_vehicle / inspections_vehicle

if inspections_driver == 0:
    oos_rate_driver = 0
else:
    oos_rate_driver = oos_driver / inspections_driver

if inspections_hazmat == 0:
    oos_rate_hazmat == 0
else:
    oos_rate_hazmat = oos_hazmat / inspections_hazmat

if inspections_IEP == 0:
    oos_rate_IEP = 0
else:
    oos_rate_IEP = oos_IEP / inspections_IEP

print("OOS Vehicle %: "+str(oos_rate_vehicle))
print("OOS Driver %: "+str(oos_rate_driver))
print("OOS Hazmat %: "+str(oos_rate_hazmat))
print("OOS IEP %: "+str(oos_rate_IEP))


if power_units == 0:
    team_score = 0
else:
    team_score = drivers / power_units

teams_trucks = drivers - power_units

if power_units == 0:
    teams_rate = 0
else:
    teams_rate = teams_trucks / power_units

if power_units == 0:
    mileage_per_truck = 0
else:
    mileage_per_truck = mileage / power_units

if drivers == 0:
    mileage_per_driver = 0
else:
    mileage_per_driver = mileage / drivers

print("Teams Score: "+str(team_score))
print("Teams Trucks: "+str(teams_trucks))
print("Teams %: "+str(teams_rate))

print("Mileage Per Power Unit: "+str(mileage_per_truck))
print("Mileage Per Driver: "+str(mileage_per_truck))
