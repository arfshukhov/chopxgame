# Вы можете расположить сценарий своей игры в этом файле.    
        
# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define p = Character("Поздняков", color="#cf8cc8")
define gg = Character("Вы", color="#148800")
#define current_label = None
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",

# Игра начинается здесь:


init:
    $ current_label = None
    #$ empty_inventory_slots = 4


label start:
    
    show img1:
        xsize 1920
        ysize 1080

    play sound "audio/Поздняков_о_ЗАЭС.ogg"

    "Пролог..."

    stop sound

    scene clock_5:
        xsize 1920
        ysize 1080

    
    gg "Да... Вшивый о бане, а Поздняк как обычно о ядерке."
    gg "Уже светает, пора бы уже лечь спать"

    hide clock_5


label conflict_preambule:

    play music "SCP-x6x.mp3" volume 0.5

    show black_screen

    "Проходит 2 месяца..." with fade

    hide black_screen 

    show natovsbrics 

    "Обстановка в мире напряженная. Нередко случаются стычки между НАТО и военной коалицией стран БРИКС." with fade

    hide natovsbrics

    show img2:
        xsize 1920
        ysize 1080

    "Столкновения происходят на нейтральных территориях третьих стран, но ни одна из сторон не признает своего участия в боевых действиях." with fade

    hide img2

    show img3:
        xsize 1920
        ysize 1080

    "Стороны все еще хотят спустить конфликт на тормозах, но даже людям, не особо смыслящим о политике, давно понятно, 
    что конфликт интересов уже достиг точки кипения, и остается только ждать, у кого первого сдадут нервы. " with fade

    hide img3


label prepare_to_nuke:
    show black_screen

    "Рофлил я над Поздняковым, а теперь собираю тревожный рюкзак."

    hide black_screen
    jump take_gasmask


label take_gasmask:
    show gasmask
    show screen take_gasmask_screen

    gg "Старый, но целый противогаз. Где-то в кладовке есть фильтры, надо будет откопать и их."

    jump take_gasmask


label take_gasmask_result:    
    python:
        answer: str
        if GasMask.taken:
            answer = "Тут ядерка намечается. Какая же ядерка без противогаза!"
        else:
            answer = 'Слышал я, что современные боеголовки довольно "чистые"... Фон должен быстро упасть.'

    gg "[answer]"

    hide gasmask
    


label take_knife:
    show knife
    show screen take_knife_screen

    gg "Неплохой охотничий нож"

    jump take_knife


label take_knife_result:
    python:
        answer: str
        if Knife.taken:
            answer = "Нож, думаю, пригодится. Пусть отправляется в рюкзак. Что там у нас еще..."
        else:
            answer = "Не внушает он мне доверия... Вряд ли стоит его брать"
    gg "[answer]"

    hide knife


label take_medkit:
    show medkit
    show screen take_medkit_screen

    gg "Автомобильная аптечка, я туда еще всякого накидал в свое время. Универсальный медкомплект на все случаи жизни!"
    jump take_medkit


label take_medkit_result:
    python:
        answer: str
        if MedKit.taken:
            answer = "Это мы берем!"
        else:
            answer = "Большая она, громоздкая, половину рюкзака займет. Если действовать осторожно, то она и не понадобится"

    gg "[answer]"

    hide medkit


label take_flashlight:
    show flashlight
    show screen take_flashlight_screen

    gg "Довольно мощный фонарь может пригодиться"
    
    jump take_flashlight


label take_flashlight_result:    
    python:
        answer: str
        if Flashlight.taken:
            answer = "Думаю, чтоит его взять, батарею вроде держит."
        else:
            answer = "Не получается даже придумать ему применение..."

    gg "[answer]"

    hide flashlight


label take_signal_pistol:
    python:
        if Inventory.empty_inventory_slots < 1:
            renpy.jump("first_alarm")
    show signal_pistol
    show screen take_signal_pistol_screen
    gg "Оу... Несколько лет назад ездил с дядей на рыбалку. Положил я его тогда себе, так он у меня и остался. А дядя вроде и не вспоминал про него. Да и комплект патронов остался."

    jump take_signal_pistol


label take_signal_pistol_result:
    python:
        answer: str
        if SignalPistol.taken:
            answer = "Вот это вещь! И посигналить, если потеряюсь, и обороняться им можно."
        else:
            answer = "Для самообороны как-то несерьезно. А сигналить в условиях постапокалипсиса себе дороже. Не думаю, что я буду добрым людям интересен."

    gg "[answer]"

    hide signal_pistol


label first_alarm:
    show black_screen
    stop music
    play music "nuke_alarm.mp3" volume 0.7
    pause 3.0
    show shocked_man
    gg "Я проснулся по воздушной тревоге. Меня обуял ужас, но мне удалось взять себя в руки, и, собрав все нужное, спешно побежал по лестнице вниз."
    gg "В подъезде кипела суета. Люди не могли поверить: случилось невероятное."
    gg "Добравшись до первого этажа, я отдышался и залетел в подвал."
    stop music
    show people_underfloor
    play music "nuke_alarm.mp3" volume 0.15
    gg "Время тянулось медленно..."
    gg "Сидя здесь, я повсюду ловлю испуганные взгляды людей "