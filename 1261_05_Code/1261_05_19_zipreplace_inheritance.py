from zip_processor import ZipProcessor
import sys
import os

class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string,
            replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        '''perform a search and replace on all files in the
        temporary directory'''
        for filename in os.listdir(self.temp_directory):
            with open(
                self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(
                    self.search_string, self.replace_string)
            with open(self._full_filename(filename), "w") as file:
                file.write(contents)

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()
