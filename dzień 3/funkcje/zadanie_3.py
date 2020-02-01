statuses = {
    "Alice": "online",
    "Rafał": "offline",
    "Anna" : "onine"
}

#Napisz funkcje ktora przyjmie jako argument slownik ze statusami oraz staus (napis). I zwroci liczbe uzytkownikow o zadanym statusie.


def status_count (statuses, status):
    for osoba, stat in statuses.items():
        if stat == status:
            counter +=1
    return counter
  #  return list(statuses.values()).count(status)



def test_status_count_with_existing_status():
    statuses = {
        "Alice": "online",
        "Rafał": "offline",
        "Anna": "onine"
    }
    assert stat_count(statuses, "online") == 2
    assert stat_count(statuses, "offline") == 1

def test_status_none():
    statuses = {
        "Alice": "online",
        "Rafał": "offline",
        "Anna" : "onine"
    }
    assert stat_count(statuses, "") == "Nie podano"