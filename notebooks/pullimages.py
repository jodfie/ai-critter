import uuid
import requests
import csv
import shutil
from os.path import exists

output = 'data/'


def save_image(URL, PATH):
    r = requests.get(URL, stream=True)
    if r.status_code == 200:
        with open(PATH, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)       

with open("inital_training_data.csv", "w") as f2:
    f2.write("fname,labels\n")
    f2.flush()
    with open("birb.csv", "r", encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            path = output +f"{str(uuid.uuid5(uuid.NAMESPACE_DNS, line[0]))}.jpg"
            label = line[1]

            if exists(path):
                print(f"[{str(i)}][-] I already have this image - {path}")
                continue
            else:
                print(f"[{str(i)}][+] Saving Image of a {label} to {path}")
                save_image(line[0].strip(), path)
            f2.write(f"{path}, {label}\n")
            f2.flush()