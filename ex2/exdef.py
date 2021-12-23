DB_NAME = "ex2TDD.db"
TABLE_NAME = "users"
COLUMN_NAMES = ("username","password","spublickey","sprivatekey","epublickey","eprivatekey")
KEY_SIZE = 128
# Il n'y a a pas d'indication sur les clés, leur caractère ou leur format
# Néanmoins des valeurs seront données pour pouvoir tester
S_PUB_KEY = "0".ljust(KEY_SIZE)[:KEY_SIZE]
S_PRI_KEY = "1".ljust(KEY_SIZE)[:KEY_SIZE]
E_PUB_KEY = "2".ljust(KEY_SIZE)[:KEY_SIZE]
E_PRI_KEY = "3".ljust(KEY_SIZE)[:KEY_SIZE]



#le username devra être un nom unique 
WORKING_USER_1 = ("Isma","B1?bbbbb")
FAULT_USERNAME_UNIQUE = ("Isma","B1#bbbbb")
# de plus de 3 chars,
FAULT_USERNAME_LENGTH = ("Ism","B1?bbbbb")
#les chiffres sont autorisés
WORKING_USER_2 = ("V1nce","A0#aaaaa")
# mais pas les caractères spéciaux
FAULT_USERNAME_SPECIALCHAR = ("user?","B1?bbbbb")
# Le password devra être composé de 8 chars minimum
FAULT_PASSWORD_LENGTH = ("Vinsma","B1?bbbb")
# contenant au moins une majuscule, 
FAULT_PASSWORD_UPPER = ("passwordupper","b1?bbbbb")
# au moins un caractère spécial, 
FAULT_PASSWORD_SPECIAL = ("passwordupper","B1bbbbbb")
# et au moins un chiffre 
FAULT_PASSWORD_DIGIT = ("passwordupper","Bbbb?bbb")
# et au moins 1 caractère standard
FAULT_PASSWORD_STANDARD = ("passwordupper","B?001111")

WORKING_USERS = (WORKING_USER_1,WORKING_USER_2)

FAULT_PASSWORD = (FAULT_PASSWORD_LENGTH,FAULT_PASSWORD_UPPER,FAULT_PASSWORD_SPECIAL,FAULT_PASSWORD_DIGIT, FAULT_PASSWORD_STANDARD)
FAULT_USERNAME = (FAULT_USERNAME_UNIQUE,FAULT_USERNAME_LENGTH,FAULT_USERNAME_SPECIALCHAR)
FAULT_USERS = (FAULT_USERNAME, FAULT_PASSWORD)