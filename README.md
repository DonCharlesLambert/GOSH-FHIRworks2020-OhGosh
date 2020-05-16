# Oh Gosh

## Introduction
Provides a demonstration of how an API can be used in to visualise and display FHIR records.  

Note: This README was updated after the 22nd March (On the 16th May) after I noticed that I had not included how to run the application in the README.

## Get it Running
1. Open Terminal  
`C:\>` 
2. Clone the repository  
`C:\> git clone https://github.com/DonCharlesLambert/GOSH-FHIRworks2020-OhGosh`
3. Install the required libraries  
`C:\GOSH-FHIRworks2020-OhGosh\> pip install -r requirements.txt`
4. Run the application  
`C:\GOSH-FHIRworks2020-OhGosh\> python air.py`

![Screenshot from application](https://github.com/DonCharlesLambert/GOSH-FHIRworks2020-OhGosh/blob/master/img/ss.png?raw=true)

## File Structure
Water - An API for visualisation of data obtained from FHIR/Fire  
Earth - Provides constants used in all classes  
Fire - Utilises the fhir_parser API to collected patient data and run operations on this data  
Air - Provides a demonstration of how Water can be used in applications (Run this!)  
