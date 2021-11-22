import capitalize

text ="Welcome to New York."
text2= text.capitalize()
print(text2)
a = '.'

letra=text[len(text2)-1]



if letra == a:
    text2 =(text2)
else:
    text2=f'{text2}{a}'

print(text2)
