"""
2
for number in range(11):
    print(number)

n = 0
while n < 11:
    print(n)
    n += 1
"""

# -------------------------------

"""
3
arr = []
for number in range(0, 11):
    arr.append(number)

arr.reverse()
print(arr)


count = 11
while count >= 0:
    print(count)
    count = count - 1
    if(count == 0):
        continue
"""

        #despues de continue vuelve a empezar
        #loop una vez mas ignorando condicion while


#---------------------------------------------
"""
4
ascx = "ads"
q = "ergf"
xc = ascx + q

print(xc)

numeral = "#"
v = 7
while v > 0:
    print(numeral)
    numeral += "#"
    v = v - 1
"""
#------------------------------------------------

"""
5
for v in range(8):
    print("########")


a = 0
b = 0
while a < 11:
    resultado = a * a
    print(str(a)+" + "+str(a)+" = "+str(resultado))
    a += 1
"""

#----------------------------------------------

"""
#6
librerias =  ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for lib in range(len(librerias)):
    print(librerias[lib])


#7
for numeros in range(101):
    if(numeros % 2 == 0):
        print(numeros)


#8
for numeros in range(101):
    if(numeros % 2 != 0):
        print(numeros)
"""

#-------------------------------------

#Level 2
#1

"""
sum = 0
for numeros in range(101):
    sum += numeros
    if(numeros == 100):
        print("The sum of all numbers is "+str(sum))

#2
par = 0
impar = 0

for numeros in range(101):
    if(numeros % 2 == 0):
        par += numeros
    else:
        impar += numeros
    if(numeros == 100):
        print("The sum of all evens is "+str(par)+". And the sum of all odds is "+str(impar))

"""

#-----------------------------------------------------

#Level 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

"""
for paises in range(len(countries)):
    for letras in countries:
        eliminar = "land" in countries
        if(eliminar):
"""

"""
#Si hacemos esto va a tirar error
#porque al for recorrer la lista despues
#del pop se va a dar cuenta que tiene un
#elemento menos, lo que provoca conflicto

lista = [1, 23, 54, 45]
for num in range(len(lista)):
    e = 0
    print(num)
    if(lista[num] > 40):
        lista.pop(num)
"""

for num in range(len(countries)-1, -1, -1):
    if "land" in countries[num]:
        co = countries.pop(num)
        print(co)