import Password

siteNames = {'Apple': 1, 'Microsoft': 2}

for x in siteNames:
    siteNames[x] = Password.Password(0, 0)


def viewInfo():
    site_name = input('Please enter the name of the website/account you would '
                      'like to access information for: ')
    if site_name in siteNames.keys():
        username = siteNames[site_name].getUsername()
        password = siteNames[site_name].getPassword()
        print('Here is the information for ' + site_name + '.\nUsername: ' + username +
              '\nPassword: ' + password + '\n\n')
        choice = int(input('Would you like to:\n1. Edit this information\n2. Enter another site name to see information'
                           '\n3. Create a new set of information \n4. Delete a set of information '
                           '\n5. Exit the program\n\n'))
        if choice == 1:
            editInfo(site_name)
        elif choice == 2:
            viewInfo()
        elif choice == 3:
            addInfo()
        elif choice == 4:
            deleteInfo()
        elif choice == 5:
            exit()
    elif site_name not in siteNames.keys():
        choice = int(input('The site name ' + site_name +
                           ' is not in the database. Would you like to:\n1. Enter another site name to see information'
                           '\n2. Create a new set of information\n3. Exit the program\n\n'))
        if choice == 1:
            viewInfo()
        elif choice == 2:
            addInfo()
        elif choice == 3:
            exit()


def editInfo(site_name):
    site = site_name
    new_username = input('Please enter a new username for this site: ')
    new_password = input('Please enter a new password for this site: ')
    siteNames[site].setUsername(new_username)
    siteNames[site].setPassword(new_password)
    print('\nThe username and password have been updated for ' + site + '.\n\n')

    choice = int(input('Would you like to:\n1. Edit this information again'
                       '\n2. Enter another site name to see information\n'
                       '3. Create a new set of information \n4. Exit the program\n\n'))
    if choice == 1:
        editInfo(site)
    elif choice == 2:
        viewInfo()
    elif choice == 3:
        addInfo()
    elif choice == 4:
        exit()


def addInfo():
    site_name = input('Please enter the name of the website/account you would like '
                      'to save information for: \n')
    if site_name not in siteNames.keys():
        unique_id = int(len(siteNames) + 1)
        siteNames[site_name] = unique_id
        siteNames[site_name] = Password.Password(0, 0)
        new_username = input('Please enter a username for this site: ')
        new_password = input('Please enter a password for this site: ')
        siteNames[site_name].setUsername(new_username)
        siteNames[site_name].setPassword(new_password)
        choice = int(input('\nThe information has been set for ' + site_name +
                           '. Would you like to:\n1. Enter a new site name for a new set of information'
                           '\n2. View/edit the information for another site\n'
                           '3. Delete the information for this site\n4. Exit the program\n\n'))
        if choice == 1:
            addInfo()
        elif choice == 2:
            viewInfo()
        elif choice == 3:
            deleteInfo()
        elif choice == 4:
            exit()
    elif site_name in siteNames.keys():
        choice = int(input("This site's information is already saved in the database. "
                           "Would you like to:\n1. Enter a new name for a new set of information\n"
                           "2.View/edit the existing information for this site\n"
                           "3. Delete the existing information for this site\n4. Exit the program\n\n"))
        if choice == 1:
            addInfo()
        elif choice == 2:
            viewInfo()
        elif choice == 3:
            deleteInfo()
        elif choice == 4:
            exit()


def deleteInfo():
    site_name = input('Please enter the name of the website/account you would like to '
                      'delete information for: ')
    if site_name in siteNames.keys():
        siteNames.pop(site_name)
        choice = int(input("\nThe data for the site you entered has been deleted. "
                           "Would you like to:\n1. Enter information for a new site\n"
                           "2. View/edit information for another site\n"
                           "3. Delete the existing information for another site\n4. Exit the program\n\n"))
        if choice == 1:
            addInfo()
        elif choice == 2:
            viewInfo()
        elif choice == 3:
            deleteInfo()
        elif choice == 4:
            exit()
    elif site_name not in siteNames.keys():
        choice = int(input("The site that you entered does not match any site in the database. "
                           "Would you like to:\n1. Enter information for a new site\n"
                           "2. View/edit information for another site\n"
                           "3. Delete the existing information for another site\n4. Exit the program\n\n"))
        if choice == 1:
            addInfo()
        elif choice == 2:
            viewInfo()
        elif choice == 3:
            deleteInfo()
        elif choice == 4:
            exit()


choices = int(input('Hello. What would you like to do?\n1. View existing information\n'
                    '2. Add new information\n3. Delete existing information\n4. Exit the program\n\n'))
if choices == 1:
    viewInfo()
elif choices == 2:
    addInfo()
elif choices == 3:
    deleteInfo()
elif choices == 4:
    exit()
