import time
from selenium import webdriver

# 打开edge
desired_cap = {
    "os": "OS X",
    "os_version": "Monterey",
    "browser": "Edge",
    "browser_version": "98.0.1108.51",
    "browserstack.local": "false",
    "browserstack.selenium_version": "3.141.0"
}
driver = webdriver.Edge(capabilities=desired_cap)
driver.get("https://xingye.me/game/eatkano/")

# 修改名字为username #######################
username = "不是人"
setting = driver.find_elements_by_css_selector('#btn_group > a.btn.btn-secondary.btn-lg')
setting[0].click()

name = driver.find_elements_by_css_selector('#username')
name[0].send_keys(username)

confirm = driver.find_elements_by_css_selector('#setting > button')
confirm[0].click()
##########################################
# 开始游戏
start_btn = driver.find_elements_by_css_selector('#btn_group > a.btn.btn-primary.btn-lg')
start_btn[0].click()

for layer in 50 * [1, 2]:
    for st in range(0, 40, 4):
        for n in range(st, st + 4):
            b = driver.find_elements_by_css_selector(f'#GameLayer{layer}-{n}')[0]
            if 't' in b.get_attribute("class"):
                b.click()
                time.sleep(0.02)
