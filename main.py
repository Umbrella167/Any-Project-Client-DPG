from src.UI.Ui import ui
import dearpygui.dearpygui as dpg


def loop():
    pass


if __name__ == "__main__":
    dpg.create_context()
    ui.create_viewport()
    ui.show_ui()
    ui.run_loop(loop)
