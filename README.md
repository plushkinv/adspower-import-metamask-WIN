# adspower-import-metamask-WIN

!!!Версия скрипта для пользователей Windows, Смотрите инструкцию https://youtu.be/K-xwRRE6iZA
!! Автор скрипта PLushkin https://t.me/plushkin_blog   
! По мотивам оригинального скрипта Ивана https://t.me/hodlmodeth

данный скрипт импортирует заранее созданные метамаски в твои готовые профили в adspower. скрипт написан на скорую руку, для меня было главное чтобы все работало. после импорта он добавляет сети optimism, bsc и arbitrum в кошелек. 

1. экспортируй ids из adspower со своих профилей.
2. добавляешь эти ids в файл id_users.txt
3. добавляешь сид фразы от заранее созданных кошельков в файл seeds.txt
4. меняешь в файле main.py переменную password
5. запускаешь файл main.py

не забудь заранее войти в свой adspower, скрипт работает именно через него. 

библиотеки для скачивания : 
pip install selenium, requests, pyperclip, termcolor
