command = {
    'del'    : ('!delete', '!del'),
    'list'   : '!list',
    'chan'   : ('channels', 'channel', 'chan', 'chans'),
    'line'   : ('lines', 'line'),
    'baned'  : ('bans', 'banned'),
    'all'    : 'all',
    'debug'  : '!debug',
    'help'   : '!help',
    'ban'    : ('!ban', '!block'),
    'unban'  : ('!unban', '!unblock'),
    'config': 'config',
    'state'  : 'state',
    'text'   : 'text',
    'sticker': 'sticker',
    'filter' : 'filter',
    }

answer={
    'unexp'  : "Некая непредвиденная ситуация.",
    'setting_r': "Состояние настройки %s изменено на %s",
    'chan'   : "Канал %s, c ID %s, ",
    'ban_r'  : "Канал %s, c ID %s, заблокирован в ленте %s.",
    'unban_r': "Канал %s, c ID %s, разблокирован в ленте %s.",
    'del_r'  : "Канал %s, c ID %s, удален из ленты %s.",
    'failed'  :"Ошибка выполнения операции %s.",
    'delline_r':"Лента успешно удалена.",
    'l_line_r':"Ваши ленты: \n",
    'l_subs_r':"Каналы в ленте:\n",
    'l_ban_r': "Заблокированные каналы:\n",
    'adl_r'  : "добавлен как лента.",
    'adl_e'  : "уже является лентой.",
    'adc_e'  : "уже есть в базе.",
    'add_ch' : " добавлен в ленту %s.",
    'helptxt': '''__Чтобы сделать канал лентой:__
**"%s"**
__Чтобы удалить ленту:__
**"%s"**
**Переслать сообщение из канала**__ - чтобы добавить канал в БД__
**!delete channel**__ - удалить канал из БД__ 
**!ban channel**__ - заблокировать канал__
**!unban channel**__ - разблокировать канал__
**!list channels**__ - список каналов в ленте__ 
**!list banned**__ - список заблокированных каналов в ленте__ 
**!list lines** __- список своих лент__ 
**!list all** __- вся база каналов__
**!help**__ - вызов справки__ 
''',}