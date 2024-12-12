#### Imports et définition des variables globales
"""
hsdfkjqhdfkjqhfkjhqf
"""



FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', buffering=-1, encoding="utf8") as opened :

        for line in opened :
            l.append([ int(number)  for number in line.strip().split(';')  ])


    return l

def get_list_k(data, k):
    """,ndksnvsjnsjnsdjdnfksdj"""
    return data[k]

def get_first(l):
    """kjkshkjsdhvkshvvkjsdh"""
    return l[0]

def get_last(l):
    """jsdfkjsdhfkjsdhfkjsdhvkj"""
    return l[-1]

def get_max(l):
    """sjdhjshfsdfisdhfsdhf"""
    return max(l)

def get_min(l):
    """hsdjhskjfhskjfhskjfhskj"""
    return min(l)

def get_sum(l):
    """jskdhfkjhfkjdhfkjwdhfsdh"""
    somme = 0
    for i in l :
        somme += i
    return somme


#### Fonction principale


def main():
    """
    isfkjsdfkjdnfkjdfkjdshf
    """

    data = read_data(FILENAME)
    # for i, l in enumerate(data):
    #     print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
