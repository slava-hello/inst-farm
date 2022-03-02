import string
import random

from mimesis import Person
from mimesis.locales import Locale


def get_password():
    output = ''
    choice = string.ascii_letters
    choice += string.digits
    # sps = "!#$%&()*+,-./:;=>?@[\]^_`{|}~"
    for i in range(random.randint(14, 19)):
        output += choice[random.randint(0, len(choice) - 1)]
    return output


def get_full_name():
    ru = Person(locale=Locale.RU)
    return ru.first_name()

def get_nickname():
    addon = "_.1234__..567890" + string.ascii_letters
    out = string.ascii_letters[random.randint(0,len(string.ascii_letters) - 1)]
    for i in range(random.randint(7,9)):
        out += addon[random.randint(0,len(addon) - 1)]
    return out
def get_mailname():
    output = ''
    choice = string.ascii_letters
    choice += string.digits
    for i in range(random.randint(14, 19)):
        output += choice[random.randint(0, len(choice) - 1)]
    return output
def answer_for_rambler():
    output = ''
    choice = string.ascii_letters
    for i in range(random.randint(6, 9)):
        output += choice[random.randint(0, len(choice) - 1)]
    return output
