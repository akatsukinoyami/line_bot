from pyrogram       import Client, MessageHandler, Filters, InputMediaPhoto, InputMediaVideo
from config         import apiId, apiHash, confline
from funcs.send     import send
from funcs.review   import review_chan, review_line, review_all
from funcs.words    import command, answer
from funcs.settings import settings
import shelve

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



with shelve.open('lineDB') as db:
    app = Client("user", apiId, apiHash)

    @app.on_message(Filters.channel & ~Filters.edited)
    def lineBot(Client, message):
        spam_chan    = '-1001368942367'
        msg_txt      = str(message.text)
        msg_txt_sm   = msg_txt.lower()
        msg_txt_sm_split = msg_txt_sm.split()
        msg_id       = message.message_id
        chan_id      = str(message.chat.id)
        chan_name    = message.chat.title
        try:          
            chan_fwd      = message.forward_from_chat
            chan_id_fwd   = chan_fwd.id
            chan_name_fwd = chan_fwd.title
        except:       
            chan_id_fwd   = None
            chan_name_fwd = None

        if msg_txt_sm == confline['addline']:
            #Создание ленты
            a = []
            txt = answer["chan"] %(chan_name, chan_id)
            for id in db.keys(): a.append(id)  
            if chan_id in a:     txt = txt+answer['adl_e']
            else:
                line        = Line(chan_id, chan_name)
                db[chan_id] = line
                txt = txt+answer['adl_r']
            app.send_message(chan_id, txt, reply_to_message_id=msg_id)
     
        else:
            for line in db.values():
                if (line.settings['state'] and 
                    chan_id in line.chan_list and
                    chan_id not in line.ban_list):

                    send(app, message, msg_id, line, spam_chan)

                elif chan_id == line.id:

                    txt = answer["chan"] %(str(chan_name_fwd), str(chan_id_fwd))

                    if chan_id_fwd and str(chan_id_fwd) not in line.chan_list:
                    #Добавление канала в БД по пересланному оттуда посту 
                        print('Канал добавлен в БД.') 
                        line.chan_list.append(str(chan_id_fwd))
                        txt = txt+answer['add_ch'] % (chan_name)
                    
                    elif '!' in msg_txt_sm_split[0]:
                        if '!config' in msg_txt_sm_split[0]:
                            cond = settings(line, msg_txt_sm_split[1], msg_txt_sm_split[2])
                            txt = answer['setting_r'] % (msg_txt_sm_split[1], cond)

                        elif command['list'] in msg_txt_sm_split[0]:
                            app.edit_message_text(chan_id, msg_id, 'Подготавливаю сводку.')
                            #Просмотр списка подписок
                            if   msg_txt_sm_split[1] in command['chan']: txt = answer['l_subs_r']+review_chan(app, line)
                            #Просмотр списка лент
                            elif msg_txt_sm_split[1] in command['line']: txt = answer['l_line_r']+review_line(db)
                            #Просмотр всей БД
                            elif msg_txt_sm_split[1] in command['all'] : txt = review_all(app, db)

                        elif command['debug'] in msg_txt_sm_split[0]:
                            txt = ('ID: '+db[line.id].id+'\n'+
                                'Name: '+db[line.id].name+'\n'+
                                'Channels: '+str(db[line.id].chan_list))
                                
                        elif command['help']in msg_txt_sm_split[0]:
                            txt = answer['helptxt'] % (confline['addline'], confline['delline'])

                        elif msg_txt_sm in confline['delline']:
                            old_id = line.id
                            line.id = ''
                            line.name = ''
                            line.chan_list = []
                            line.ban_list = []
                            db[old_id] = line
                            txt = answer['delline_r']
                        else:
                            try:
                                chan_rpl_fwd = message.reply_to_message.forward_from_chat
                                
                                if   msg_txt_sm_split[0] in command['ban']: 
                                #Запрет на форвард сообщений из канала по реплаю на пересланное сообщение
                                    line.ban_list.append(str(chan_rpl_fwd.id))
                                    txt = answer['ban_r'] %(str(chan_rpl_fwd.title), str(chan_rpl_fwd.id), chan_name)
                                    
                                elif msg_txt_sm_split[0] in command['unban']: 
                                #Снятие запрета на форвард сообщений из канала по реплаю на пересланное сообщение  
                                    line.ban_list.remove(str(chan_rpl_fwd.id))
                                    txt = answer['unban_r'] %(str(chan_rpl_fwd.title), str(chan_rpl_fwd.id), chan_name)
                                    
                                elif msg_txt_sm_split[0] in command['del']:
                                #Удаление канала из БД по реплаю на пересланное сообщение
                                    line.chan_list.remove(str(chan_rpl_fwd.id)) 
                                    txt = answer['del_r'] %(str(chan_rpl_fwd.title), str(chan_rpl_fwd.id), chan_name)
                            except:
                                print(message) 
                                break 

                    try:
                        app.edit_message_text(chan_id, msg_id, txt)
                    except:
                        app.send_message(chan_id, txt)  
                    db[line.id] = line
                    
    app.run()