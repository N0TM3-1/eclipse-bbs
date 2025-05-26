import mystic_bbs as bbs # type: ignore

userdata = bbs.getuser(0)

def other_acc():
    bbs.write("Do you have other accounts on this BBS? (y/n): ")
    return bbs.getstr(1,1,1,"")

# Page title
bbs.write("|CL")
bbs.writeln("User application form")
bbs.write("|$D80=")

#Get data 

bbs.writeln("Why did you sign up for this BBS?")
reason = bbs.getstr(11, 60, 60, "")
bbs.writeln("How did you find out about this BBS?")
source = bbs.getstr(11, 60, 60, "")
bbs.writeln("What do you hope to get out of being a member here?")
hope = bbs.getstr(11, 60, 60, "")
bbs.writeln("Have you ever called a BBS before? If so, which one(s)?")
priors = bbs.getstr(11, 60, 60, "")
while True:
    other = other_acc()
    if other != "y" and other != "n" and other != "Y" and other != "N":
        pass
    else:
        break

if other == "y" or other == "Y":
    bbs.writeln("Why did you create this account?")
    other_reason = bbs.getstr(11, 60, 60, "")
    bbs.writeln("What is your other account's handle?")
    other_handle = bbs.getstr(11, 60, 60, "")


#Write to main bulletin
#Get existing entries
with open("applications/bulletin.asc", "r") as file:
    existing_entries = file.readlines()

#Check if the user already exists
new_line = str(userdata["handle"]) + ". ID: " + str(userdata["id"])+"\n"
if new_line not in existing_entries:
    with open("applications/bulletin.asc", "a") as file:
        file.write(new_line)

with open("applications/submissions/application"+str(userdata["id"])+".asc","w") as file:
    file.write("|CL \n" \
    "|16User application form:|07\n \n" \
    "Account Details:\n"\
    "Account ID: " + str(userdata["id"]) + "\n" \
    "Account handle: " + str(userdata["handle"]) + "\n \n"\
    "Questionaire answers:\n" \
    "Why did you sign up for this BBS?: " + str(reason) + "\n" \
    "How did you find out about this BBS?: " + str(source) + "\n" \
    "What do you hope to get out of being a member here?: " + str(hope) + "\n" \
    "Have you ever called a BBS before? If so, which one(s)?: " + str(priors) + "\n" \
    "Do you have other accounts on this BBS?: " + str(other) + "\n")
    if other == "y" or other == "Y":
        file.write("Why did you create this account?: " + str(other_reason) + "\n" \
        "What is your other account's handle?: " + str(other_handle) + "\n")

bbs.writeln("")
bbs.writeln("Your request was sent successfully")
bbs.write("|PA")