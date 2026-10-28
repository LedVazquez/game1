#Script for the entity class

class entity:

    #Startup
    def __init__(self, name, hp, con, str, dex, int, fai, skl, lck, mna, aur, portrait):

        #identificator
        self.name=name

        self.portrait=portrait
        
        #Base stats
        self.hp=hp
        self.con=con
        self.str=str
        self.dex=dex
        self.int=int
        self.fai=fai
        self.skl=skl
        self.lck=lck
        self.mna=mna
        self.aur=aur

        #Temp stats
        self.temp_hp=0
        self.temp_con=0
        self.temp_str=0
        self.temp_dex=0
        self.temp_int=0
        self.temp_fai=0
        self.temp_skl=0
        self.temp_lck=0
        self.temp_mna=0
        self.temp_aur=0

    #Getters & Setters

    #Name
    def get_name(self):
        return self.name

    def set_name(self, name):
        try:
            self.name=name
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg

   #portrait
    def get_portrait(self):
        return self.portrait

    def set_portrait(self, portrait):
        try:
            self.portrait=portrait
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
   

    #Hp
    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        try:
            self.hp=hp
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    
    #con
    def get_con(self):
        return self.con

    def set_con(self, con):
        try:
            self.con=con
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #str
    def get_str(self):
        return self.str

    def set_str(self, str):
        try:
            self.str=str
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #dex
    def get_dex(self):
        return self.dex

    def set_dex(self, dex):
        try:
            self.dex=dex
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #int
    def get_int(self):
        return self.int

    def set_int(self, int):
        try:
            self.int=int
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #fai
    def get_fai(self):
        return self.fai

    def set_fai(self, fai):
        try:
            self.fai=fai
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #lck
    def get_lck(self):
        return self.lck

    def set_lck(self, lck):
        try:
            self.lck=lck
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #skl
    def get_skl(self):
        return self.skl

    def set_skl(self, skl):
        try:
            self.skl=skl
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #mna
    def get_mna(self):
        return self.mna

    def set_mna(self, mna):
        try:
            self.mna=mna
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    
    #aur
    def get_aur(self):
        return self.aur

    def set_aur(self, aur):
        try:
            self.aur=aur
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    

    # -- Temps --
   
    #Hp
    def get_temp_hp(self):
        return self.temp_hp

    def set_temp_hp(self, temp_hp):
        try:
            self.temp_hp=temp_hp
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    
    #con
    def get_temp_con(self):
        return self.temp_con

    def set_temp_con(self, temp_con):
        try:
            self.temp_con=temp_con
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #str
    def get_temp_str(self):
        return self.temp_str

    def set_temp_str(self, temp_str):
        try:
            self.temp_str=temp_str
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #dex
    def get_temp_dex(self):
        return self.temp_dex

    def set_temp_dex(self, temp_dex):
        try:
            self.temp_dex=temp_dex
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #int
    def get_temp_int(self):
        return self.temp_int

    def set_temp_int(self, temp_int):
        try:
            self.temp_int=temp_int
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #fai
    def get_temp_fai(self):
        return self.temp_fai

    def set_temp_fai(self, temp_fai):
        try:
            self.temp_fai=temp_fai
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #lck
    def get_temp_lck(self):
        return self.temp_lck

    def set_temp_lck(self, temp_lck):
        try:
            self.temp_lck=temp_lck
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #skl
    def get_temp_skl(self):
        return self.temp_skl

    def set_temp_skl(self, temp_skl):
        try:
            self.temp_skl=temp_skl
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #mna
    def get_temp_mna(self):
        return self.temp_mna

    def set_temp_mna(self, temp_mna):
        try:
            self.temp_mna=temp_mna
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg
    #aur
    def get_temp_aur(self):
        return self.temp_aur

    def set_temp_aur(self, temp_aur):
        try:
            self.temp_aur=temp_aur
            msg= "OK!"
        except Exception as e:
            msg= e

        finally:
            return msg

