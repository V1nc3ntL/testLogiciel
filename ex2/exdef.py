DB_NAME = "ex2TDD.db"
TABLE_NAME = "users"
COLUMN_NAMES = ("username","password","spublickey","sprivatekey","epublickey","eprivatekey")
KEY_NAMES = COLUMN_NAMES[2:]
KEY_SIZE = 128
USERNAME_COL_NAME = COLUMN_NAMES[0]
PASSWORD_COL_NAME = COLUMN_NAMES[1]
S_PUB_KEY_COL_NAME = COLUMN_NAMES[2]
S_PRI_KEY_COL_NAME = COLUMN_NAMES[3]
E_PUB_KEY_COL_NAME = COLUMN_NAMES[4]
E_PRI_KEY_COL_NAME = COLUMN_NAMES[5]

S_PUB_KEY = "spub".rjust(KEY_SIZE)[:KEY_SIZE]
S_PRI_KEY = "spri".rjust(KEY_SIZE)[:KEY_SIZE]
E_PUB_KEY = "epub".rjust(KEY_SIZE)[:KEY_SIZE]
E_PRI_KEY = "epri".rjust(KEY_SIZE)[:KEY_SIZE]
#le username devra être un nom unique 
WORKING_USER_1 = ("Isma","B1?bbbbb")
FAULT_USERNAME_UNIQUE = ("Isma","B1#bbbbb")
# de plus de 3 chars,
FAULT_USERNAME_LENGTH = ("Ism","B1?bbbbb")
MIN_USERNAME_LENGTH = 3
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