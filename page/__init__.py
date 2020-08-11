from selenium.webdriver.common.by import By
# 以下为搜索页面的元素配置信息
# 搜索按钮
search_btn = By.ID, 'com.android.settings:id/search'
# 输入文本框
search_input = By.ID, 'android:id/search_src_text'
# 返回按钮
search_back = By.CLASS_NAME, 'android.widget.ImageButton'