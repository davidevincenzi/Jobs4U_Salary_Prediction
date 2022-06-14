import streamlit as st
from streamlit_option_menu import option_menu

from prediction_page import show_prediction_page
from dashboard_page import show_dashboard_page


page = option_menu(
	menu_title = "Jobs4U",
	options = ["Prediction", "Dashboard", "Contact"],
	icons = ["coin", "speedometer", "envelope"],
	default_index = 0,
	)

if page == "Prediction":
    show_prediction_page()
else:
    show_dashboard_page()