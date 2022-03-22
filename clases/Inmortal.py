class Inmortal:  
    def ejecucion():  
        class Yin: pass
        class Yang: 
            def _del_(self): 
                print("Yang destruido") 
        
        yin = Yin() 
        yang = Yang() 
        yin.yang = yang 
        print(yang)
        print(yang is yin.yang)
        Yang._del_(yang) 
        print("?") 
# Habíamos llamado mal a la función _del_(self) y ahora ya sí que se ejecuta correctamente:
# Salida:
# True
# Yang destruido
# ?

