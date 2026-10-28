#Main script

def Main_menu(player, level):
    main_menu_str="\n" \
    "0.- Salir"\
    "1.- Acciones"\
    "2.- Ver Entorno"
    
    while True:
        try:
            opc=int(input(main_menu_str))
            match opc:
                case 0: break
                case 1: print(player.show_actions())
                case 2: print(level.show_enviroment())

        except Exception as e:
            print(e)




# -- Begins main --
if __name__=='__main__':
    print("a")