import json
def find_index(_list, _urun_ismi):
    try:
        result = [i for i, item in enumerate(_list) if item["urun"] == _urun_ismi]
        return result[0]
    except IndexError:
        print("lutfen urun adini kontrol ederek tekrar giriniz!")
        return -1


def read_users_file():
    try:
        f = open("user.txt")
        result = json.loads(f.read())
        f.close()
        return result
    except:
        return []

def write_users_file(_users):
    try:
        f = open("user.txt", "w")
        f.write(json.dumps(_users))
        f.close()
        return True
    except:
        return False
