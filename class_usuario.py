class Usuario():
    
    def __init__(self, id, username, clase):
        self.id = id
        self.username = username
        self.clase = clase
        
    def __str__(self):
        
        return("Tu nombre de usuario es {}".format(self.username))
        

    