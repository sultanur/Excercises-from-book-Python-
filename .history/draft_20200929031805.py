
#!/usr/bin/python3
import re
import string

def remove_authors_name():
      
    text = open("article.txt", 'r').read()
    output = text
    names = (open("new_file.txt", 'r').read()) 
    output = output.replace(names, '_' *len(names)) 
    print(output)
    #list = [re.sub(names, ' ', i) for i in text]
    #open("edited_article.txt", 'w').writelines(output)
    #print(open("edited_article.txt", 'r').read())

remove_authors_name()