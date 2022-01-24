def DicttoHTML_Films(dictionary):
    data = '<table class="film-table">'
    for row in dictionary:
        id = row['film_id']
        title = row['title']
        description = row['description']
        rij = f"<tr><td>{id}</td><td>{title}</td><td>{description}</td></tr>"
        data += rij

    data += "<table>"
    return data
