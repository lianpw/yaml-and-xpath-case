import os, sys
sys.path.append(os.getcwd())
from base.base_action import BaseAction
import page


class PageSearch(BaseAction):
    # 点击搜索按钮
    def page_click_search(self):
        self.base_click(page.search_btn)

    # 输入搜索内容
    def page_input_value(self, value):
        self.base_input(page.search_input, value)

    # 点击返回按钮
    def page_back_btn(self):
        self.base_click(page.search_back)