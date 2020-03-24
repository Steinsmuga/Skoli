#FORR1FG05AU-Hát - Tímaverkefni3B - Steinn Þorkelsson
choice = 0
while choice != "5":
    print('1. Liður 1')
    print('2. Liður 2')
    print('3. Liður 3')
    print('4. Liður 4')
    print('5. hætta')
    choice = input('Veldu Tölu: ')

    if choice == "1":
        items = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
        dup_items = set()

        for x in items:
            if x not in dup_items:
                dup_items.add(x)

        print(f"Með duplicates: {items}")
        print(f"Án duplicates:  {dup_items}")

    if choice == "2":
        original_list = ["Banani", "Epli", "Rauðrófa", "Vínber"]
        cloned_list = list(original_list)

        print(f"Original ávextir: {original_list}")
        print(f"Cloned ávextir: {cloned_list}")

    if choice == "3":
        litir = ['Rauður', 'Grænn', 'Hvítur', 'Svartur', 'Bleikur', 'Gulur']
        new_litir = [x for (i, x) in enumerate(litir) if i not in (0, 4, 5)]

        print(litir)
        print(new_litir)

    if choice == "4":
        tolur = [7, 8, 120, 25, 44, 20, 27]
        new_tolur = [x for x in tolur if x % 2 != 0]

        print(f"Með Sléttum tölum: {tolur}")
        print(f"Án Sléttum Tölum: {new_tolur}")
