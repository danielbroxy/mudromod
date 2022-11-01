init python:
    mods["mudromod"] = "Мудромод"
    tih = Character (u'Тихомир-тян', color="FFFF00", what_color="E2C778")
    ted = Character (u'Унабомбер', color="00ff0d", what_color="E2C778")

label mudromod:
    $ save_name = ('Мудромод. Пролог')
    #$ set_mode_adv()
    #$ reload_names()
    #$ backdrop = "prologue"
    #$ new_chapter(-1, translation_new["prologue"])
    #$ prolog_time()
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    $ renpy.pause(3)
    scene anim prolog_1
    with fade3
    window show
    "Офисный гул — это душа офиса. "
    "Стучание клавиш, шум компьютеров и речь о всё новых способах закабалить свой разум оптимизацией кода это пустота, истинный смысл всего что мы здесь делаем. "
    "Порой мне хочется проломить монитор, раздробить клавиатуры и сложить из букв нелицеприятные выражения.{w} Бить стёкла и рвать бумаги из принтеров в клочья.{w} Разлить бутыль кулера.{w} Проломить стеклопакеты навороченными игровыми креслами. "
    "Мне кажется, так я вмиг стану живее их всех. "
    "Внутри у них не мясные потроха, как было раньше, а пух и шестерёнки. "
    stop music fadeout 5
    "Они куклы, роботы. "
    window hide
    scene bg black
    with fade3
    $ renpy.pause(2)
    play sound_loop sfx_keyboard_mouse_computer_noise fadein 3
    scene anim 1_prologue
    with fade3
    $ renpy.pause(9.4, hard=True)
    scene anim 2_prologue
    with fade3
    $ renpy.pause(9.4, hard=True)
    scene anim 3_prologue
    with fade3
    $ renpy.pause(6.2, hard=True)
    window show
    "Когда кто-то открывает рот рядом со мной мне хочется взглянуть им в самую глубь глотки."
    "Что там, если не динамики и выпитый энергетик с парами никотиновой жидкости?"
    window hide
    show blinking with dissolve
    $ renpy.pause(3.5)
    window show
    "Они питаются шоколадом и энергетиками.{w} Они дышат жижками от пода. "
    "На перекуре я держусь в стороне.{w} Спасает лишь то, что многие здесь, как и я - не особо разговорчивые. "
    window hide
    hide blinking
    $ renpy.pause(3)
    scene anim prolog_15
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_3
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_4
    with fade
    $ renpy.pause(3, hard=True)
    stop sound_loop fadeout 4
    window show
    "Наша келья, наша община не вольных кодеров убогое зрелище.{w} Загвоздка только в том, что нынче всё стало таким. "
    window hide
    $ renpy.pause(3)
    scene anim prolog_5
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_14
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_11
    with fade
    $ renpy.pause(3, hard=True)
    play music music_list["farewell_to_the_past_edit"] fadein 5
    $ renpy.pause(3)
    scene anim prolog_2
    with fade
    $ renpy.pause(1)
    $ set_mode_nvl()
    window show
    "Киберпанк придумали японцы. Реализовывать его, по-видимому, взялись цыгане. "
    "Город - нагромождение цветных и абсолютно безвкусных вывесок. Шум автоблядей и мотохрустов. "
    "2040 не год, а тонны дерьма, вылившиеся вокруг меня. "
    "Я иду по тротуару, меня едва не сбило самокатом. 4 раза. И так каждый день. "
    "Облака пара окружают меня как сырой болотный туман. Они все помешались на этом. "
    "Я мечтаю открыть дверь дома. Поскорее бы прийти. Не то чтобы мне там нравится."
    "Моя квартира-студия есть келья. Келья монаха 2040 года. "
    "Моя морозилку не терпит полуфабрикаты, как и я сам. На моей работе я насмотрелся на самые разные виды карательной кулинарии. "
    "Эти котлеты, которые становятся ещё хуже после микроволновки. В них соя и мясо жуков. Их вонь донимает меня. "
    "Только дома я могу насладиться запахом нормальной пищи. "
    nvl clear
    window hide
    scene bg semen_room_window
    with fade
    stop music fadeout 4
    play sound_loop sfx_street_traffic_outside fadein 2
    $ renpy.pause(3)
    window show
    "Я мечтаю открыть дверь дома. Поскорее бы прийти. Не то чтобы мне там нравится."
    "Моя квартира-студия есть келья. Келья монаха 2040 года. "
    "Моя морозилку не терпит полуфабрикаты, как и я сам. На моей работе я насмотрелся на самые разные виды карательной кулинарии. "
    "Эти котлеты, которые становятся ещё хуже после микроволновки. В них соя и мясо жуков. Их вонь донимает меня. "
    "Только дома я могу насладиться запахом нормальной пищи. "
    "Но сегодня мне не хочется есть. "
    window hide
    $ renpy.pause(4)
    stop sound_loop fadeout 3
    play ambience ambience_cold_wind_loop fadein 3
    $ set_mode_adv()
    play sound sfx_intro_bus_stop_steps
    scene anim intro_1
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_2
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_3
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_4
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_5
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_6
    with fade
    $ renpy.pause(3, hard=True)
    play sound sfx_intro_bus_stop_sigh
    scene anim intro_8
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_7
    with fade
    $ renpy.pause(3, hard=True)
    scene bg bus_stop
    with fade
    window show
    return



