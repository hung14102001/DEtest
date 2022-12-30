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
        "https://vnexpress.net/doi-truong-lao-xin-doi-ao-voi-van-quyet-4551264.html"
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

    workbook = xlsxwriter.Workbook("vnex1.xlsx")
    worksheet = workbook.add_worksheet()

    row = 0
    column = 0
    for cmt in cmts:
        # text comment
        cmtText = cmt.text
        # take name who comment
        commentAuthor = driver.execute_script(
            "return arguments[0].firstChild.textContent", cmt
        )
        # take comment content
        cmtText = cmtText.replace(commentAuthor, "")
        # save in xlsx file
        worksheet.write(row, column, commentAuthor)
        worksheet.write(row, column + 1, cmtText)
        row += 1
    # find all long comments
    cmtsMore = driver.find_elements(By.CSS_SELECTOR, "p.content_more")
    if cmtsMore:
        cmtText = cmt.text
        # take name who comment
        nameCmt = driver.execute_script(
            "return arguments[0].firstChild.textContent", cmt
        )
        # take comment content
        cmtText = cmtText.replace(nameCmt, "")
        # save in xlsx file
        worksheet.write(row, column, nameCmt)
        worksheet.write(row, column + 1, cmtText)
        row += 1

    workbook.close()

    driver.quit()
