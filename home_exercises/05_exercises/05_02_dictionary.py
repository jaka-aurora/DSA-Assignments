fi_en_dict = {
    'kissa': 'cat',
    'koira': 'dog',
    'maa': 'country',
    'kieli': 'language',
    'aikasarja': 'time series',
    'tila': 'status',
    'tuote': 'product',
    'palvelin': 'server',
    'salasana': 'password'
}

print(fi_en_dict)

search_word = input("Give a Finnish Word: ")

def fin_en():
    for key in fi_en_dict:
        if key == search_word:
            print(fi_en_dict.keys())
        else:
            "Word not found"


print(input("Give a Finnish Word: "))
