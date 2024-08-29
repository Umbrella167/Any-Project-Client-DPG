import dearpygui.dearpygui as dpg
import src.UI.Theme as theme
from src.UI.LayoutManager import layoutManager


class UiData:
    def __init__(self):
        pass


class DiyComponents:
    def __init__(self, data: UiData):
        pass


class UiCallBack:
    def __init__(self, data: UiData, component: DiyComponents):
        pass
    def save_layout(self,sender, app_data, user_data):
        if dpg.is_key_down(dpg.mvKey_Control) and dpg.is_key_down(dpg.mvKey_Control):
           layoutManager.save_layout()

class UI:
    def __init__(self):
        self._data = UiData()
        self._diycomponents = DiyComponents(self._data)
        self._callback = UiCallBack(self._data, self._diycomponents)
        self._theme = theme

    def show_ui(self):
        layoutManager.load_layout()
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def run_loop(self, func=None):
        if func is not None:
            while dpg.is_dearpygui_running():
                func()
                dpg.render_dearpygui_frame()
        else:
            dpg.start_dearpygui()

    def create_global_handler(self):
        with dpg.handler_registry() as global_hander:
            dpg.add_key_release_handler(label="save_layout",callback=self._callback.save_layout)
            

    def create_viewport(self, lable: str = "", width: int = 1920, height: int = 1080):
        self.create_global_handler()
        dpg.configure_app(
            docking=True,
            docking_space=True,
            init_file=layoutManager.dpg_window_config,
            load_init_file=True,
        )
        dpg.create_viewport(title=lable, width=width, height=height)


ui = UI()
