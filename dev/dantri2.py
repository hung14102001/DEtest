import time
import xlsxwriter
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


# show all replay comments
def showMoreCmt():
    while True:
        try:
            # find show more comment icon
            time.sleep(2)
            moreCmtButtons = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.comment-more"))
            )
            # click icon
            moreCmtButtons.click()

        except:
            break


# show all replay comments
def viewReplyCmt():

    while True:
        try:
            # find icon show reply comment
            time.sleep(2)
            cmtRepLinks = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.comment-reply"))
            )
            # click icon
            cmtRepLinks.click()

        except:
            break


if __name__ == "__main__":
    driver = webdriver.Chrome("/path/to/chromedriver")

    driver.get(
        "https://dantri.com.vn/kinh-doanh/evn-muon-tang-gia-dien-luc-nao-va-bao-nhieu-20221222115147876.htm"
    )

    wait = WebDriverWait(driver, 10)

    showMoreCmt()
    viewReplyCmt()
    # find all comments
    cmts = driver.find_elements(By.CLASS_NAME, "comment-text")

    # save in xlsx file
    workbook = xlsxwriter.Workbook("dantri2.xlsx")

    worksheet = workbook.add_worksheet()
    row = 0
    column = 0
    for cmt in cmts:

        worksheet.write(row, column, cmt.text)
        row += 1

    driver.close()
    workbook.close()
