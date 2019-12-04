from selenium import webdriver
import time
import pickle

# 获取题库
# driver = webdriver.Chrome()
# driver.get('http://172.20.32.19/')
# driver.find_element_by_name("xuehao").send_keys("170153428")
# driver.find_element_by_name("password").send_keys("123456")
# driver.find_element_by_name("提交").click()
# time.sleep(1)
#
# answers = {}
# for dajuan_id in range(3000):
#     try:
#         driver.get('http://172.20.32.19/redir.php?catalog_id=6&cmd=dajuan_chakan&huihuabh=4' + str(dajuan_id).zfill(4) + '&mode=test')
#         shitis = driver.find_elements_by_class_name("shiti")
#         for shiti in shitis:
#             timu = shiti.find_element_by_tag_name("strong").text
#             if shiti.text.find("标准答案： ") > 0:
#                 answers[timu] = shiti.text[shiti.text.find("标准答案： ")+6:]
#                 with open("shiti.db", "wb") as f:
#                     pickle.dump(answers, f)
#                 print(timu, answers[timu], len(answers))
#     except:
#         pass
#
# time.sleep(10)
# driver.quit()


# 做题
driver = webdriver.Chrome()
driver.get('http://172.20.32.19/')
driver.find_element_by_name("xuehao").send_keys("170153434")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("提交").click()
time.sleep(1)

with open("shiti.db", "rb") as f:
    answers = pickle.load(f)
questions = answers.keys()
driver.get('http://172.20.32.19/redir.php?catalog_id=6&cmd=kaoshi_chushih&kaoshih=31327')
for i in range(10):
    shitis = driver.find_elements_by_class_name("shiti")
    for shiti in shitis:
        timu = shiti.find_element_by_tag_name("h3").text
        num = timu[:timu.find("、")]
        timu = timu[timu.find("、")+1:]
        if timu in questions:
            value = answers[timu]
            if value == "正确":
                value = "1"
            if value == "错误":
                value = "0"
            shiti.find_element_by_xpath("//input[@value='" + value + "' and @name='ti_" + num + "']").click()
            print(num, timu, value)
        else:
            print("题库没有该问题")
    try:
        driver.find_element_by_xpath("//input[@value='下一页']").click()
    except:
        driver.find_element_by_xpath("//input[@value='提交答卷']").click()
        break
