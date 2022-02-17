import daily_triage
from application import Application, AppTypes

apps = [
    Application("https://twitter.com/ivess_john", AppTypes.WEBPAGE),
    Application("https://mail.google.com/mail/u/0/#inbox", AppTypes.WEBPAGE),
    Application("https://mail.google.com/mail/u/1/#inbox", AppTypes.WEBPAGE),
    #Application("C:\Users\Ivan\AppData\Local\Discord\app-1.0.9003\Discord.exe", AppTypes.EXECUTABLE),
]

daily_triage.launch_apps(apps)