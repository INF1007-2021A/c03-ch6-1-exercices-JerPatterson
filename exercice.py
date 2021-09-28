#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = list(map(str, input('Entrez dix valeurs: ').split()))
        values = values[:10]
    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = sorted( list( map(str, input('Entrez deux mots: ').split()) ) )
    word1 , word2 = set(words[0]) , set(words[1])
    return True if len(word1.difference(word2)) == 0 else False


def contains_doubles(items: list) -> bool:
    number_ofItems = len(items)
    number_noDuplicates = len(set(items))
    return True if number_ofItems != number_noDuplicates else False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    class_best = {}
    averages = []
    names = []
    for student, tests in student_grades.items() :
        number_ofTests = len(tests)
        grades_sum = 0
        for grades in tests :
            grades_sum += grades
        average = grades_sum / number_ofTests
        averages.append(average)
        names.append(student)
    best_average = max(averages)
    best_student = names[averages.index(best_average)]   
    class_best[best_student] = best_average

    return class_best


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    with5_appearence = {}
    letters = set(sentence)
    characters = list(sentence)
    for letter in letters :
        appearence = characters.count(letter)
        if appearence > 5 :
            with5_appearence[letter] = appearence
        else : 
            continue
    with5_appearence = dict(sorted(with5_appearence.items(), key=lambda index: index[1], reverse=True))
    print(with5_appearence)
    return with5_appearence


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
