class Bar:
    menu = {
        "vino": 4,
        "cerveza": 2,
        "agua": 1
    }

#init es metodo que se ejecuta cuando se instancia un objeto
#self es variable de instancia
def __init__(self):
    self.total = 0
    self.objetos = []


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
