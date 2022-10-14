frutas = ("manzana", "sandia", "naranja")

vegetales = ("lechuga", "rucula", "cebolla")

productos_animales = ("cucha", "correa", "bozal")

food_stuff_tp = frutas + vegetales + productos_animales
food_stuff_it = list(food_stuff_tp)
#print(food_stuff_it)

mid = food_stuff_it[3:5]
print(food_stuff_it)

inicio = food_stuff_it[:3]
fin = food_stuff_it[6:]
print(inicio)
print(fin)

del food_stuff_tp


#-------------------------------------


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

