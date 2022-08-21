# usdot_fmcsa_saferweb_tool

## What it does:
This is a web scraper that takes a USDOT Number for a motor carrier and gets information from the Federal Motor Carrier Safety Administration (FMCSA)'s SAFERWeb portal about that motor carrier. It uses that information to calculate some things about it.

Teams Score: Represents likelihood a company runs "Teams" trucks
Teams Trucks: Approximation of number of trucks owned by a company are driven by a team of two drivers.
Teams %: Approximation of the percentage of trucks owned by a company are drivven by a team of two drivers.

## Why?
It can be difficult to get accurate information from recruiters at motor carriers. There are a few small pieces of information which can be obtained directly from the the Federal Motor Carrier Safety Administration which can be a factor in choosing which motor carrier to work for. Two pieces of information are critical to the decision making process:

1.) How many miles can I expect to get working here?
2.) Will I be pressured to drive teams at this company? / Will I have the opportunity to drive teams at this company?

Why take a recruiter's word for it, when you can look it up yourself instantly?

The FMCSA's SAFERWeb portal also helps you determine the professionalism level of a motor carrier. How well do they take care of their equipment? How likely are their drivers to be put out of service?

## How to run:

Run the pythonscript with input argument of USDOT number for the company you want data for.

ex:

python3 saferweb_parser.py 3706

## Note:

This uses curl, and os.system() -- Originally written on Ubuntu 22.04. Presumes curl and python are installed and you have read/write permissions in the directory you're running it from.

the command: 
  
  curl -s "http://...html" > temporary_html.html
  
 Will need to run on your OS.
  

## Example Output:

<pre>
https://safer.fmcsa.dot.gov/query.asp?searchtype=ANY&query_type=queryCarrierSnapshot&query_param=USDOT&query_string=3706

-------------------------
          DATA
-------------------------
USDOT Number: 3706
Company Name: NEW PRIME INC
Power Units: 7335
Drivers: 9501
Mileage: 842696419
Inspections Vehicle: 8177
Inspections Driver: 15330
Inspections Hazmat: 154
Inspections IEP: 0
OOS Vehicle: 693
OOS Driver: 197
OOS Hazmat: 4
OOS IEP: 0
-------------------------
        ANALYSIS
------------------------
OOS Vehicle %: 0.08474990827932004
OOS Driver %: 0.012850619699934769
OOS Hazmat %: 0.025974025974025976
OOS IEP %: 0
Teams Score: 1.2952965235173823
Teams Trucks: 2166
Teams %: 0.2952965235173824
Mileage Per Power Unit: 114887.03735514656
Mileage Per Driver: 114887.03735514656
</pre>
