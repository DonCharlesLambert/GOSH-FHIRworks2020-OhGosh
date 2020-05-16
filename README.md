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

![enter image description here](https://lh3.googleusercontent.com/btqv1GfMtulJoOr_LfwcC5rQmJxLKIA_AIA8fOQ-WRNkQGXvXwlMsM8XuJtPkqNWS_p-BQCjYwHtR1KQ-OJ6OGfbYhN5CupBAW0t6NiWWI2zP0T4xMn77RScwR_TZbFu_Svw1zVHwPYiG96dpTHpP_6pRH6p582O9_Xm6Tbr5T2N9Dqcj0Erx6WCPb6vLWv5Js5_Ki0pgD5vKKwZ-t2KmFeFnufq7EUgKZiL_Ld9XobaC0mBKC1Kr1XAgOG775nM2q6OId7of1dkX-6cOb82Eze04wxFnyPQ-eP_azw5OJ6va2_1FwEuGaCyqMM4YMJmSXItxzE1fsYV9ROROvOe7w0lv78FkMSOSajPJwQz7yz9Wzuro9FgUMovd-q_sNZxqXglLeebyxVbTbXYmtl_hRnfBFgCOZsqakGs2QcAHd-iDbXRpiXsvIS3Z0cykshnfuZ_xe4fzvsOB_sHlkbfHzyWe2_04690i-iG_T-5yh4quI0uQtZpbg6wpBMXVFusC6KfGVvsJ8Akc6h7_Rr_sBTJyjECBiwmvU9NVu9h8o6z-HDGcS4Hh_BwUaPqBVQhZVBwkI1u8yqJF0XpTmpHZsylqjVFskKLySHRQTQSpMK4ge-SKn8drKMXJUwp3Frt8ry05ojOXl8Pga-mZlxIwvJPkJXGWpLlSTV_gd6NK7kE5LYyQi9JzeOkfRAdVQ=w1337-h891-no?authuser=0)

## File Structure
Water - An API for visualisation of data obtained from FHIR/Fire  
Earth - Provides constants used in all classes  
Fire - Utilises the fhir_parser API to collected patient data and run operations on this data  
Air - Provides a demonstration of how Water can be used in applications (Run this!)  
