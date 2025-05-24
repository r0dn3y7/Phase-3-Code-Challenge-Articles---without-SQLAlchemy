from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Create Author
author = Author("Roddy Dangerfield")
author.save()

# Create Magazine
magazine = Magazine("Tech Roast", "Comedy")
magazine.save()

# Create Article
article = Article("Why My Code Gets No Respect", "It’s full of bad practices.", author.id, magazine.id)
article.save()

# Test associations
print([a.title for a in author.articles()])
print([m.name for m in author.magazines()])
print([a.name for a in magazine.contributors()])
