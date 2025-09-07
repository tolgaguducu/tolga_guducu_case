# Test Automation Project
This is an End-to-End (E2E) test automation project based on Selenium and Pytest.

The project automates a 5-step scenario that tests the user journey from the homepage to finding a specific job position, filtering by location and department, verifying the results, and being redirected to the application page.

## ✨ Features

* **Page Object Model (POM):** Test logic and page interactions are separated to enhance code readability and maintainability.
* **Detailed Reporting:** Utilizes the **Allure Framework** to generate rich, interactive test reports.
* **Automatic Screenshots on Failure:** Automatically captures a screenshot at the point of failure and attaches it to the Allure report for easier debugging.
* **Robust Waiting Strategy:** Employs `WebDriverWait` (Explicit Waits) instead of static sleeps to handle dynamic page elements, making tests more stable and reliable.
* **Advanced User Interactions:** Implements `ActionChains` to simulate complex user actions like hover events.
* **Centralized Driver Management:** Uses a `DriverFactory` pattern for centralized WebDriver instantiation and configuration.
* **Code Standardization:** Enforces a consistent code style across the project using the `black` code formatter.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Test Framework:** Pytest
* **Browser Automation:** Selenium WebDriver
* **Reporting:** Allure Framework (`allure-pytest`)
* **Browser Driver Management:** webdriver-manager
* **Code Formatter:** black

## 🚀 Setup and Installation

To run this project on your local machine, please follow the steps below:

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd insider-test-automation
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows (PowerShell)
    .\venv\Scripts\activate

    # Activate on macOS / Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install all the required Python libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Allure Commandline:**
    To generate the HTML report, the Allure command-line tool must be installed on your system. For installation instructions, please refer to the [official Allure Framework documentation](https://docs.qameta.io/allure/#_installing_a_commandline).

## ⚡ Running the Tests

To execute the tests and generate the raw result files for the Allure report, run the following command in the project's root directory:
```bash
pytest --alluredir=allure-results
```

## 📊 Viewing the Report
After the test run is complete, use the Allure command-line tool to serve the interactive report:

```bash
allure serve allure-results
```


## 📁 Project Structure

```bash
.
├── pages/                # Page Object Model (POM) sınıfları
│   ├── base_page.py      # Tüm page object'ler için ortak metotlar (base class)
│   ├── careers_page.py   # Careers sayfası ile ilgili element & metotlar
│   ├── home_page.py      # Home sayfası için page object
│   ├── qa_jobs_page.py   # QA job listing sayfası için page object
│   └── lever_page.py     # Lever başvuru formu ile ilgili page object
├── tests/                # Test senaryoları
│   ├── conftest.py       # Pytest fixture'ları (setup/teardown, failure hook'ları)
│   └── test_career_application.py  # Kariyer başvurusu akışı testi
├── utils/                # Tekrar kullanılabilir yardımcı fonksiyonlar
│   └── driver_factory.py # WebDriver oluşturan factory
├── allure-results/       # Allure ham sonuçları (ci/pytest tarafından üretilir)
├── logs/                 # Test çalıştırmaları sırasında oluşturulan .log dosyaları
├── .env                  # IDE / local environment için gizli/konfigürasyon değişkenleri
├── .gitignore            # Git tarafından takip edilmeyecek dosyalar
├── pytest.ini            # Pytest yapılandırma ayarları
└── requirements.txt      # Projenin Python bağımlılıkları
```