import sys
import os
import shutil
import zipfile

class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(
                filename)

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.filename)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def find_replace(self):
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                    self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)

    def zip_files(self):
        file = zipfile.ZipFile(self.filename, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()
