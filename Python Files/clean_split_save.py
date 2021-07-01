# %%
from pickle import load
from pickle import dump
from numpy.random import rand
from numpy.random import shuffle

# %%
# load a clean dataset
def load_clean_sentences(filename):
	return load(open(filename, 'rb'))

# %%
# save a list of clean sentences to file
def save_clean_data(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)

# %%
# load dataset
raw_dataset = load_clean_sentences('../PKL Files/english-hieroglpyhic.pkl') # 100 0000

# reduce dataset size
n_sentences = 100000
dataset = raw_dataset[:n_sentences, :]
# random shuffle
shuffle(dataset)
# split into train/test
train, test = dataset[:50000], dataset[50000:]
# save
save_clean_data(dataset, '../PKL Files/english-hiero-both.pkl')
save_clean_data(train, '../PKL Files/english-hiero-train.pkl')
save_clean_data(test, '../PKL Files/english-hiero-test.pkl')

# %%
