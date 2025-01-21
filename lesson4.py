def generate_fairy_tale():
    hero = input("Введите имя героя: ")
    place = input("Введите место действия: ")
    artifact = input("Введите волшебный предмет: ")
    villain = input("Введите имя злодея: ")

    tale = (f"Жил-был {hero} в далеком {place}. Однажды он нашел {artifact}, но {villain} хотел его украсть. "
            f"Храбрый {hero} преодолел испытания, победил {villain} и вернулся домой с {artifact}, "
            f"принеся мир и радость в {place}.")

    print("\nВот ваша сказка:\n" + tale)


# Запуск генератора сказки
generate_fairy_tale()
