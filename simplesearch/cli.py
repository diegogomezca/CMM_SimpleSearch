import argparse
import requests
import json

def simple_search(metabolites_type, databases, masses_mode, ion_mode,adducts,tolerance,tolerance_mode,masses):

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

	return out.text


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

	out = simple_search(args.metabolites_type,args.databases,args.masses_mode,args.ion_mode,args.adducts,args.tolerance,args.tolerance_mode,args.masses)
	
	print("hola")
	
	#return out

if __name__ == '__main__':
    main()
