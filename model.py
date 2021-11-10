import fitz

# location = './cv_docs/' +

doc = fitz.open("./cv_docs/shaji.pdf")

def make_text(words):
    """Return textstring output of get_text("words").
    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
    line_dict = {}  # key: vertical coordinate, value: list of words
    words.sort(key=lambda w: w[0])  # sort by horizontal coordinate
    for w in words:  # fill the line dictionary
        y1 = round(w[3], 1)  # bottom of a word: don't be too picky!
        word = w[4]  # the text of the word
        line = line_dict.get(y1, [])  # read current line content
        line.append(word)  # append new word
        line_dict[y1] = line  # write back to dict
    lines = list(line_dict.items())
    lines.sort()  # sort vertically
    return "\n".join([" ".join(line[1]) for line in lines])


# doc = fitz.open("search.pdf")  # any supported document type
page = doc[0]  # we want text from this page

"""
-------------------------------------------------------------------------------
Identify the rectangle.
-------------------------------------------------------------------------------
"""
rect = page.first_annot.rect  # this annot has been prepared for us!
# Now we have the rectangle ---------------------------------------------------

"""
Get all words on page in a list of lists. Each word is represented by:
[x0, y0, x1, y1, word, bno, lno, wno]
The first 4 entries are the word's rectangle coordinates, the last 3 are just
technical info (block number, line number, word number).
The term 'word' here stands for any string without space.
"""

words = page.get_text("words")  # list of words on page

"""
We will subselect from this list, demonstrating two alternatives:
(1) only words inside above rectangle
(2) only words insertecting the rectangle
The resulting sublist is then converted to a string by calling above funtion.
"""

# ----------------------------------------------------------------------------
# Case 1: select the words *fully contained* in the rect
# ----------------------------------------------------------------------------
mywords = [w for w in words if fitz.Rect(w[:4]) in rect]

print("Select the words strictly contained in rectangle")
print("------------------------------------------------")
print(make_text(mywords))

# ----------------------------------------------------------------------------
# Case 2: select the words *intersecting* the rect
# ----------------------------------------------------------------------------
mywords = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]

print("\nSelect the words intersecting the rectangle")
print("-------------------------------------------")
print(make_text(mywords))