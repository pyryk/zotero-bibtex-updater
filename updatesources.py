import requests
import bibtexparser
import json

def get_credentials():
	configfile = open('zotero.json', 'r')
	config = json.load(configfile)
	return config

def get_sources(user, key, offset, limit):
	r = requests.get('https://api.zotero.org/users/{0}/items/top?format=bibtex&start={1}&limit={2}&key={3}'.format(user, offset, limit, key))
	return r.text.encode('utf-8')

def get_all_sources():
	config = get_credentials()
	start = 0
	limit = 100
	chunks = [get_sources(config['user'], config['key'], start, limit)]
	while len(bibtexparser.loads(chunks[-1]).entries) == limit:
		start += limit
		# print('Chunk {0} full, getting another one with items {1}-{2}'.format(len(chunks), start, start+limit))
		chunks.append(get_sources(config['user'], config['key'], start, limit))
	print('Successfully fetched {0} items.'.format((len(chunks)-1) * limit + len(bibtexparser.loads(chunks[-1]).entries)))
	return '\n'.join(chunks)

# print(get_all_sources())

f = open('sources.bib', 'w')
f.write(get_all_sources())