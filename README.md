# 🧪 Selenium Automation Framework (POM + Toolkit + Logging)

本專案是基於 **Selenium + Page Object Model（POM）** 所設計的  
可維護、自動化程度高、可跨專案複用的測試框架。

今天新增了「專業級 Logging 系統」，可同時輸出到：

- 終端機（測試時立即看到進度）
- `logs/test_run.log`（永久保存 log，方便除錯與追蹤）

---

# 🚀 Features（框架特色）

### ✔ Page Object Model（POM）
每個頁面都封裝成獨立物件，維護容易、結構清楚。

### ✔ Toolkit（跨專案通用工具）
包含：

- `wait_and_click`
- `wait_and_type`
- `wait_and_get_text`
- `is_visible`
- `wait_for_url`

所有 Page 自動繼承，提高穩定性與可複用性。

### ✔ BasePage（POM 抽象層）
封裝共用方法：

- type()  
- click()  
- get_text()  
- wait_for_url()  
- 可選自動 logging  

### ✔ Browser 管理
- 建立 driver  
- 建立 WebDriverWait  
- 提供 quit()  
- 集中瀏覽器生命週期

### ✔ Logging（今日新增 ✨）
- 自動建立 `/logs/test_run.log`
- 終端機 + 檔案雙輸出
- INFO / ERROR / EXCEPTION 支援
- 讓測試更像正式產品可控性高

---

# 📂 Project Structure（專案結構）

```
sdet-training/
│  config.py
│  README.md
│
├── logs/
│     test_run.log      # 今日新增：所有測試執行紀錄
│
├── toolkit/
│     __init__.py
│     web_toolkit.py    # 等候、點擊、輸入 等動作通用工具
│     logger.py         # 今日新增：統一 Logging 工具
│
├── base/
│     __init__.py
│     base_page.py      # Page 層抽象父類別
│     browser.py        # Driver + Wait 管理
│
├── pages/
│     __init__.py
│     login_page.py     # LoginPage（POM 實作）
│
└── tests/
      __init__.py
      test_login.py     # 今日強化：加入 logger、例外處理
```

---

# ▶ 如何執行（Running Tests）

在專案根目錄執行：

```
python -m tests.test_login
```

執行後你會看到：

- 終端機即時 log
- Chrome 自動開啟、登入、驗證
- 測試結果寫入 `logs/test_run.log`

---

# 📝 Example Log Output（範例日誌）

```
2025-02-xx 12:34:56 [INFO] tests.test_login - Start login test
2025-02-xx 12:34:57 [INFO] tests.test_login - Open URL: https://www.saucedemo.com/
2025-02-xx 12:34:57 [INFO] tests.test_login - Login with username=standard_user
2025-02-xx 12:34:58 [INFO] tests.test_login - Current URL: https://www.saucedemo.com/inventory.html
2025-02-xx 12:34:58 [INFO] tests.test_login - ✅ Login test passed
2025-02-xx 12:34:58 [INFO] tests.test_login - Quit browser
```

---

# 📈 Today's Progress（今日新增內容）

✨ **新增 Logging 架構（可終端機 + 檔案輸出）**  
✨ `toolkit/logger.py` 完成  
✨ 測試案例加入 logger / exception handling  
✨ 新增 `logs/` 資料夾並自動寫入 test_run.log  
✨ test_login 自動輸出詳細測試流程  
✨ 測試框架邁向企業級架構

---

# 🔮 Next Steps（明日建議）

- 加入 InventoryPage（登入後的頁面）
- 加入更多測試案例（加入購物車、商品列表驗證）  
- 在 BasePage 增加更多通用動作（scroll、hover、select）  
- 開始導入 **pytest + fixtures**（正式企業用法）  
- 加入 Screenshot / retry / error handler  
- 最終整合 CI/CD（GitHub Actions）

---

# 📧 Author

Cheng Lun Fan  
目標職位：SDET / Automation Engineer  
技能方向：Python、Selenium、API、Test Framework Development  
