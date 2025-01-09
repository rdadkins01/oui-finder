import requests
import json
import gzip
import os


def get_oui_data():
    wireshark_oui_url = "https://www.wireshark.org/download/automated/data/"
    oui_file = "manuf.gz"
    r = requests.get(wireshark_oui_url + oui_file, stream=True)
    if r.ok:
        # Write to file
        with open(f"./{oui_file}", "wb") as file:
            for chunk in r.iter_content(chunk_size=1024):
                file.write(chunk)
        
        # Extract file
        with gzip.open(f"./{oui_file}", 'rb') as z:
            with open("./manuf", "wb") as file:
                file.write(z.read())
    else:
        raise Exception(f"Failed to download OUI Lookup file from {wireshark_oui_url}{oui_file}, Error Code {r.status_code}")

    with open("./manuf", "r") as file:
        parsed_file = [x for x in file.read().split("\n") if "#" not in x]
    
    temp_dict = {}
    for line in parsed_file:
        if "\t" in line:
            print(line)
            mac = line.split("\t")[0].strip()
            print(mac)
            if "/" in mac:
                mask = mac.split("/")[1]
                mac = mac.split("/")[0]
            else:
                mask = 24
            short_name = line.split("\t")[1].strip()
            long_name = line.split("\t")[2].strip()
            temp_dict[mac] = {"mask": mask, "short_name": short_name, "long_name": long_name}

    # Write to json file for future use
    with open("oui_manuf.json", "w") as file:
        json.dump(temp_dict, file)
    
    return


def main():

    # Download wireshark OUI database if it doesn't already exist
    if not os.path.exists("./oui_manuf.json"):
        get_oui_data()

    with open("./oui_manuf.json", "r") as file:
        oui_data = json.load(file)

    print(oui_data)


if __name__ == "__main__":
    main()
