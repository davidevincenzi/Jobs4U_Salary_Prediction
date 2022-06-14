import streamlit as st
from streamlit_option_menu import option_menu

from prediction_page import show_prediction_page
from dashboard_page import show_dashboard_page
from contacts_page import show_contacts_page


page = option_menu(
	menu_title = "Jobs4U",
	options = ["Prediction", "Dashboard", "Contacts"],
	icons = ["coin", "speedometer", "envelope"],
	default_index = 0,
	)

if page == "Prediction":
    show_prediction_page()
else if page == "Contacts":
	show_contacts_page()
else:
	show_dashboard_page()