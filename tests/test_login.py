from base.browser import Browser
from pages.login_page import LoginPage
from toolkit.logger import get_logger
import config

logger = get_logger(__name__)


def test_login():
    C = config.ACTIVE_CONFIG
    browser = Browser()

    try:
        logger.info("Start login test")
        page = LoginPage(browser)

        logger.info(f"Open URL: {C.BASE_URL}")
        page.open(C.BASE_URL)

        logger.info(f"Login with username={C.USERNAME}")
        page.login(C.USERNAME, C.PASSWORD)

        current_url = browser.driver.current_url
        logger.info(f"Current URL: {current_url}")

        assert "inventory" in current_url
        logger.info("✅ Login test passed")

    except Exception as e:
        logger.exception("❌ Login test failed with exception")
        raise
    finally:
        logger.info("Quit browser")
        browser.driver.quit()


if __name__ == "__main__":
    test_login()
