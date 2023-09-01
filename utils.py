def find_index(_list, _urun_ismi):
    try:
        result = [i for i, item in enumerate(_list) if item["urun"] == _urun_ismi]
        return result[0]
    except IndexError:
        print("lutfen urun adini kontrol ederek tekrar giriniz!")
        return -1

