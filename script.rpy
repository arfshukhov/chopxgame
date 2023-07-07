# Вы можете расположить сценарий своей игры в этом файле.
python:

    class InventoryItem:
        pass
    

    class GasMask(InventoryItem):
        name = "gasmask"

        def __repr__(self):
            return self.name

    class Inventory:
         
        
        
        
# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define p = Character("Поздняков", color="#cf8cc8")
define gg = Character("Вы", color="#148800")
#define current_label = None
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


image clock_5 = "images/211109_original.jpg"
image black_screen = "#000"
image natovsbrics = im.Scale("images/NATOvsBRICS.png", 1920, 1080)


# Игра начинается здесь:

init:
    $ current_label = None


label start:

    
    $ current_label = "start"       
    
    show black_screen

    play sound "audio/Поздняков_о_ЗАЭС.ogg"

    "Вступление..."

    stop sound

    scene clock_5:
        xsize 1920
        ysize 1080

    
    gg "Да... Вшивый о бане, а Поздняк как обычно о ядерке."
    gg "Уже светает, пора бы уже лечь спать"

    #hide clock_5 with fade

label conflict_preambule:

    $ current_label = "conflict_preambule" 

    show black_screen

    "Проходит 2 месяца..." with fade

    hide black_screen 

    show natovsbrics 

    "Обстановка в мире напряженная. Нередко случаются стычки между НАТО и военной коалицией стран БРИКС." with fade

    "Столкновения происходят на нейтральных территориях третьих стран, но ни одна из сторон не признает своего участия в боевых действиях." with fade

    "Стороны все еще хотят спустить конфликт на тормозах, но даже людям, не особо смыслящим о политике, давно понятно, 
    что конфликт интересов уже достиг точки кипения, и остается только ждать, у кого первого сдадут нервы. " with fade

    hide natovsbrics with fade

label prepare_to_nuke:

    $ current_label = "label prepare_to_nuke"

    "Рофлил я над Поздняковым, а теперь собираю тревожный рюкзак."

label take_gasmask:
    menu