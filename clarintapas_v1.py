## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
from datetime import datetime, timedelta


def downloadfrontpage(dtini):
    ## Set up the image URL and filename
    base_url = "https://tapas.clarin.com/tapa"
    image_url = f"{base_url}/{dtini[0:4]}/{dtini[4:6]}/{dtini[6:8]}/{dtini}_thumb.jpg"
    filename = image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Imagen descargada exitosamente: ',filename)
    else:
        print('La imagen no pude ser descargada', filename)

while True:
    try:
        varyear = int(input('Ingrese año entre 1948 y 2021: '))
        assert 1948 < varyear < 2021
    except ValueError:
        print("Por favor ingrese un año valido.")
    except AssertionError:
        print("Por favor elija un año entre 1948 y 2021")
    else:
        break

while True:
    try:
        varmonth = int(input('Ingrese un mes entre 1 y 12: '))
        assert 0 < varmonth < 13
    except ValueError:
        print("Por favor ingrese un mes valido.")
    except AssertionError:
        print("Por favor elija un mes entre 1 y 12")
    else:
        break

while True:
    try:
        varday = int(input('Ingrese dia entre 1 y 31: '))
        assert 0 < varday < 32
    except ValueError:
        print("Por favor ingrese un dia valido.")
    except AssertionError:
        print("Por favor elija un dia entre 1 y 31")
    else:
        break

specific_date = datetime(varyear, varmonth, varday)
print(specific_date)

for i in range(120):
    if i==0:
        new_date = specific_date
    else:
        new_date = new_date + timedelta(1)
    downloadfrontpage(new_date.strftime('%Y%m%d'))

