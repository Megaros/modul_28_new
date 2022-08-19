Этот репозиторий — является итоговым проектом. Репозиторий был создан с использованием шаблона PageObject с Selenium и PyTest (Python). Проект содержит UI тесты интернет-магазина "Лабиринт" "https://www.labirint.ru/.

Подготовка к запуску:  
скопируйте репозиторий на свой компьютер,  
если вы используете PyCharm, он автоматически запрашивает установку необходимых библиотек,  
если нет - установите требуемые библиотеки в файле requirements.txt.  
Измените следующие данные:  
в Config/config.py измените путь на (актуальный для вашей ОС и версии вашего браузера) chromedriver и/или geckodriver:  
для macOS: CHROME_EXECUTABLE_PATH = "/path...to/chromedriver" FIREFOX_EXECUTABLE_PATH = "/path...to/geckodriver"  
для Windows: CHROME_EXECUTABLE_PATH = "C:\path...to\chromedriver.exe" FIREFOX_EXECUTABLE_PATH = "C:\path...to\geckodriver.exe"  
в Tests/conftest.py: если вы хотите начать тестирование браузеров Firefox и Chrome, оставьте (params=["chrome", "firefox"]),  
если вы хотите начать тестирование одного браузера за другим измените (params=["chrome "]) или (params=["firefox"]).
Чтобы НАЧАТЬ тест:  
для запуска всех тестов команда:  
для macOS: pytest Tests/* or pytest Tests  
для Windows: pytest Tests  
для запуска всех тестов и регистрации результатов в формате html:  
for macOS: pytest Tests/* -v --html=./hubSpot.html  
for Windows: pytest Tests -v --html=./hubSpot.html  
для запуска одного набора тестов:  
pytest Tests/test_File_Name.py  
для запуска одного теста:  
pytest Tests/test_File_Name.py::TestClassName::test_name  
Если вы запускаете тесты с журналом в html, ДЛЯ ПОЛУЧЕНИЯ ЖУРНАЛА выполнения теста:  
щелкните правой кнопкой мыши на "hubSpot.html" (файл будет создан после выполнения теста) щелкните COPY/PATH/Reference,  
щелкните «Absolute Path», чтобы открыть ссылку в браузере.  
Для получения новых результатов после выполнения «обновите» страницу с результатами.
