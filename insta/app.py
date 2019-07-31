# Reference
import sys
import time
import datetime
import random
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import NoSuchElementException

class MyApp():
    def instagramStart(self):
        # ======== 1. Setting Options =======
        self.options = webdriver.ChromeOptions()

        # Chrome을 안 띄우고 수행하고 싶으면 아래 주석을 해제(리눅스 서버에서 작업시 headless 추천, 디버깅시는 headless 주석처리)
        # options.add_argument("headless")

        # Chrome 설정 : 진짜 유저가 작업하는 것처럼 보이도록 설정
        self.options.add_argument("window-size=1920x1080")
        self.options.add_argument("disable-gpu")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        )
        self.options.add_argument("lang=ko_KR")

        # ======= 2. Setting id, password, hashtag ======

        id = "oceanfog1@gmail.com"
        password = "1234@Aoeu"

        hash_tag = "냉면"
        hash_tags_count = 600

        # ======== 3. InstaJob Class ======
        print("browser loading..")
        global browser
        browser = webdriver.Chrome(
            # "/Users/jihyun/Documents/GitHub/instagram-auto-like-with-Python/chromedriver_74",
            sys.path[1] + "/chrome/chromedriver74",
            chrome_options=self.options,
        )

        browser.get("https://instagram.com/")

        # 로그인
        login_link = browser.find_element_by_css_selector(
            "p.izU2O"
        ).find_element_by_css_selector("a")
        login_link.click()
        time.sleep(3.5)

        username_input = browser.find_elements_by_css_selector("input._2hvTZ")[0]
        username_input.send_keys(id)
        time.sleep(2 + random.random() * 0.3)
        password_input = browser.find_elements_by_css_selector("input._2hvTZ")[1]
        password_input.send_keys(password)
        time.sleep(1)
        password_input.submit()
        time.sleep(2)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            for i in range(timeline_like_count):
                time.sleep(1.5)

                browser.find_elements_by_css_selector(
                    "span.fr66n > button > span"
                    # "span.glyphsSpriteHeart__outline__24__grey_9.Szr5J"
                )[0].click()

                time.sleep(1.5)

        except Exception as e:
            print("Error! ", e)
            # slacker.chat.post_message("#general", text="raise timeline like error")
            pass


            try:
                print(hash_tag + " 좋아요 작업을 시작합니다")
                browser.get("https://www.instagram.com/explore/tags/" + quote(hash_tag))
                time.sleep(5 + random.random() * 1.2)
                element = browser.find_elements_by_css_selector("div._9AhH0")[9]
                element.click()
                time.sleep(5)

                count_number = hash_tags_count

                for i in range(1, count_number):
                    try:
                        # 좋아요 해쉬태그 지정
                        like = browser.find_element_by_css_selector(
                            "span.fr66n > button > span"
                            # "span.glyphsSpriteHeart__outline__24__grey_9.Szr5J"
                        )
                        # 좋아요 해쉬태그 클릭
                        like.click()

                        # 다음 포스팅으로 넘어가기전 대기
                        time.sleep(2 + random.random() * 1.2)

                        # 다음 포스팅으로 넘어감
                        browser.find_element_by_css_selector(
                            "span.glyphsSpriteHeart__outline__24__grey_9.Szr5J"
                        ).click()

                        time.sleep(3.2 + random.random() * 1.3)
                    except:
                        browser.find_element_by_css_selector(
                            "a.HBoOv.coreSpriteRightPaginationArrow"
                        ).click()
                        time.sleep(1 + random.random() * 1.2)

            except NoSuchElementException as e:
                print("NoSuch Error", e)
                pass

            except Exception as e:
                print("Error! ", e)


if __name__ == "__main__":
    ex = MyApp()
    ex.instagramStart()
