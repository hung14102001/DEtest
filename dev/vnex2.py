# import time
# import xlsxwriter
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium import webdriver


# def viewMoreCmt():
#     firstMoreCmt = wait.until(
#         EC.element_to_be_clickable(
#             (
#                 By.CSS_SELECTOR,
#                 "#box_comment_vne > div > div.view_more_coment.width_common.mb10",
#             )
#         )
#     )
#     driver.execute_script("arguments[0].click()", firstMoreCmt)
#     firstMoreCmt.click()

#     while True:
#         try:

#             time.sleep(1)
#             moreCmtButtons = wait.until(
#                 EC.element_to_be_clickable(
#                     (By.CSS_SELECTOR, "#list_comment > div:last-child > a")
#                 )
#             )
#             driver.execute_script("arguments[0].click();", moreCmtButtons)
#         except TimeoutException:

#             break


# def viewReplyCmt():

#     count = 0
#     while True:

#         try:
#             time.sleep(1)
#             cmtRepLink = wait.until(
#                 EC.element_to_be_clickable(
#                     (By.CSS_SELECTOR, "#list_comment > div > p > a")
#                 )
#             )
#             print(cmtRepLink.text)
#             driver.execute_script("arguments[0].click()", cmtRepLink)
#             count += 1

#         except TimeoutException:
#             print(count)
#             break


# def ContinueReading():
#     continueReadings = driver.find_elements(
#         By.CSS_SELECTOR,
#         "#list_comment > div > div.content-comment > p.content_less > a",
#     )
#     print("continueReadings: " + str(len(continueReadings)))
#     for cr in continueReadings:
#         time.sleep(3)
#         driver.execute_script("arguments[0].click();", cr)


# #
# def ContinueReadingCmtReply():
#     continueReadingCmtReply = driver.find_elements(
#         By.CSS_SELECTOR,
#         "#list_comment > div > div > div > div.content-comment > p.content_less > a",
#     )
#     print("continueReadings: " + str(len(continueReadingCmtReply)))
#     for crcr in continueReadingCmtReply:
#         time.sleep(3)
#         driver.execute_script("arguments[0].click();", crcr)


# if __name__ == "__main__":
#     driver = webdriver.Chrome("/path/to/chromedriver")
#     driver.get(
#         "https://vnexpress.net/hlv-park-khong-cuoi-du-thang-dam-lao-4551167.html"
#     )
#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     wait = WebDriverWait(driver, 15)

#     viewMoreCmt()

#     viewReplyCmt()

#     ContinueReading()

#     ContinueReadingCmtReply()

#     continue_reading_cmt_reply = driver.find_elements(
#         By.CSS_SELECTOR,
#         "#list_comment > div > div > div > div.content-comment > p.content_less > a",
#     )

#     print("continue_reading_cmt_reply: " + str(len(continue_reading_cmt_reply)))

#     cmts = driver.find_elements(By.CSS_SELECTOR, "p.full_content")

#     workbook = xlsxwriter.Workbook("vnex2.xlsx")

#     worksheet = workbook.add_worksheet()

#     row = 0
#     column = 0
#     for cmt in cmts:

#         print(cmt.text)
#         worksheet.write(row, column, cmt.text)
#         row += 1
#     cmtsMore = driver.find_elements(By.CSS_SELECTOR, "p.content_more")
#     if cmtsMore:
#         print(driver.find_element(By.CSS_SELECTOR, "p.content_more").text)
#         for cmt in cmtsMore:

#             print(cmt.text)
#             worksheet.write(row, column, cmt.text)
#             row += 1
#     print(row)

#     workbook.close()

#     driver.quit()

import time
import xlsxwriter
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver

# View more comment function
def viewMoreCmt():
    firstMoreCmt = wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "#box_comment_vne > div > div.view_more_coment.width_common.mb10",
            )
        )
    )
    driver.execute_script("arguments[0].click()", firstMoreCmt)
    firstMoreCmt.click()

    while True:
        try:

            time.sleep(1)
            moreCmtButtons = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#list_comment > div:last-child > a")
                )
            )
            driver.execute_script("arguments[0].click();", moreCmtButtons)
        except TimeoutException:

            break


# View all reply comment
def viewReplyCmt():

    while True:

        try:
            time.sleep(1)
            # find icon view reply comment
            cmtRepLink = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#list_comment > div > p > a")
                )
            )
            # click icon
            driver.execute_script("arguments[0].click()", cmtRepLink)

        except TimeoutException:
            break


# Continue reading long comment
def ContinueReading():
    # Find all icon show full comment
    continueReadings = driver.find_elements(
        By.CSS_SELECTOR,
        "#list_comment > div > div.content-comment > p.content_less > a",
    )
    for icon in continueReadings:
        time.sleep(3)
        # click icon
        driver.execute_script("arguments[0].click();", icon)


# Continue reading long reply comment
def ContinueReadingCmtReply():
    # Find all icon show full comment
    continueReadingCmtReply = driver.find_elements(
        By.CSS_SELECTOR,
        "#list_comment > div > div > div > div.content-comment > p.content_less > a",
    )

    for icon in continueReadingCmtReply:
        time.sleep(3)
        driver.execute_script("arguments[0].click();", icon)


if __name__ == "__main__":
    driver = webdriver.Chrome("/path/to/chromedriver")
    driver.get(
        "https://vnexpress.net/hlv-park-khong-cuoi-du-thang-dam-lao-4551167.html"
    )
    driver.maximize_window()
    driver.implicitly_wait(10)

    wait = WebDriverWait(driver, 15)

    viewMoreCmt()

    viewReplyCmt()

    ContinueReading()

    ContinueReadingCmtReply()

    # find all  comments
    cmts = driver.find_elements(By.CSS_SELECTOR, "p.full_content")

    workbook = xlsxwriter.Workbook("vnex2.xlsx")
    worksheet = workbook.add_worksheet()

    row = 0
    column = 0
    for cmt in cmts:
        # text comment
        cmtText = cmt.text
        # take name who comment
        nameCmt = driver.execute_script(
            "return arguments[0].firstChild.textContent", cmt
        )
        # take comment content
        cmtText = cmtText.replace(nameCmt, "")
        # save in xlsx file
        worksheet.write(row, column, nameCmt)
        print(cmtText)
        worksheet.write(row, column + 1, cmtText)
        row += 1
    # find all long comments
    longCmts = driver.find_elements(By.CSS_SELECTOR, "p.content_more")
    if longCmts:
        for longCmt in longCmts:
            longCmtText = longCmt.text
            # take name who write comment
            commentAuthor = driver.execute_script(
                "return arguments[0].firstChild.textContent", longCmt
            )
            # take comment content
            longCmtText = longCmtText.replace(commentAuthor, "")
            # save in xlsx file
            worksheet.write(row, column, commentAuthor)
            worksheet.write(row, column + 1, longCmtText)
            row += 1

    workbook.close()

    driver.quit()
