import os, shutil, logging, getpass
from time import sleep


logging.basicConfig(filename='logs.log',format='%(asctime)s %(message)s')
logging.info('installer started, logging set up')

str_header = """
                        ````````````````````````````````````````````````````````````````````````````````````````````````````
                          ````````````````````````````````````..---------..````````````````````````````````````````````````
                            ```````````````````````````````.---::::---::://:--..``````.-````````````````````````````````````
                            ```````````````````````````.-:::------------::::::--......-``````````````````````````````````` 
                              ```````````````````.....-:::----------.-----::://::--::--.`````````````````````````````````` 
                              `````````````````.----::::-----............---::///::://///-.``````````````````````````````  
                                `````````````.-----::::---................----::::/::::/+o/.`````````````````````````````  
                                ````````````.----::::---..................-----::::::::://+/.``````````````````````````````
                                  ``````````./-.-:/::---.....................----::::::::-:/s/.```````````````````````````  
                                ```````````::---------........``````..........----::::::-::+o-`````````````````````````````
                                  `````````.:--------..........`````...........-------:::::::+/-````````````````````````````
                                  ````````.--------..........```````...............----::::::/o/.```````````````````````````
                                ` ```````----------...........````................---::::::::+o-```````````````````````````
                        `       `````````:---------..............`...............----:::/:::://-.``````````````````````````
                                `````````----:------.-........................-------::///::::/:.``````````````````````````
                                ``````````-----------...........................------:://///::::.``````````````````````````
                              ```````````---------..........................--------::::://////+-.`````````````````````````
                                `````````----------------::---......--://++/:------:://///::://+-.`````````````````````````
                                ``````````------------:/oyhhys+:-...-:oyhhhyo/::::::://///:::::/+:..````````````````````````
                                `````````-:---:::://+syhhsssss/-..-:/oso++//shhs+oyyo++//:::--:o/-..```````````````````````
                                  ``````--//---:/oyso/yys+:::::/:--:/++:------://://++/::::::--://+o..``````````````````````
                                ```````+/::---://::---------://:--:++/:-----------------------:/+hy...`````````````````````
                                ````````.+::-----------------/+/:--:/+//:--...-------.---------+++/:..`..```````````````````
                                ````````-::.---.........---://:---:+oo/::---..........-----:::s+::....`````````````````````
                                ``````````--.---........----:/:--.--/o+//---.--.......----::::::::-.....````````````````````
                                ``````````.-------..--..----:+/:---:oso//:-....--...-----:::::::::-......```````````````````
                            ` ```````````.-:---------.....-+hmy/+/smNmho/-......-------:::::::::::......```````````````````
                            `````````````-::-------.......-/ysoohhs+++o+:--.......----:::::::::-::....`````````````````````
                            `````````````.---------......--:///:::--:///::---.....----:::::://::-....``````````````````````
                            ``````````````-:-------...---::////::---:+soo++/::---.---:::::::-::-....```````````````````````
                          ````````````````..----:::-://+++oo+/:::---:/osssyysso+/::::::::::-.........``````..``````````````
                          ` `````````````````.---:+soyssosooooooo+//+oosyyyyyyyyyysss+//::::-..........`...`.....```````````
                          ```````````````````..--://///+oyo+o+////////////+++o++oooso//:://:............`..........`````````
                          ``````````````````..--::-------------:////::------------:://:///-.........................```````
                          ```````````````````..-:-::--..---------------------------://:://:...........................``````
                          ```````````````````...-::::--------..............-------:://////-............................`.```
                          ``````````````````....-:::::-----.................-----::/++ooo++:-..............................`
                          ````````````````....:sm+//:::------...........-----::/+ossyys+sNd+-............................``
                          `````````````````.../dNMy//+o+:::----.......-----::/+oydddhs+++hMMms--............................
                          `````````````````..:hNMMy/::/ooo+/::::------::://+shdmmhso////+sMNNmo-............................
                          ```````````````..-smNMN+/:---:/+oosyhhyyyyyhhhhdddhyoo/::-:::/+NNNmd/-.........................``
                          ```````````````../hmmNN+/:--..--::/+ooooosssoo+++//::-------:/ommmNms:-.......................```
                            ````````````.-:shmNNNh/:--.....-----:-----------:-.....--::+hhyhdmhss+-..................`.````
                            ````````````-+oohddmmmNs/:--............................-::/syyyhdmdshdy+:................``````
                          ``````````.-/sysshhhmmmNmo/:---.........................---:oysyhhhmdhyddhy+-..............``````
                        `````````..:+oyyysyhhhddddmdo:-----.....````````````.......--+yyyhhhhmdhyhdddyo:...............````
                        ```..---::/+sysyyssyyyhhhdddmmo:--...........``.............-/syhhhhhhmmdyddddhhy+:--..............`
                        ++osssssoosyyyysysyhhhhyyddhddds:-.........-:-.............-/syhhddhhhdmmdddddhhhhsyyoo+/::-........
                        mNNNNmdsosyyyyysysyyhhyhhhhhdhddh/-......-+yhys/...``.`...:+syyyyhhyhhdmmdmddhddhhhdNNNNNmmdhso+:-..
                        mdddhssssyyyyysssyysddyymmhhhhhhdy:-...-:ydddddds-.......:osyhyyyyyysydmmmmdddddhddhdmmmdmNNNNMNNmhs
                        hhyysssyyyyyysssyhhyhhyhmdyyyyyyhhs/---:dNNmdhhdNy-....-/sysyysyhyyyyhhmmmmdddhddhhhhhdmdhdhddmmNNMM
                        hyyyyyyyyysssyyyhdmmmNNNNNdssyyyhhdho:-sdhhNdyyhNMs-.-:+yyyyhysyyyyyyyyhmmmmddhhhhhhhdddNmdhhhhhdhhm
                        ssyyhhhyyhhhdmNNNNNNNNNNNNdooyhhhhhhdhyhsoohmydhmNMs-/syyyhyyosydmmmdmdmdddhyhyyyhhdhhhhdmmhhyhhhhhh
                        mmmNNNNNmmmmmmmddddmmddddmyoossyhyhhdmNMNNNmhhhhdNMNsyyssyssssoymMMMMMMMMMmmdhyhhdhhhhhdhhdddhhhyhhy
                        dddmmmmmdmddddddhdddmddmmdsososyyyhhhdmNMMNNyhyshmNmhyyyyhyssysysymNmmdddmNNMMMNNNNmmddddhyhdddhhhhh
                        hhdddddmdddddddhdddmmmddmysosooyyhhyhhddmMMmhyyyhddhysssssooosssyydmmdhyyyhhhdddmNNNMMMNNmdddmmhhhhh
                        hhhddddddddddddddddmmmmmhyosssssyyhyyhhhdmMmhyhhhhyyyyyyyysyyhdmmNNNmmdhyhhhhhyyyyhhddNNNNNNNNdhhhhd
                        hddddddddddddhhhhhmmmmmdssssssyysyyyhyhhyhmNdhhhyyhhhhhhdmmNNMMMNNNmdhddyhhddhhhhyhyyydmmdmmmdhyyhhh
                        dmmdhdddhdddddddddmmmmhyyyyyyyyysssyyyyyyhhNNdhyhhhhdmNNMMMMNNNNmmmhs:osoo/oyyysshhhhhhhhhddddhhhhhd
                        ddddhdddddhddddmddmmmmhyhyyhyyyysyyyyyyyhhhmNhyhhdmNNNNMNNNmddhhhhhhssyhhs+oo++:/mNmdds///sdssoooosy
                        ddhdhdhhhhhhhhdddhdmNNmmdhhhhhhysyyyhyyhdhdmdhhmNNNNNNmNNmmdhyyyyyyyhsohmy+oydsosdddhhs:::+hsooososh
                        hhhhhhhdddhhhhhdddmmNNNNNNNNmdhhhyyyhhhhdddhdmNmdmmmNmNNNhyhyyyyyyhhhhymmhosyho+hdddhhhhhhhhhhhhdhhh
                        dhhddddddddddddddddmmNNmNNNNNNNmdhyhhhddmmhmNNdhdmNNmmNmdsysysysyyhyyyyhhhddddhhddddhhhdddhyhhddhdhh
                        ddddhhyhhyhhdyhhyhhhhdddhmNmmNNNNNmmdddmmdmNdhymmNNmhmNdmyysyhddhhhdddhhhhddddhyhyyhyhhdhhhhyhdhhhhh
                        hdhdddddddmmmmmmmmmmmdmmmNNmmmmmmmmmmmmmddmmhydNNNNmmNmmNdddmdmmmdddddddhhhdNmmmmmmmdmmdddddhddhdddd                                                     

        _______   __         ______   __    __  _______   ______  ________        __    __   ______    ______   __    __  __        ________  _______  
        /       \ /  |       /      \ /  \  /  |/       \ /      |/        |      /  |  /  | /      \  /      \ /  |  /  |/  |      /        |/       \ 
        $$$$$$$  |$$ |      /$$$$$$  |$$  \ $$ |$$$$$$$  |$$$$$$/ $$$$$$$$/       $$ |  $$ |/$$$$$$  |/$$$$$$  |$$ | /$$/ $$ |      $$$$$$$$/ $$$$$$$  |
        $$ |__$$ |$$ |      $$$  \$$ |$$$  \$$ |$$ |  $$ |  $$ |  $$ |__          $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/  $$ |      $$ |__    $$ |__$$ |
        $$    $$< $$ |      $$$$  $$ |$$$$  $$ |$$ |  $$ |  $$ |  $$    |         $$    $$ |$$    $$ |$$ |      $$  $$<   $$ |      $$    |   $$    $$< 
        $$$$$$$  |$$ |      $$ $$ $$ |$$ $$ $$ |$$ |  $$ |  $$ |  $$$$$/          $$$$$$$$ |$$$$$$$$ |$$ |   __ $$$$$  \  $$ |      $$$$$/    $$$$$$$  |
        $$ |__$$ |$$ |_____ $$ \$$$$ |$$ |$$$$ |$$ |__$$ | _$$ |_ $$ |_____       $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |$$  \ $$ |_____ $$ |_____ $$ |  $$ |
        $$    $$/ $$       |$$   $$$/ $$ | $$$ |$$    $$/ / $$   |$$       |      $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  |$$       |$$       |$$ |  $$ |
        $$$$$$$/  $$$$$$$$/  $$$$$$/  $$/   $$/ $$$$$$$/  $$$$$$/ $$$$$$$$/       $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ $$$$$$$$/ $$$$$$$$/ $$/   $$/                     
"""
print(str_header)
logging.info("printing str_header")
sleep(2)
print("creating logging path")
logging.info("creating logging path")
sleep(1)
# DirectorY
user = getpass.getuser()
print("getting user: %s" % (user))
logging.info("getting user: %s" % (user))
logging.info("creating directory variable")
sleep(1)
# Parent Directory path
directory = "\\frumentarii"
print(directory)
print(user)
parent_dir = "C:\\Users\\%s" % user
print(parent_dir)
print("creating Parent Directory path: ", parent_dir)
logging.info("Parent Directory path") 
sleep(2)
# Path
path = parent_dir, directory
path = ''.join(path)
print("created location: %s" % (path))
logging.info("creating logging path")  
sleep(2)
exists = os.path.exists(path)
print(exists)
if exists==True:
      
  print("Directory already exists, uninstalling")
  logging.info("Directory %s already exists, uninstalling" % (path)) 
  list_dir = os.listdir(path)
  print(list_dir)
  for filename in list_dir:
        
        print(filename)
        file_path = os.path.join(path, filename)
        print(file_path)
        
        try:
          
          if os.path.isfile(file_path) or os.path.islink(file_path):
          
                os.unlink(file_path)
                print("File already exists, uninstalling %s" % (file_path))
                logging.info("File already exists, uninstalling %s" % (file_path))
                  
          elif os.path.isdir(file_path):
                
                shutil.rmtree(file_path)
                print("Directory already exists, uninstalling %s" % (file_path))
                logging.info("File already exists, uninstalling %s" % (file_path))  
                            
        except Exception as e:
          
          print('Failed to delete %s. Reason: %s' % (file_path, e))
          logging.error('Failed to delete %s. Reason: %s' % (file_path, e))
          
  print("continue with install")
  logging.info("continue with install")
  
else: 
  
  print("continue with install")
  logging.info("continue with install")
  # Create the directory
  print(path)
  os.mkdir(path)
  print("Directory '% s' created" % directory)
  sleep(2)

print("installing exacutable")
logging.info("installing exacutable")
sleep(2)

print("closing installer")
logging.info("closing installer")
sleep(2)

print("launching Frumentarri")
sleep(2)

logging.info("launching Frumentarri")
print('program files can be found in: ',path)
sleep(2)


# from Frumentarii.__main__ import main

# if __name__ == '__main__':
#     main()





