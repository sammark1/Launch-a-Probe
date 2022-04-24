import math
import random

def testing(username):
    return username

def get_system_stars(system_type):
    match system_type:
        case "Solitary star":
            return 1
        case "Binary system":
            return 2
        case "Trinary system":
            return 3
        case "Star cluster":
            return int(math.floor(random.random()*3)+4)
        case "Stellar nebula":
            return int(math.floor(random.random()*6)+6)

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
    phrases  = int(math.floor(random.random()*2)+2)
    for index, x in enumerate(range(phrases)):
        segments = int(math.floor(random.random()*2)+2)
        phrase=""
        if index == 0 and phrases >= 3:
            phrase = letters[int(random.random()*len(letters))]
        else:
            for jndex, y in enumerate(range(segments)):
                phrase=f"{phrase}{sounds[int(random.random()*len(sounds))]}"
        name=f"{name}{phrase.capitalize()} "
    return name

def gen_system_type():
    system_choices = ["Solitary star", "Binary system","Trinary system", "Star cluster", "Stellar nebula"]
    out = random.choices(system_choices, weights=(64,25,8,2,1))
    return out[0]

def gen_star_designation(system, star_index):
    suffix = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',] 
    return(f"{system.designation}-{suffix[star_index]}")
# FIXME TEMPORARY

def gen_planet_designation(system): 
    return(f"{system.designation}-{math.floor(random.random()*100)}")
# FIXME TEMPORARY
