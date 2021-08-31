book.objects.filter(title__search='Harry')
steps performing inbuilt.
i.creates a to_tsvector in the database from the title
ii.creates a plainto_tsquery from the search term 'Harry'

Parsing Queries - plainto_tsquery
1. to_tsquery and plainto_tsquery


plainto_tsquery

1. The text is parsed and normalized
2. plainto_tsquery escapes all the character and places '&'
   between words
3. plainto_tsquery cannot recognize Boolean operators,      weight labels or prefix-match labels in its input


Trigram (or Trigraph) Concepts
1. group of three consecutive character taken from a string
2. measure the similarity of two strings by counting the no of trigrams they share

Example:
string "cat" "is", "ca", "cat" and "at"


