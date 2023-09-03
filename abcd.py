class Teams:
     def __init (self, members): 
        self.__myTeam=members
         def __len__(self): 
            return len(self.__myTeam) 
            def__contains__ (self, member): 
                 
                return member in self.__myTeam 
                def__iter__. (self): 
                    
                    return iter (self.__myTeam) 
                    def main(): 
                        classmates=Teams (['John', 'Steve', 'Tim']) 
                        print('Tim' in classmates) 
                        print ('Sam' in classmates) 
                        iterator=iter(classmates)
                        for member in iterator: 
                            print (member,end=" ") 
                  main ()