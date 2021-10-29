import sys
import re

# The filter funciton is responsible for removing URLs from a file that contain certain words that are undesirable.
def filter(filename):
    words = ["signup", "signin", "cookies", "contact-us", "login", "covid", "term", "faq",
            "sign-in", "account", "settings", "contact", "privacy-policy", "blog", "cookie-policy",
            "terms-and-conditions", "terms-of-use", "sign-up", "signout", "sign-out", "user", "logout", "password",
            "forgot", "help", "search"]
    f = open(filename, "r")
    content = f.readlines()
    new_file = []

    for word in words:
        for i in range(len(content)):
            if content[i] != "\n" and content[i] != '#':
                if (re.search(".*" + re.escape(word) + ".*\n", content[i], re.IGNORECASE)):
                    content[i] = ""


    new_content = top_5(content)
    n = open("FILTERED_" + filename, "a")
    for line in new_content:
        if (line != ""):
            n.write(line)

    n.close()
    f.close()

# Returns the top 5 entries for each domain group.
def top_5(content):
    count = 0
    new_content = []

    for line in content:
        if (line != ''):
            if (line[0] == '#'):
                count = 0
                new_content.append(line)
            else:
                if (count <= 5):
                    new_content.append(line)
            count += 1

    return new_content

# Main function.
if __name__ == '__main__':
    filter(sys.argv[1])
