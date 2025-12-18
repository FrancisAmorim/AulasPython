import pprint

filmDict = {
    "inception": {
        "yearRelease": 2010,
        "imdbRating" : 8.8,
        "genre" : ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar": {
        "yearRelease": 2014,
        "imdbRating" : 10.0,
        "genre" : ["Sci-fi", "Drama"]
    },
    "the dark knight": {
        "yearRelease": 2008,
        "imdbRating" : 9.0,
        "genre" : ["Action", "Drama"]
    }
}

PP = pprint.PrettyPrinter(depth=4)

PP.pprint(filmDict)