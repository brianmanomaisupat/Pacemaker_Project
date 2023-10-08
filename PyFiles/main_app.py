''' Import Libraries '''
from tkinter import *
import customtkinter
from tkinter import font
import json
import os


''' Import External Classes '''
from program_classes.user_class import user

''' App Class '''
class DCM(customtkinter.CTk):
  # class variables
  bg_colour = "#1A1A1A"

  gray_1 = "#2A2A2A"
  gray_2 = "#8f8f8f"
  gray_3 = "#888888"

  blue_1 = "#195FA6"

  white_1 = "#D9D9D9"

  green_1 = "#3FAB4A"
  green_2 = "#67AB6E"

  red_1 = "#D13434"
  red_2 = "#D25E5E"

  # init function to initialize the window
  def __init__(self):
    # intialize master screen
    super().__init__()
    self.title("G29 - MECHTRON 3K04 - DCM")
    self.geometry("1000x700")
    self.resizable(height=False, width=False)
    self.create_login_screen()
    #self.create_main_interface()
  
  # Methods for Page navigation

  def create_login_screen(self):
    self.frm_login_screen = customtkinter.CTkFrame(master=self, fg_color = DCM.bg_colour)
    self.frm_login_screen.pack(fill='both', expand=True)

    font_text_box = customtkinter.CTkFont(family="Lexend", size=15)
    font_buttons = customtkinter.CTkFont(family="Lexend SemiBold", size=20)
    font_title = customtkinter.CTkFont(family="Lexend", weight="bold",size=50)
    font_name = customtkinter.CTkFont(family="Lexend", weight="bold",size=35)

    # center screen frame
    self.frm_login_box = customtkinter.CTkFrame(master=self.frm_login_screen, width=357, height=601, fg_color=DCM.gray_1, corner_radius=15, border_width=3, 
                           border_color=DCM.blue_1).place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # Login label title
    customtkinter.CTkLabel(master=self.frm_login_screen, text="Login", width=143, height=63, fg_color=DCM.gray_1, text_color=DCM.white_1, font=font_title).place(relx=0.5, rely=0.2, anchor=CENTER)

    # sign in button
    customtkinter.CTkButton(master=self.frm_login_box, width = 191, height=43, text="Sign In", font=font_buttons, 
                            state="normal",corner_radius=40, fg_color=DCM.blue_1).place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    # username text box
    self.txtbx_username = customtkinter.CTkEntry(master=self.frm_login_screen, placeholder_text="Enter Username", width=295, height=39, fg_color=DCM.white_1,
                                                text_color=DCM.gray_1, placeholder_text_color=DCM.gray_2, font=font_text_box).place(relx = 0.5, rely=0.4, anchor=CENTER)
    

  def create_main_interface(self):
    #fonts
    font_text_box = customtkinter.CTkFont(family="Lexend", size=15)
    font_buttons = customtkinter.CTkFont(family="Lexend SemiBold", size=20)
    font_title = customtkinter.CTkFont(family="Lexend", weight="bold",size=50)
    font_username = customtkinter.CTkFont(family="Lexend", weight="bold",size=35)
    font_sections = customtkinter.CTkFont(family="Lexend", weight="bold",size=24)
    font_curmode = customtkinter.CTkFont(family="Lexend", size=20)
    font_connect = customtkinter.CTkFont(family="Lexend", size=15)

    #frame
    self.frm_main_interface = customtkinter.CTkFrame(master=self, fg_color = DCM.bg_colour)
    self.frm_main_interface.pack(fill='both', expand=True)
   
    #admin button
    customtkinter.CTkButton(master=self.frm_main_interface, width = 252, height=43, text="Admin", state="normal", font=font_buttons, fg_color=DCM.blue_1).place(x = 22, y = 306)
    #run button 
    customtkinter.CTkButton(master=self.frm_main_interface, width = 117, height=43, text="Run", state="disabled", font=font_buttons, fg_color=DCM.green_1, hover_color=DCM.green_2).place(x = 22, y = 368)
    #stop button 
    customtkinter.CTkButton(master=self.frm_main_interface, width = 117, height=43, text="Stop", state="disabled", font=font_buttons, fg_color=DCM.red_1, hover_color=DCM.red_2).place(x = 159, y = 368)
    #sign out button 
    customtkinter.CTkButton(master=self.frm_main_interface, width = 252, height=43, text="Sign Out", state="normal", font=font_buttons, fg_color=DCM.blue_1).place(x = 22, y = 546)
    #delete account button 
    customtkinter.CTkButton(master=self.frm_main_interface, width = 252, height=33, text="Delete Account", state="disabled", font=font_buttons, fg_color=DCM.red_1, hover_color=DCM.red_2).place(x = 22, y = 603)
  
    #text for permissions
    customtkinter.CTkLabel(master=self.frm_main_interface, text="Permission: Client", width=143, height=34, fg_color=DCM.bg_colour, text_color=DCM.gray_3, font=font_buttons).place(x=22, y=651)
    #text for permissions
    customtkinter.CTkLabel(master=self.frm_main_interface, text="John Smith", width=199, height=40, fg_color=DCM.bg_colour, text_color=DCM.white_1, font=font_username).place(x=22, y=49)
    #text for mode
    customtkinter.CTkLabel(master=self.frm_main_interface, text="Mode", width=67, height=30, fg_color=DCM.bg_colour, text_color=DCM.gray_3, font=font_sections).place(x=22, y=104)
    #text for current mode
    customtkinter.CTkLabel(master=self.frm_main_interface, text="Current Mode: None", width=200, height=15, fg_color=DCM.bg_colour, text_color=DCM.gray_3, font=font_curmode).place(x=22, y=188)
    #text for parameters
    customtkinter.CTkLabel(master=self.frm_main_interface, text="Parameters", width=142, height=30, fg_color=DCM.bg_colour, text_color=DCM.gray_3, font=font_sections).place(x=300, y=49)
  
    #text for connected
    customtkinter.CTkLabel(master=self.frm_main_interface, text="🟢 Connected", width=154, height=34, fg_color=DCM.bg_colour, text_color=DCM.gray_3, font=font_connect).place(x=5, y=9)
    


  # Other methods

  # Functions

''' Main '''
if __name__ == "__main__":
  dcm = DCM()
  dcm.mainloop()
