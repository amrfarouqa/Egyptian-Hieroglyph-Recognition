# %%
import string
import re
from pickle import dump
from unicodedata import normalize
from numpy import array

# %%
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, mode='rt', encoding='utf-8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# %%
# split a loaded document into sentences
def to_pairs(doc):
	lines = doc.strip().split('\n')
	pairs = [line.split('\t') for line in  lines]
	return pairs

# %%
# clean a list of lines
def clean_pairs(lines):
	cleaned = list()
	for pair in lines:
		clean_pair = list()
		for line in pair:
			clean_pair.append(''.join(line))
		cleaned.append(clean_pair)
	return array(cleaned)

# %%
# save a list of clean sentences to file
def save_clean_data(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)

# %%
# load dataset
filename = '../Text Files/eng-hg-gardiner.txt'
doc = load_doc(filename)
# split into english-hieroglyph pairs
pairs = to_pairs(doc)
# clean sentences
clean_pairs = clean_pairs(pairs)
# save clean pairs to file
save_clean_data(clean_pairs, '../PKL Files/english-hieroglpyhic.pkl')
# spot check
for i in range(100):
	print('[%s] => [%s]' % (clean_pairs[i,0], clean_pairs[i,1]))

# %%
