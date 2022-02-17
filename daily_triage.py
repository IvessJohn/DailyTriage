import os
import webbrowser

from application import Application, AppTypes


def launch_apps(apps):
    """Launches given apps (executables, webpages, files) simultaneously.
    :param apps: list - Application-s to launch"""
    for app in apps:
        if app.path == "":
            raise ValueError("The path can not be an empty string!")
        
        if app.type == AppTypes.EXECUTABLE:
            os.startfile(app.path)
            continue
        if app.type == AppTypes.WEBPAGE:
            webbrowser.open_new_tab(app.path)
            continue