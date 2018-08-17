import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Plex TUI")

class MainForm(npyscreen.FormBaseNewWithMenus):
    def create(self):
        y,x = self.useable_space()
        self.new_menu(name="Main Menu").addItemsFromList([
            ("Quit", self.exit_app),
        ])
        self.add(npyscreen.
    
    def exit_app(self):
        self.parentApp.setNextForm(None)
        self.editing=False
        self.parentApp.switchFormNow()

app = App()
app.run()
