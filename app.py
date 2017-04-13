__author__ = "Ambrosios"

from database import Database
from menu import Menu

Database.connect()

menu = Menu()

menu._run_menu()