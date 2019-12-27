from pages.homepage import HomePage
from main import PATH

def search(criteria):
    google = HomePage()
    results = google.search(criteria)
    file_export = open(f'{PATH}\\{criteria}.txt','w')

    for i in results:
        file_export.write("{}\r".format(i))

    file_export.close()
    google.quit()