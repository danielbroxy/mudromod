init python:
    mods["mudromod"] = "Мудромод"
    tih = Character (u'Тихомир-тян', color="FFFF00", what_color="E2C778")
    ted = Character (u'Унабомбер', color="00ff0d", what_color="E2C778")

label mudromod:
    $ save_name = ('Мудромод. Пролог')
    scene bg sloboda
    with dissolve
    show tih normal with dissolve
    tih "Хорошо сосёт, нежно... Очень жадна до члена"
    "Судя по всему, эта слобода – единственое место, где могли быть люди, поэтому я решил пойти туда и уже почти дошёл до ворот, как..."
    "Оттуда выглянула дедушка..."
    menu:
        "ТРАХНУТЬ":
            me "ТРАХ ПРОШЕЛ УСПЕШНО"
        "Нет (почему?)":
            me "СОБАЧЬЯ СРАКА!!!"
    show ted normal at left with dissolve
    ted "The Industrial Revolution and its consequences have been a disaster for the human race"
    return



