import flet as ft
import controller as c

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.parole=""
        self.t=0

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self._selezioneLingua = ft.Dropdown(label="Select Language",
                                            options=[ft.dropdown.Option("english"), ft.dropdown.Option("italian"),
                                                     ft.dropdown.Option("spanish")])

        self._selezioneModalita = ft.Dropdown(label="Search Modality",
                                              options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"),
                                                       ft.dropdown.Option("Dichotomic")])
        self._insTesto = ft.TextField(label="Add your sentence here")
        self._btnSubmit = ft.ElevatedButton(text="Spell check", icon=ft.icons.SEARCH,
                                            on_click=self.handleClick)
        self._listV = ft.ListView(controls=[])
        self.page.banner = ft.Banner(bgcolor=ft.colors.AMBER_100, leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=100),content=ft.Text("CAMPI MANCANTI" ),actions=[ft.TextButton("Okay", on_click=self.close_banner),])
        self.page.banner.close = True

        row1 = ft.Row([self._selezioneLingua])
        row2 = ft.Row([self._selezioneModalita, self._insTesto, self._btnSubmit])
        row3 = ft.Row([self._listV])
        self.page.add(row1,row2, row3)

        self.page.update()
    def close_banner(self, e):
        self.page.banner.open = False
        self.page.update()

    def handleClick(self, e):
        if self._insTesto.value=="" or self._selezioneLingua.value=="" or self._selezioneModalita.value== None:
            self.page.banner.open=True
            self.update()
            return
        (self.parole, self.t) = self.__controller.handleSentence(self._insTesto.value,self._selezioneLingua.value, self._selezioneModalita.value)
        self._listV.controls.append(ft.Text("Fraseinserita: "+self._insTesto.value))
        self._listV.controls.append(ft.Text("Parole errate: "+self.parole))
        self._listV.controls.append(ft.Text("Tempo eseguito: "+str(self.t)))
        self._insTesto.value=""
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
