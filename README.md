# ⚡ 2ch.hk toolkit ⚡

Несколько скриптов для двощей.

## dvach_send_posts
API для постинга. Может работать в несколько потоков. Можно прикрепить картинку к посту.

### Установка

1. Зарегистрироваться на anti-captcha.com, закинуть немного шекелей
1. Установить пакет для работы с anticaptcha api ` pip3 install anticaptchaofficial `
1. Получить API-ключ и приступить к использованию 
1. ???
1. PROFFFFIT

### Использование
![1](/img/1.jpg)

```
atom = dvachdesc("ANTICAPTCHA KEY")
atom.send_post('b','225677863','test2')
```
## 2ch_download
Простой быстрый парсер медиа с тредов. Работает в несколько потоков. 
### Установка 

Не требуется.


### Использование
```
usage: 2ch_download.py [-h] -t THREAD [-p PATH] [--tdc TDC]

2ch_hk threads downloading tool

optional arguments:
  -h, --help  show this help message and exit
  -t THREAD   Thread's number
  -p PATH     Path for downloaded stuff
  --tdc TDC   Thread's division constant
```

