import zipfile
import requests
from io import BytesIO
import os


os.makedirs('./enem2020', exist_ok=True)

import time
url = 'https://download.inep.gov.br/microdados/microdados_enem_2020.zip'

t0 = time.time()
filebytes = BytesIO(
    requests.get(url, verify=False).content
)

myzip = zipfile.ZipFile(filebytes)
myzip.extractall("./enem2020")

tf = time.time()

print('Download completed in: %0.3f s' % (tf-t0))
