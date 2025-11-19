# example, list inside a dictionary
book = {
    "name":  "My Lady Jane",
    "year":  2016,
    "authors": ["Cynthia Hand", "Brodi Ashton", "Jodi Meadows"]
}

# getting authors list
authors = book['authors']
first_author = authors[0]
print(first_author)

# approach 2: you can also chain these if you want
# authors => first index
print(book['authors'][0])
print()

# if you need to loop through all of the authors
for author in book['authors']:
    print(author)