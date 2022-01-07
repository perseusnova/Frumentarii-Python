import os, shutil, logging, getpass


#logging file for installer

f = os.fspath("log.logs")
logger = logging.getLogger("")
logger.setLevel(logging.INFO)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()
fileHandler = logging.FileHandler(f)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
logger.info('installer started, logging set up')

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
logger.info("printing str_header")

logger.info("creating logging path")

# DirectorY
user = getpass.getuser()
logger.info("getting user: %s" % (user))
logger.info("creating directory variable")

# Parent Directory path
directory = "\\frumentarii"
parent_dir = "C:\\Users\\%s" % user
logger.info("Parent Directory path %s" % (parent_dir))

# Path
path = parent_dir, directory
path = ''.join(path)

logger.info("creating logging path")  

exists = os.path.exists(path)

if exists==True:
      
  logger.info("Directory %s already exists, uninstalling" % (path)) 
  list_dir = os.listdir(path)
  
  for filename in list_dir:
        
        file_path = os.path.join(path, filename)

        try:
          
          if os.path.isfile(file_path) or os.path.islink(file_path):
          
                os.unlink(file_path)
                logger.info("File already exists, uninstalling %s" % (file_path))
                  
          elif os.path.isdir(file_path):
                
                shutil.rmtree(file_path)
                logger.info("File already exists, uninstalling %s" % (file_path))  
                            
        except Exception as e:
          
          logging.error('Failed to delete %s. Reason: %s' % (file_path, e))
          
  logger.info("continue with install")
  
else: 
  
  logger.info("continue with install")
  # Create the directory
  os.mkdir(path)

  
logger.info("creating logging file and appending installer logs")

#file for logging application
logging_file = path, "\\frumentarri.logs"
logging_file = ''.join(logging_file) 
lf = open(logging_file, "a")
lf.write("##############Frumentari logs##############")
#open and read the file after the appending:

logger.info("installing exacutable")


logger.info("closing installer")



logger.info("launching Frumentarri")
logger.info('program files can be found in: %s' % (path))

d = open(f, 'r')
for i in d.read():
      lf.write(i)

lf.close()

# from Frumentarii.__main__ import main

# if __name__ == '__main__':
#     main()





