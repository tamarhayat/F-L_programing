gimatria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50, 
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 
    'ר': 200, 'ש': 300, 'ת': 400
}


def sum(l,i):
    if i==len(l):
        return 0
    return l[i]+sum(l,i+1)

def get_num(letter):
    return gimatria.get(letter)

def get_gimatria_value(mystr):
    return sum(list(map(get_num ,mystr)),0)


#print(get_gimatria_value("שלום"))