## Установка потрібних програм

Як що потрібно показувати систему моніторингу (метрики) установіть пункт 2,
пункт 1,3 обовязковий для запуска проекта 

1. Установка компонентів для сайта
    1. Установка python
    [Посилання на установник python 3.12.3](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)
    2. Установка git [Посилання на git установник](https://github.com/git-for-windows/git/releases/download/v2.45.1.windows.1/Git-2.45.1-64-bit.exe)

2. Установка компонентів для моніторингу (метрики)
     1. [Відео установки docker і wsl](https://www.youtube.com/watch?v=goBwSrfEqBk&t=281s)
     2. Включення віртуалізації [Посилання на сайт як включити віртуалізації в біосі](https://daad.org.ua/13444-yak-vklyuchiti-virtualizatsiyu-v-bios-dokladna-instruktsiya.html)
    аналогічне можна найти на ютубі
    3. Установка docker [Посилання на git установник](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module&_gl=1*10x9x1*_ga*MTEyNDUzMTkwNS4xNzE2MjM3NTAy*_ga_XJWPQMJYHQ*MTcxNjk4OTUyNC4xNi4xLjE3MTY5ODk1MjguNTYuMC4w)
    4. Установка Virtualbox [Посилання на git установник](https://download.virtualbox.org/virtualbox/7.0.18/VirtualBox-7.0.18-162988-Win.exe)
 
3. Установка програми для бази даних
   1. Установка Sqlite studio [Посилання на sqlite studio установник](https://github.com/pawelsalawa/sqlitestudio/releases/download/3.4.4/SQLiteStudio-3.4.4-windows-x64-installer.exe) 

## Установка проекта і активація віртуального середовища

1. Установка проекта 
   1. Створити нову папку
   2. Відкрите в ній cmd консоль
   3. Копірайте команду і установіть в консоль, запустіть її **Enter**
   ```bash
   git clone https://github.com/Vasyl20/project_django_docker_.git
   ```
   4. Видаліть папку .git з проекта, відкрите папку проекта в провіднику у навбар панелі натисніть на вигляд і у відображені прихованих натисніть галочку на приховані елементи, після цього в папці проекта зявиться папка .git, видаліть її.

   5. Запустіть команди по черзі в cmd консолі
        ``` bash
        cd project_django_docker_
        ```
        ```bash
        env\Scripts\activate
        ```

## Запуск сервера проекта 

1. Запуск проекта, запустити команду в терміналі
     ```bash
     python manage.py runserver
     ```
2. Копірайте посилення і вставте в браузер, **Enter**
   ```bash
    http://127.0.0.1:8000/
    ```
3. Зупинка сервера, відкрийте термінал і натиснути **Ctrl + C**
4. Панель адміністратора 
    ```bash
    http://127.0.0.1:8000/admin
    ```
5. Логін: admin пароль: admin1
   
На цьому етапі буде досить для того, щоб показати сам сайт,
як що потрібно показати метрики (моніторинг) тоді ідемо далі

## Запуск контейнерів docker

1. Запустити програму Docker Desktop, попередньо установлено в **Установник потрібних програм** пунк 2
2. В терміналі проекта запустити команду
   ```bash
   docker-compose up --build
   ```
3. Дочекайтесь розгортання всіх контейнерів, приблизно 2-4 хв
4. На англійській розкладці в терміналі натиснути **v** букву, відкриється Dcoker Desktop, тут ви побачите 3 запущені контейнери, можете нажати на контейнер на саму лінку
   ![](./myapp/static/png/172514.png)

5. Натиснути на любу лінку контейнерів
6. Список контейнерів:
   + grafana (метрики) - 3000:3000⁠  
   + prometheus (збирач метриків) - 9090:9090
   + server (сайт) - 8000:8000
