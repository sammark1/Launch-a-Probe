from random import random
import math

def testing(username):
    return username

def gen_system_designation(username,systems):
    # currently no redundancy filter
    return f"{(username[0:2]).upper()}-{str(len(systems)+1).rjust(5,'0')}"

# def gen_system_name():
#     name=""
#     vsounds = ["a","e","i","o","u","ae","ai","ao","au","ea","ee","ei","eo","eu","ia","ie","io","iu","oa","oe","oi","oo","ou","ua","ue","ui","aou","oui"]
#     consounds = ["b","c","d","f","g","h","j","k","l","m","n","p","qu","r","s","t","v","w","x","y","z"]
#     segments = int(math.floor(random()*4)+2)
#     for index, x in enumerate(range(segments)):
#         if (index%2) == 0:
#             name=f"{name}{vsounds[int(random()*len(vsounds))]}"
#         else:
#             name=f"{name}{consounds[int(random()*len(consounds))]}"
#     return name

def gen_system_name():
    name=""
    sounds = ["ab","al","an","ta","ir","ri","gel","be","tel","ge","po","lar","is","wo","olf","eri","da","ni","us","si","sa","gi","ta","ri","us","dro","mi","dae","ce","ti","le","on","is","la","ce","ra","tae"]
    letters = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa", "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega", "aleph", "bet", "giml", "dalet", "hē", "wāw", "zajin", "hēt", "tēt", "yod", "kāp", "iāmed", "mēm", "nūn", "śāmek", "ayin", "pē", "ṩādē", "qōp", "rēs", "šīn", "tāw"]
    phrases  = int(math.floor(random()*2)+2)
    # phrases  = 4
    for index, x in enumerate(range(phrases)):
        segments = int(math.floor(random()*2)+2)
        phrase=""
        if index == 0 and phrases >= 3:
            phrase = letters[int(random()*len(letters))]
        else:
            for jndex, y in enumerate(range(segments)):
                phrase=f"{phrase}{sounds[int(random()*len(sounds))]}"
        name=f"{name}{phrase.capitalize()} "
    return name