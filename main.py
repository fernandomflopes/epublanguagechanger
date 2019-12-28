import zipfile
import os
import hashlib
import sys
from lxml import etree as ET


class EpubZip(object):
    def __init__(self, filename:str):
        self.filename, self.tempdir = filename, str(hash(filename))
        if int(self.tempdir) < 0: # negative paths?
            self.tempdir = str(int(self.tempdir) * -1)

    def compress(self):
        os.chdir(self.tempdir)
        try:
            filename = self.filename.split('.')[0]
            mzip = zipfile.ZipFile('../' + filename + "_" + self.tempdir + '.epub', 'w')
            for path, _, filename in os.walk('.'):
                for f in filename:
                    mzip.write(os.path.join(path, f))
            mzip.close()
        except:
            pass
        os.chdir("../")  
          
    def decompress(self):
        os.mkdir(self.tempdir)
        with zipfile.ZipFile(self.filename, 'r') as zr:
            zr.extractall(self.tempdir)

class EpubLanguageChanger(object):
    def __init__(self, epubname:str, lang:str):
        self.epubname = epubname
        self.lang = lang
        self.epubfile = EpubZip(self.epubname)

    def change(self):
        def whereisthecontent(content = 'content.opf'):
            for path, _, filename in os.walk(self.epubfile.tempdir):
                if content in filename:
                    return os.path.join(path, content)
        
        def changeLanguage(contentpath):
            tree = ET.parse(contentpath)
            r = tree.getroot()
            ns = {'dc':'http://www.idpf.org/2007/opf'}
            sub = r.find('dc:metadata', ns)
            nsl = {'dc':'http://purl.org/dc/elements/1.1/'}
            lang = sub.find('dc:language', nsl)
            lang.text = self.lang
            
            tree.write(open(contentpath, "wb"))
            
        self.epubfile.decompress()
        contentpath = whereisthecontent()
        changeLanguage(contentpath)
        self.epubfile.compress()

try:
    file, lang = sys.argv[1], sys.argv[2]
    if os.path.exists(file):
        c = EpubLanguageChanger(file, lang)
        c.change()
    else:
        print(file + " file not exists")
except:
    print("argument error")