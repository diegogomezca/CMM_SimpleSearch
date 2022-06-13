import argparse
import requests
import json

def myEntryPoint(query_type, atabases, masses_mode, ion_mode, adducts, tolerance, tolerance_mode, masses)):
	if(query_type == "SIMPLE_SEARCH"):
		return simple_search(json_data)
	else if(query_type == "BATCH:_SEARCH"):
		# CAMBIAR A BATCH SEARCH return simple_search(json_data)

def simple_search(metabolites_type, databases, masses_mode, ion_mode,adducts,tolerance,tolerance_mode,masses):

	print(metabolites_type, databases, masses_mode, ion_mode,adducts,tolerance,tolerance_mode,masses)

	url = "http://ceumass.eps.uspceu.es/mediator/api/v3/batch"
	x = {
	"metabolites_type": "all-except-peptides",
	"databases": ["hmdb"],
	"masses_mode": "mz",
	"ion_mode": "positive",
	"adducts": ["all"],
	"tolerance": 10.0,
	"tolerance_mode": "ppm",
	"masses": [400.3432]
	}

	out = requests.post(url,json = x)
	# No se puede asumir que es correcto
	print(out.status_code)

	json = out.json()

	return json


def main():
	


	parser = argparse.ArgumentParser(description='CEU Mass Mediator is a tool for searching metabolites in different databases')

	parser.add_argument('--version', action='version', version='1.0')
	parser.add_argument("metabolites_type", type=str)
	parser.add_argument("databases", type=str)
	parser.add_argument("masses_mode", type=str)
	parser.add_argument("ion_mode", type=str)
	parser.add_argument("adducts", type=str)
	parser.add_argument("tolerance", type=float)
	parser.add_argument("tolerance_mode", type=str)
	parser.add_argument("masses", type=float)

	args = parser.parse_args()
	# SWITCH CASE CON QUERY TYPE 
	outjson = simple_search(args.metabolites_type,args.databases,args.masses_mode,args.ion_mode,args.adducts,args.tolerance,args.tolerance_mode,args.masses)

	return(outjson)

if __name__ == '__main__':
    main()