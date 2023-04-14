# Плавный вход в Python
Здесь собраны основные quick start программы и скрипты на python. В дополнении представлены полезные ссылки и гайды по установке и запуску среды программирования. 

Презентацию введения с ссылками на источники можно взять по [ссылке](https://docs.google.com/presentation/d/1Y0ykNofupLzioS66xSxleAm_sMVdBT1Z/edit?usp=share_link&ouid=117033173110504155765&rtpof=true&sd=true)

## Оглавление

1. [Установка Python :hatching_chick:](#установка-python)
2. [Среды разработки на Python (IDE)](#среды-разработки-на-python-ide)
3. [Установка библиотек и создание виртуального окружения](#pip-venv)
    1. [Зачем нужен ```pip```](#зачем-нужен-pip)
    2. [Зачем нужно виртуальное окружение](#зачем-нужно-виртуальное-окружение)
4. [Шаблоны задач :newspaper:](#шаблоны-задач-newspaper)
5. [Полезные ссылки :books:](#ok-links)
    
____
## Установка Python
Python определенной версии можно скачать на официальном [сайте](https://www.python.org/downloads/).
При открытии файла установки поставьте галочку как на картинке и запустите Install Now:
<p align="center">
    <img src=./media/install-python-1.jpg width="450" height="300" />
</p>

Проверить успех установки можно так. Откройте командную строку (cmd, powershell) и выполните команду: 
```console
python --version
```
В случае успеха Вы увидете версию Вашего питона

__Основные команды для работы с python из командной строки (cmd, powershell)__
1. Запустить выполениние файла .py:
```console
python путь-название-файла.py
```
(остановить выполнение можно горячими клавишами Ctrl+C)

2. Запустить среду выполнения кода внутри командной строки (аналог командной строки для написания кода, как в matlab):
```console
python
```
Выйти из этой среды можно написав функцию `exit()` внутри командной строки.

____
## Среды разработки на Python (IDE)
__Вы можете__ скачать платформу [Anaconda](https://www.anaconda.com/products/distribution/start-coding-immediately), где все будет сразу (Jupyter, JupyterLab, Spider и несколько базовых библиотек).

Причем для запуска Jupyter или JupyterLab достаточно будет зайти в командную стоку и выполнить две команды:
1. перейти в каталог Вашего проекта:
```console
cd "абсолютный-путь-до-проекта"
```
2. открыть Jupyter или JupyterLab, после этого переходите по ссылке в командной строке в браузер:
```console
jupyter lab
```
(если не запускается, попробуйте `jupyterlab`). Для открытия Jupyter используйте команду `jupyter notebook`

__Вы можете__ установить open-source IDE [VSCode](https://code.visualstudio.com/) с синхронизацией настроек, приятным интерфейсом и большим количеством плагинов для приятной работы (при открытии файла определенного формата, он сам предложит установить Вам тот или иной плагин). 

Плагин для работы с ноутбуками так и называется Jupyter)

[В этой статье](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) описан функционал для работы с питоновскими ноутбуками, в частности:
* как запускать ячейки;
* как просмотреть переменные;
* как поменять версию питона, на которой будет выполняться ваш код.

Если Вы установили VSCode, то можете с помощью pip установить базовые библиотеки, которые перечислены в файлике [requirements.txt](/requirements.txt). Как это сделать описано ниже.

____
## Зачем нужен ```pip```
pip - это пакетный менаджер, который живет в вашей системе (будет жить после установки). Он необходим для удобной работы с библиотеками и фреймворками.

Если вы пользуетесь Python 2.7.9 (и выше) или Python 3.4 (и выше), pip устанавливается вместе с Python по умолчанию. Если Вы используете младшую версию Python pip можно установить следуя [гайду](https://pythonru.com/baza-znanij/ustanovka-pip-dlja-python-i-bazovye-komandy)

__Основные команды для работы с pip (в новых версиях может встречаться pip3 вместо pip) (в комнадной строке cmd, powershell)__

1. Установить нужную библиотеку:
```console
pip install название-библиотеки
```
Если нужна библиотека конкретной версии
```console
pip install 'название-библиотеки=версия'
```
Если у Вас уже установлена какая-то версия, а Вы хотите ее переустановить, испольуйте команду `--force-reinstall`:
```console
pip install 'название-библиотеки=версия' --force-reinstall
```

2. Установить библиотеки из текстового файла:
```console
pip install -r "путь-до-файла/requirements.txt"
```

3. Удалить библиотеку:
```console
pip uninstall название-библиотеки
```

4. Сохранить все установленные библиотки в проекте или в системе в тектовый файл `requirements.txt`:
```console
pip freeze > requirements.txt
```
____
## Зачем нужно виртуальное окружение?
Виртуальное окружение полезно, чтобы избегать конфликта версий конктретной библиотеки в Вашем проекте, а также чтобы изолировать Ваш проект. Т.е. в Вашем проекте будет жить отдельный маленький питон.

Создать виртуальную среду просто в корневом каталоге Вашего проекта в командной строке пропишите команду:
```console
python -m venv "имя-папки-где-будет-жить-ваша-виртуальная-среда(часто называют env)"
```
(команда `python` такая же как для запуска когда см. [установка python](#установка-python))

После создания виртуальной среды ее нужно активировать командой:
```console
"имя-папки-где-будет-жить-ваша-виртуальная-среда(часто называют env)"\Scripts\activate
```
____
## Шаблоны задач :newspaper:

Ниже в таблице приведены примеры кода на pyhton, а также примеры работы с must have библиотеками:

| пример кода для старта в задаче | описание |
|----------------|:----------------|
| [работа с табличными данными](/templates/1.%20tables/table-work.ipynb)| открытие, сохранение файлов, просмотр, статистики, группировки, агрегации, склеки, сводные таблицы |
| [визуализация данных](/templates/2.%20data%20visualisation/data-plots.ipynb) | построение линейных, точечных, контурных, трехмерных графиков | 
| [работа с картинками, видео](/templates/3.%20images/) |  |
| [ООП](/templates/4.%20oop/test.ipynb) | примеры написания классов | 
| [запросы на сторонние API-ресурсы (GET-запросы)](/templates/5.%20requests/) |  | 
| [возможный :smirk: шаблон проекта на Python](/templates/6.%20py_project/) |  | 

____
## Полезные ссылки :books:
* Описание этикета написания кода на python, которые рекоммендуют разработчики языка, - [PEP8](https://pep8.org/) (кратко на русском [тут](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html))
* Хендбук от Яндекса для обучения на Python: https://academy.yandex.ru/handbook/python
* Лекции по программированию на Python от Computer Science School: https://youtube.com/playlist?list=PLlb7e2G7aSpQmGnhrxlqI4iMXNv4R7khy;
* Обучение Python на практических задачках: https://www.hackerrank.com/python-tutorial/;
* Обучение Python в играх (Программируй, чтобы играть!): https://dtf.ru/u/367155-shkola-programmirovaniya-piksel/973952-top-8-igr-chtoby-nauchitsya-programmirovaniyu-na-python;
* Курс по разработке на Python (школа бэкенда Яндекса): https://habr.com/ru/companies/yandex/articles/498856/;
* Школа от МФТИ для анализа данных, изучения машинного обучения и нейронных сетей:  https://dls.samcs.ru/;
* Telegram канал по Python, библиотекам, курсам, новым технологиям: https://t.me/data_analysis_ml; 
