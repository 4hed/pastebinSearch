try:
    import json
    import requests
    import sys
except:
    print("""
    Missing Imports !
    """)

def usage():
    print()
    print("Usage: python3 "+sys.argv[0]+" --help")
    print("Usage: python3 "+sys.argv[0]+" <username>")
    print("Usage: python3 "+sys.argv[0]+" <example@gmail.com>")
    print()

def main():
    if len(sys.argv) < 2 or len(sys.argv) >= 3 or "-help" in sys.argv[1] or "--help" in sys.argv[1]:
        usage()
    else:
        if "@" in sys.argv[1]:
            print("Searching For Email: "+sys.argv[1])
            email_search(sys.argv[1])
        else:
            print("Searching For Username: "+sys.argv[1])
            username_search(sys.argv[1])

def email_search(email):
    try:
        get = requests.get("https://psbdmp.ws/api/search/email/"+email)
        data = get.json()
        count = 0
        found_count = data["count"]
        if found_count == 0:
            print("No Results Found")
        else:
            while count < found_count:
                print("Found: https://pastebin.com/"+data["data"][count]["id"]+" Date:"+data["data"][count]["time"]+" Tags: "+data["data"][count]["tags"])
                count = count + 1
        print()
        print("Found: "+str(found_count)+" Results")
    except:
        print("Failed To Connect To psbdmp")

def username_search(username):
    try:
        get = requests.get("https://psbdmp.ws/api/search/"+username)
        data = get.json()
        count = 0
        found_count = data["count"]
        if found_count == 0:
            print("No Results Found")
        else:
            while count < found_count:
                print("Found: https://pastebin.com/"+data["data"][count]["id"]+" Date:"+data["data"][count]["time"]+" Tags: "+data["data"][count]["tags"])
                count = count + 1
        print()
        print("Found: "+str(found_count)+" Results")
    except:
        print("Failed To Connect To psbdmp")

if __name__ == "__main__":
    main()
