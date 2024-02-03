class Password:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def setUsername(self, username):
        self.username = username


    def setPassword(self, password):
        self.username = password


    def getUsername(self):
        read_file = open("test.txt", "r")
        content = read_file.read()
        read_file.close()

        return content
    

    def getPassword(self):
        return str(self.password)
    
    def deleteInfo(self, Password):
        del Password
        