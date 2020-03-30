import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


def csvfile(datafile):
	df = pd.read_json(datafile)
	df.to_csv("../data/covid19.csv")

def get_region(regions, region):
	df = pd.read_csv(regions)
	lst = df.loc[lambda df: df['denominazione_regione'] == region]
	idx = np.arange(len(lst))
	lst = lst['totale_casi']
	print(lst.values)
	r = pd.DataFrame(lst.values, index=idx, columns =['totale_casi']) 
	return r
	
def graphs(regfile, regions, dois):
	colors = ['red', 'green', 'blue', 'yellow', 'cyan',  'orange']
	df = pd.read_csv(regfile)
	c = 0
	shows = []
	for region in regions:
		regcol = df.loc[lambda df: df['denominazione_regione'] == region]
		date = regcol['data']
		data = regcol [dois]
		#plt.legend(regions)
		plt.plot(date, data, color=colors[c])
		shows.append(colors[c])
		c = (c + 1) %  len(colors)
	plt.show()
	return

def graph(datafile):
	df = pd.read_json(datafile)
	plt.figure()
	plt.plot(df['totale_casi'])
	plt.plot(df['dimessi_guariti'])
	plt.plot(df['deceduti'])
	plt.title("COVID-19 Italia")
	plt.show()
	return
	
def world(url, country):
	df = pd.read_csv(url)
	buf = df.loc[lambda df: df['Country'] == country]
	data = buf['Confirmed']
	date = buf['Date']
	plt.plot(date, data)
	plt.title(country)
	buf = df.loc[lambda df: df['Country'] == 'Italy']
	data = buf['Confirmed']
	plt.plot(date, data)
	buf = df.loc[lambda df: df['Country'] == 'Korea, South']
	data = buf['Confirmed']
	plt.plot(date, data)
	
	plt.legend([country, 'Italy', 'Korea, South'])
	
	plt.show()
	return

def model(datafile, regions, region):
	r = get_region(regions, region)
	#print(r)
	df = pd.read_json(datafile)
	k = 0.355
	x = np.arange(len(df['totale_casi']))
	#print(x)
	plt.figure()
	plt.plot(df['totale_casi'])
	plt.plot(np.exp(k * x))
	plt.title("Modello COVID-19")
	plt.figure()
	plt.plot(r)
	k = 0.23
	plt.plot(np.exp(k * x))
	plt.title(region)
	plt.show()
	
	

#regfile = "dpc-covid19-ita-regioni.csv"
#datafile = "dpc-covid19-ita-andamento-nazionale.json"
regfile = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv"
datafile = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
worldurl = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
regions = ["Campania","Lombardia"]
dois = ["totale_casi","deceduti"]
region = "Campania"
country = 'China'
csvfile(datafile)
#graph(datafile)
model(datafile, regfile, region)
#graphs(regfile, regions, dois)
#world(worldurl, country)
