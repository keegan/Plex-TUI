import npyscreen

class App(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Name")

class MainForm(npyscreen.ActionForm):
    def create(self):
        self.title = self.add(npyscreen.TitleText, name="Title", value="Hello World")

    def on_ok(self):
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.title.value="Hellow World"


if __name__ == "__main__":
    app  = App()
    app.run()
