import rocket as space_module
from random import randint

rocket_names = [['01', 'john'], ['02','op'], ['03','black'], ['04','jack'], ['05','smith']]

rockets = [space_module.Rocket(el[0],el[1]) for el in rocket_names]
for x in range(len(rockets)):
    horiz = randint(-50, 50)
    vert = randint(1,100)
    rockets[x].moving(horiz, vert)
    print(rockets[x].name)


shuttles = [space_module.Shuttle(el[0], el[1], 0,0, randint(0,10)) for el in rocket_names]
for sh in shuttles:
    x = randint(-50,50)
    y = randint(0,100)
    sh.moving(x,y)
    print(sh.flights)
    print(sh.x)
