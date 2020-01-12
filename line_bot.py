from pyrogram   import Client, MessageHandler, Filters
from config     import apiId, apiHash, confline
from words      import words
import shelve

class Line:
    def __init__(self, id, name, chlist=[], cond=True):
        self.id     = id
        self.name   = name
        self.cond   = cond
        self.chlist = chlist

with shelve.open('lineDB') as db:
    app = Client("user", apiId, apiHash)

    @app.on_message(Filters.channel)
    def lineBot(Client, message):
        msg_txt      = str(message.text)
        msg_txt_sm   = msg_txt.lower()
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
            txt = words["chan"] %(chan_name, chan_id)
            for id in db.keys():
                a.append(id)  
            if chan_id in a:
                txt = txt+words['adl_e']
            else:
                line        = Line(chan_id, chan_name, chlist=[])
                db[chan_id] = line
                txt = txt+words['adl_r']
                
            app.send_message(chan_id, txt, reply_to_message_id=msg_id) 

            
        else:
            for line in db.values():
                if chan_id == line.id:
                    txt = words["chan"] %(str(chan_name_fwd), str(chan_id_fwd))

                    if chan_id_fwd and chan_id_fwd not in line.chlist:
                        #Добавление канала в БД по пересланному оттуда посту
                        line.chlist.append(str(chan_id_fwd))

                        txt = txt+words['add_ch'] % (chan_name)

                    elif msg_txt_sm in words['del']:
                        #Удаление канала из БД по реплаю на пересланное сообщение
                        try:
                            chan_rpl_fwd = message.reply_to_message.forward_from_chat
                            line.chlist.remove(str(chan_rpl_fwd.id))            
                            txt = words['del_r'] %(str(chan_rpl_fwd.title), str(chan_rpl_fwd.id), chan_name)
                        except:
                            print(message)
                            txt = words['del_e']
                    
                    elif msg_txt_sm in words['list_ch']:
                        #Перечислить каналы этой ленты
                        chan_str = ""
                        for chan_id_list in line.chlist:
                            name = (app.get_chat(chan_id_list)).title
                            chan_str = chan_str+chan_id_list+' - '+name+'\n'

                        txt = words['list_r']+chan_str

                    elif msg_txt_sm in words['list_ln']:
                        #Перечислить свои ленты 
                        chan_str = ""
                        for chan_list in db.values():
                            cond = '✅' if chan_list.cond else '❎'
                            chan_str = (chan_str+
                                        chan_list.id+' - '+
                                        chan_list.name+' - '+
                                        cond+'\n')

                        txt = words['list_l']+chan_str
                    
                    elif msg_txt_sm in words['debug']:
                        txt = ('ID: '+db[line.id].id+'\n'+
                               'Name: '+db[line.id].name+'\n'+
                               'Channels: '+str(db[line.id].chlist))
                               
                    elif msg_txt_sm in words['help']:
                        txt = words['helptxt'] % (confline['addline'], confline['delline'])
                    
                    elif words['cond'] in msg_txt_sm:
                        if 'off' in msg_txt_sm : line.cond = False
                        elif 'on' in msg_txt_sm: line.cond = True

                        cond = '✅' if line.cond else '❎'
                        txt = words['cond_r'] % cond

                    elif msg_txt_sm in confline['delline']:
                        line.id = ''
                        line.name = ''
                        line.chlist = []
                        txt = words['delline_r']

                    else:
                        txt = words['unexp']
                        print(message)
                    
                    db[line.id] = line
                    app.send_message(chan_id, txt, reply_to_message_id=msg_id) 

                elif line.cond and chan_id in line.chlist:
                    #Пересылка сообщений из каналов в ленту
                    app.forward_messages(line.id, chan_id, msg_id) 
                
    app.run()