from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=10, poll=1):
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == 'By.XPATH':
            loc_value = self.make_xpath_with_feature(loc_value)
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(loc_by, loc_value))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        self.base_find_element(loc).send_keys(value)

    def make_xpath_with_unit_feature(slef, loc):
        """
        拼接xpath中间的部分
        :param loc:
        :return:
        """
        key_index = 0
        value_index = 1
        option_index = 2

        args = loc.split(',')
        feature = ""

        if len(args) == 2:
            feature = 'contains(@' + args[key_index] + ',"' + args[value_index] + '")' + 'and'
        elif len(args) == 3:
            if args[option_index] == '1':
                feature = '@' + args[key_index] + '="' + args[value_index] + '"' + 'and'
            elif args[option_index] == '0':
                feature = 'contains(@' + args[key_index] + ',"' + args[value_index] + '")' + 'and'

        return feature

    def make_xpath_with_feature(self, loc):
        feature_start = "//*["
        feature_end = ']'
        feature = ""

        if isinstance(loc, str):
            # 如果是正常的xpath, 直接返回
            if loc.startswith('//'):
                return loc

            # loc 字符串
            feature = self.make_xpath_with_unit_feature(loc)
        else:
            # loc 列表
            for i in loc:
                feature += self.make_xpath_with_unit_feature(i)
        feature = feature.rstrip('and')
        loc = feature_start + feature + feature_end
        return loc