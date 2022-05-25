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
	json = out.json()

	return json


