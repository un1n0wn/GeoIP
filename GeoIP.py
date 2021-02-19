import os
import time

print ("\033[36m")                                                                                                                                                                                                           
                                                                                                                                                                                                                             
os.system("clear")                                                                                                                                                                                                           
                                                                                                                                                                                                                             
                                                                                                                                                                                                                             
logo4 = '''                                                                                                                                                                                                                  
 #####                ### ######                                                                                                                                                                                             
#     # ######  ####   #  #     #                                                                                                                                                                                            
'''                                                                                                                                                                                                                          
                                                                                                                                                                                                                             
logo1 = '''                                                                                                                                                                                                                  
 #####                ### ######                                                                                                                                                                                             
#     # ######  ####   #  #     #                                                                                                                                                                                            
#       #      #    #  #  #     #                                                                                                                                                                                            
#  #### #####  #    #  #  ######                                                                                                                                                                                             
'''                                                                                                                                                                                                                          
                                                                                                                                                                                                                             
logo2 = '''                                                                                                                                                                                                                  
 #####                ### ######                                                                                                                                                                                             
#     # ######  ####   #  #     #                                                                                                                                                                                            
#       #      #    #  #  #     #                                                                                                                                                                                            
#  #### #####  #    #  #  ######                                                                                                                                                                                             
#     # #      #    #  #  #                                                                                                                                                                                                  
'''                                                                                                                                                                                                                          
                                                                                                                                                                                                                             
logo = '''                                                                                                                                                                                                                   
 #####                ### ######                                                                                                                                                                                             
#     # ######  ####   #  #     # 
#       #      #    #  #  #     # 
#  #### #####  #    #  #  ######  
#     # #      #    #  #  #       
#     # #      #    #  #  #       
 #####  ######  ####  ### #   
'''

print (logo4)
time.sleep(0.1)
os.system("clear")
print (logo1)
time.sleep(0.1)
os.system("clear")
print (logo2)
time.sleep(0.1)
os.system("clear")
print(logo)
print ("\033[31m")
d3 = input("Target: ")
os.system("curl http://api.hackertarget.com/geoip/?q=" + d3)
print ("")
