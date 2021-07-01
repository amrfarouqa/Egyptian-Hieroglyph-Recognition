# %%
from PIL import Image, ImageFont, ImageDraw, ImageTk
import PIL.Image
import textwrap
try:
    from Tkinter import Label
except ImportError:
    from tkinter import Label

# %%
from random import randint
import numpy as np
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import tensorflow as tf
import keras
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# %%
# load doc into memory
def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# %%
# generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
	result = list()
	in_text = seed_text
	# generate a fixed number of words
	for _ in range(n_words):
		# encode the text as integer
		encoded = tokenizer.texts_to_sequences([in_text])[0]
		# truncate sequences to a fixed length
		encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
		# predict probabilities for each word
		yhat = np.argmax(model.predict_classes(encoded, verbose=0))
		# map predicted word index to word
		out_word = ''
		for word, index in tokenizer.word_index.items():
			if index == yhat:
				out_word = word
				break
		# append to input
		in_text += ' ' + out_word
		result.append(out_word)
	return ' '.join(result)

# %%
# load cleaned text sequences
in_filename = '../Text Files/eng-hg-gardiner.txt'
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1
 
# load the model
model = load_model('../Model Files/model.h5')
 
# load the tokenizer

tokenizer = load(open('../PKL Files/english-hiero-both.pkl', 'rb'))
tokenizer = Tokenizer(num_words=50)

# %%
def truetype_font(font_path, size):
    return ImageFont.truetype(font_path, size)

# %%
class CustomFont_Message_Original(Label):
    def __init__(self, master, text, foreground="black", truetype_font=None, font_path=None, family=None, size=None, **kwargs):   
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")
                
            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)
        
        width, height = truetype_font.getsize(text)

        image = PIL.Image.new("RGBA", (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(image)

        draw.text((0, 0), text, font=truetype_font, fill=foreground)
        
        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

# %%
class CustomFont_Message_Transliterated(Label):
    def __init__(self, master, text, width, foreground="black", truetype_font=None, font_path=None, family=None, size=None, **kwargs):   
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")
                
            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)
    
        lines = textwrap.wrap(text, width=width)

        width = 0
        height = 0
        
        line_heights = []
        for line in lines:
            line_width, line_height = truetype_font.getsize(line)
            line_heights.append(line_height)
            
            width = max(width, line_width)
            height += line_height

        image = PIL.Image.new("RGBA", (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(image)

        y_text = 0
        for i, line in enumerate(lines):
            draw.text((0, y_text), line, font=truetype_font, fill=foreground)
            y_text += line_heights[i]

        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

# %%
class CustomFont_Message_Translated(Label):
    def __init__(self, master, text, width, foreground="black", truetype_font=None, font_path=None, family=None, size=None, **kwargs):   
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")
                
            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)
    
        lines = textwrap.wrap(text, width=width)

        width = 0
        height = 0
        
        line_heights = []
        for line in lines:
            line_width, line_height = truetype_font.getsize(line)
            line_heights.append(line_height)
            
            width = max(width, line_width)
            height += line_height

        image = PIL.Image.new("RGBA", (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(image)

        y_text = 0
        for i, line in enumerate(lines):
            draw.text((0, y_text), line, font=truetype_font, fill=foreground)
            y_text += line_heights[i]

        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

# %%
class CustomFont_Message_Gardiner(Label):
    def __init__(self, master, text, width, foreground="black", truetype_font=None, font_path=None, family=None, size=None, **kwargs):   
        if truetype_font is None:
            if font_path is None:
                raise ValueError("Font path can't be None")
                
            # Initialize font
            truetype_font = ImageFont.truetype(font_path, size)
    
        lines = textwrap.wrap(text, width=width)

        width = 0
        height = 0
        
        line_heights = []
        for line in lines:
            line_width, line_height = truetype_font.getsize(line)
            line_heights.append(line_height)
            
            width = max(width, line_width)
            height += line_height

        image = PIL.Image.new("RGBA", (width, height), color=(0,0,0,0))
        draw = ImageDraw.Draw(image)

        y_text = 0
        for i, line in enumerate(lines):
            draw.text((0, y_text), line, font=truetype_font, fill=foreground)
            y_text += line_heights[i]

        self._photoimage = ImageTk.PhotoImage(image)
        Label.__init__(self, master, image=self._photoimage, **kwargs)

# %%
from tkinter import *
from tkinter.font import Font
import html

# select a seed text
seed_text = lines[randint(0,len(lines))]
split_string = seed_text.split("\t")

original_text = split_string[0]
gardiner_text = split_string[1]
text_for_transliteration = split_string[0]

text_for_translation = split_string[1]
glyph_for_translation = gardiner_text
glyph_for_transliteration = original_text

for r in ((" ", " "), ("G01", "A"), ("M170", "B"), ("Z4", "C"), ("M17A", "D"), ("D36", "E"), ("G43", "F"), ("D058", "G"), ("Q3", "H"), ("I9", "I"), ("G17", "J"), ("N35", "K"), ("D21", "L"), ("O4", "M"), ("V28", "N"), ("AA1", "O"), ("F32", "P"), ("O34", "Q"), ("S29", "R"), ("N37", "S"), ("N29", "T"), ("V31", "U"), ("W11", "V"), ("X1", "W"), ("V13", "X"), ("D46", "Y"), ("I10", "Z")):
    text_for_translation = text_for_translation.replace(*r)

for r in ((" ", " "), ("G01", "&#78143;"), ("M170", "&#78283;"), ("Z4", "&#78829;"), ("M17A", "&#78284;"), ("D36", "&#77981;"), ("G43", "&#78193;"), ("D058", "&#78016;"), ("Q3", "&#78506;"), ("I9", "&#78225;"), ("G17", "&#78163;"), ("N35", "&#78358;"), ("D21", "&#77963;"), ("O4", "&#78420;"), ("V28", "&#78747;"), ("AA1", "&#78861;"), ("F32", "&#78113;"), ("O34", "&#78467;"), ("S29", "&#78580;"), ("N37", "&#78361;"), ("N29", "&#78350;"), ("V31", "&#78753;"), ("W11", "&#78780;"), ("X1", "&#78799;"), ("V13", "&#78719;"), ("D46", "&#77991;"), ("I10", "&#78227;")):
    glyph_for_translation = glyph_for_translation.replace(*r)

for r in ((" ", " "), ("A", "&#78143;"), ("B", "&#78283;"), ("C", "&#78829;"), ("D", "&#78284;"), ("E", "&#77981;"), ("F", "&#78193;"), ("G", "&#78016;"), ("H", "&#78506;"), ("I", "&#78225;"), ("J", "&#78163;"), ("K", "&#78358;"), ("L", "&#77963;"), ("M", "&#78420;"), ("N", "&#78747;"), ("O", "&#78861;"), ("P", "&#78113;"), ("Q", "&#78467;"), ("R", "&#78580;"), ("S", "&#78361;"), ("T", "&#78350;"), ("U", "&#78753;"), ("V", "&#78780;"), ("W", "&#78799;"), ("X", "&#78719;"), ("Y", "&#77991;"), ("Z", "&#78227;"), ("a", "&#78143;"), ("b", "&#78283;"), ("c", "&#78829;"), ("d", "&#78284;"), ("e", "&#77981;"), ("f", "&#78193;"), ("g", "&#78016;"), ("h", "&#78506;"), ("i", "&#78225;"), ("j", "&#78163;"), ("k", "&#78358;"), ("l", "&#77963;"), ("m", "&#78420;"), ("n", "&#78747;"), ("o", "&#78861;"), ("p", "&#78113;"), ("q", "&#78467;"), ("r", "&#78580;"), ("s", "&#78361;"), ("t", "&#78350;"), ("u", "&#78753;"), ("v", "&#78780;"), ("w", "&#78799;"), ("x", "&#78719;"), ("y", "&#77991;"), ("z", "&#78227;")):
    glyph_for_transliteration = glyph_for_transliteration.replace(*r)    
    
transliterated_glyphs = html.unescape(glyph_for_transliteration)
translated_glyphs = html.unescape(glyph_for_translation)

print('Original Target Text:  '+ original_text)  
print('Transliterated Glyph:  '+ transliterated_glyphs) 
print('Source Gardiner Text:  '+ gardiner_text) 
print('Translated Predicted Text:  '+ text_for_translation)   
print('Translated Predicted Glyph:  '+ translated_glyphs)   
  

if __name__ == "__main__":
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
        
    root = Tk()
    root.title('Egyptian Hieroglyphic Recognition: Transliteration Technique Vs. Translation Analysis')
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))

    # Define our font
    bigFont = Font(
        family="Helvetica",
        size=30,
        weight="bold",
        slant="roman",
        underline=0,
        overstrike=0)

    
    my_label_Original = Label(root, text="Original",  font=bigFont)
    my_label_Original.pack(pady=20)
    CustomFont_Message_Original(root, text=original_text, font_path="../Building Font/Font Files/Nimbus-Sans.ttf", size=55).pack(pady=(30,30))
    
    my_label_Transliterated = Label(root, text="Transliterated",  font=bigFont)
    my_label_Transliterated.pack(pady=20)
    CustomFont_Message_Transliterated(root, text=text_for_transliteration, width=50, font_path="../Building Font/Font Files/Hieroglyphicextended-Regular.ttf", size=55).pack(pady=(30,30))
    
    my_label_Translated = Label(root, text="Translated",  font=bigFont)
    my_label_Translated.pack(pady=20)
    CustomFont_Message_Gardiner(root, text=gardiner_text, width=50, font_path="../Building Font/Font Files/Helvetica.ttf", size=55).pack(pady=(30,30))
    CustomFont_Message_Translated(root, text=text_for_translation, width=50, font_path="../Building Font/Font Files/Hieroglyphicextended-Regular.ttf", size=55).pack(pady=(30,30))
    
    root.mainloop()

# %%
