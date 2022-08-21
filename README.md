# usdot_fmcsa_saferweb_tool

## How to run:

Run the pythonscript with input argument of USDOT number for the company you want data for.

ex:

python3 saferweb_parser.py 3706

## Note:

This uses curl, and os.system() -- Originally written on Ubuntu 22.04. Presumes curl and python are installed and you have read/write permissions in the directory you're running it from.

the command: 
  
  curl -s "http://...html" > temporary_html.html
  
 Will need to run on your OS.
  



