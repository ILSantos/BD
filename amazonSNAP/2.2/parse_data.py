import re

class snapobject:
    def __init__(self):
        self.id = None
        self.asin = None
        self.title = None
        self.group = None
        self.salesrank = None
        self.similar = []
        self.categories = []
        self.reviews = []

class review:
    def __init__(self):
        self.customerID = None
        self.date = None
        self.rating = None
        self.votes = None
        self.helpful = None

class category:
    def __init__(self):
        self.id = None
        self.name = None

def parsefile(filepath):
    list = []

    idMatcher = re.compile('Id: (.*)')

    with open(filepath, 'r') as file:
        nextLine = file.readline()

        while nextLine:
            idMatch = idMatcher.match(nextLine)
            if idMatch:
                objectMatchList = []
                while nextLine is not '\n':
                    objectMatchList.append(nextLine)
                    nextLine = file.readline()

                list.append(parseobject(objectMatchList));

            nextLine = file.readline()

    return list


def parseobject(objectLineList):

    idMatcher = re.compile('Id: (.*)')
    asinMatcher = re.compile('ASIN: (.*)')
    titleMatcher = re.compile(' title: (.*)')
    groupMatcher = re.compile(' group: (.*)')
    rankMatcher = re.compile(' salesrank: ([0-9-]*)')
    categoryCountMatcher = re.compile(' categories: ([0-9]*)\n')
    categoryInfoMatcher = re.compile('   (?:\|([A-Za-z0-9& .]*)\[(\d*)\])(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?' +
                                     '(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?' +
                                     '(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?' +
                                     '(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?(?:\|([A-Za-z0-9& .]*)\[(\d*)\])?')

    reviewMetaMatcher = re.compile('  reviews: total: (\d*)  downloaded: (\d*)  avg rating: ([0-9]\.?[0-9]?)')
    reviewInfoMatcher = re.compile('\s*([0-9\-]*)\s*cutomer:\s*([0-9A-Za-z]*)\s*rating: ([0-9]*)\s*votes:  ([0-9]*)\s*helpful:\s*([0-9]*)')

    currentobject = snapobject()

    currentobject.id = idMatcher.search(objectLineList[0]).group(1).replace(" ", "")
    currentobject.asin = asinMatcher.search(objectLineList[1]).group(1).replace(" ", "")


    # check if object is valid via its title
    titleMatch = titleMatcher.search(objectLineList[2])

    if titleMatch is None:
        return currentobject
    else:
        currentobject.title = titleMatch.group(1)

    currentobject.group = groupMatcher.search(objectLineList[3]).group(1)
    currentobject.salesrank = rankMatcher.search(objectLineList[4]).group(1)

    # check if object has similar ones
    similarMatch = re.findall('[0-9A-Za-z]*', objectLineList[5])
    while similarMatch.__contains__(''):
        similarMatch.remove('')


    if similarMatch[1] is not '0':
        for i in range(2, similarMatch.__len__()):
            currentobject.similar.append(similarMatch[i])

    categoryCount = int(categoryCountMatcher.search(objectLineList[6]).group(1))

    if categoryCount > 0:
        for i in range(7, 7 + categoryCount):
            categorySearch = categoryInfoMatcher.search(objectLineList[i])
            categoryElements = []

            for i in range(1, categorySearch.lastindex + 1):
                categoryElements.append(categorySearch.group(i))

            categoryline = []

            for j in range(0, categoryElements.__len__() - 1, 2):
                if categoryElements[j] is not None and categoryElements[j + 1] is not None:
                    newCat = category();
                    newCat.name = categoryElements[j]
                    newCat.id = categoryElements[j + 1]
                    categoryline.append(newCat)

            currentobject.categories.append(categoryline)

    reviewMetaLine = 7 + categoryCount
    reviewCount = int(reviewMetaMatcher.search(objectLineList[reviewMetaLine]).group(2))

    if reviewCount > 0:
        for i in range(reviewMetaLine + 1, reviewMetaLine + 1 + reviewCount):
            reviewInfo = re.findall('[0-9\-A-Za-z]*', objectLineList[i])
            reviewElements = []

            for element in reviewInfo:
                if element is not '':
                    reviewElements.append(element)

            reviewObj = review()

            reviewObj.date = reviewElements[0]
            reviewObj.customerID = reviewElements[2]
            reviewObj.rating = reviewElements[4]
            reviewObj.helpful = reviewElements[6]
            reviewObj.votes = reviewElements[8]

            currentobject.reviews.append(reviewObj)

    print(currentobject.id)
    print(currentobject.asin)
    print(currentobject.title)
    print(currentobject.group)

    print('\n')


    return currentobject
