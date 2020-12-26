import re
requiredFields = {
    "byr": True,  # birth year
    "iyr": True,  # issue year
    "eyr": True,  # expiration year
    "hgt": True,  # height
    "hcl": True,  # hair color
    "ecl": True,  # eye color
    "pid": True,  # passport id
    "cid": False  # country id
}

# ogni passaporto è costituito da key:val
# e sono divisi da una linea vuota

# i passaporti sono validi se tutti gli 8 campi sono presenti
# al più può non esistere CID
passports = []


def wrapper_is_valid(field_name, field_value, debug=False):
    if debug:
        print("Validating {} of value {}".format(
            field_name, field_value), end="\t\t")
    valid = is_valid(field_name, field_value)
    if debug:
        print("was valid: {}".format(valid))
    return valid


def is_valid(field_name, field_value):
    if field_name == "byr":
        if re.match("\\d{4}", field_value):
            return 1920 <= int(field_value) <= 2002
        return False
    elif field_name == "iyr":
        if re.match("\\d{4}", field_value):
            return 2010 <= int(field_value) <= 2020
        return False
    elif field_name == "eyr":
        if re.match("\\d{4}", field_value):
            return 2020 <= int(field_value) <= 2030
        return False
    elif field_name == "hgt":
        if "cm" in field_value:
            field_value = field_value.replace("cm", "")
            if re.match("\\d*", field_value):
                return 150 <= int(field_value) <= 193
            return False
        elif "in" in field_value:
            field_value = field_value.replace("in", "")
            if re.match("\\d*", field_value):
                return 59 <= int(field_value) <= 76
            return False
        else:
            return False
    elif field_name == "hcl":
        return re.match("#[0-9a-f]{6}", field_value) is not None
    elif field_name == "ecl":
        return re.match("(amb|blu|brn|gry|grn|hzl|oth)", field_value) is not None
    elif field_name == "pid":
        return re.match("\\d{9}", field_value) is not None
    elif field_name == "cid":
        return True


with open("day4_input.txt", "r") as f:
    lines = f.readlines()
    passport = ""
    for line in lines:
        if not re.match("^$", line):
            passport += line
        else:
            passports.append(passport)
            passport = ""
    passports.append(passport)


valids = 0
debug = True
printNotValid = False
threshold = 5
for passport in passports:
    passport = passport.replace("\n", " ")
    if debug:
        print(passport)
    count = 0
    missings = []
    for key in requiredFields:
        required = requiredFields[key]
        regex = r"{}:([\D|\d]*?)(\\n|$| )".format(key)
        if (required):
            matcher = re.search(regex, passport)
            if matcher is not None:
                value = matcher.group(1)
                if "2033\nhgt:177cm" in value:
                    print(passport)
                if wrapper_is_valid(key, value, debug=debug):
                    count += 1
                else:
                    pass
            else:
                missings.append(key)
    if count >= 7:
        valids += 1
    elif printNotValid and count >= threshold:
        print(passport, missings)

        found = 0
        for missing in missings:
            if missing in passport:
                print("Missing {} but found in string".format(missing), end="\n\n")
                found += 1
        if found == 0:
            print("\n\n")


print("trovati {} passaporti di cui validi {}".format(len(passports), valids))
