import shelve

class LineOld:
    def __init__(self, id, name, chan_list=[], ban_list=[], 
    settings={
        'state'  : True,
        'text'   : True,
        'sticker': False,
        'filter' : False}):
        self.id     = id
        self.name   = name
        self.chan_list = chan_list
        self.ban_list  = ban_list
        self.settings  = settings

class Line:
    def __init__(self, id, name, chan_list=[], ban_list=[], 
    settings={
        'state'  : True,
        'text'   : True,
        'sticker': False,
        'copy'   : False,
        'filter' : False}):
        self.id     = id
        self.name   = name
        self.chan_list = chan_list
        self.ban_list  = ban_list
        self.settings  = settings

with shelve.open('lineDBold') as oldDB:
    with shelve.open('lineDB') as newDB:
        for x, y in oldDB.items():
            print('O - Key ID:', x, 'Value ID: ', y.id)
            print('O - Title: ', y.name)
            print('O - Channels: ', y.chan_list)
            print('O - Banned: ', y.ban_list)
            print('O - Settings: State: ',      y.settings['state'], 
                                 'Text: ',      y.settings['text'],
                                 'Stickers: ',  y.settings['sticker'],
                                 'Filtration: ',y.settings['filter'],)
            print('---------------------------')

        for x, y in oldDB.items():
            new_obj = Line( id          = y.id, 
                            name        = y.name, 
                            chan_list   = y.chan_list,
                            ban_list    = y.ban_list,
                            settings    = {
                                            'state'  : True,
                                            'text'   : True,
                                            'sticker': False,
                                            'copy'   : False,
                                            'filter' : False
                                            })
            new_obj.settings['state']   = y.settings['state']
            new_obj.settings['text']    = y.settings['text']
            new_obj.settings['sticker'] = y.settings['sticker']
            new_obj.settings['filter']  = y.settings['filter']
            newDB[x] = new_obj
        
        for x, y in newDB.items():
            print('N - Key ID:', x, 'Value ID: ', y.id)
            print('N - Title: ', y.name)
            print('N - Channels: ', y.chan_list)
            print('N - Banned: ', y.ban_list)
            print('N - Settings: State: ',      y.settings['state'], 
                                 'Text: ',      y.settings['text'],
                                 'Stickers: ',  y.settings['sticker'],
                                 'Copy: ',      y.settings['copy'],
                                 'Filtration: ',y.settings['filter'],)
            print('---------------------------')