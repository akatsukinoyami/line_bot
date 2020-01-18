from time import sleep

def iter_chan(app, chan_list):
    chan_str = ""
    for chan_id_list in chan_list:
        name = (app.get_chat(chan_id_list)).title
        chan_str = chan_str+chan_id_list+' - '+name+'\n'
        sleep(.1)
    return chan_str

def review_chan(app, line):
    state    = '✅' if line.settings['state']   else '❎'
    text     = '✅' if line.settings['text']    else '❎'
    stick    = '✅' if line.settings['sticker'] else '❎'
    ad_filt  = '✅' if line.settings['filter']  else '❎'
    chan_str = (line.id+' - '+line.name+' - '+
                'St:'+state+'Txt:'+text+
                'Stk:'+stick+'adB:'+ad_filt+'\n'+                    
                'Subscriptions:\n'+iter_chan(app, line.chan_list)+
                'Banned:\n'+iter_chan(app, line.ban_list))
    return chan_str

def review_line(db):
    chan_str = ""
    #Перечислить свои ленты 
    for chan_list in db.values():
        state    = '✅' if chan_list.settings['state']   else '❎'
        text     = '✅' if chan_list.settings['text']    else '❎'
        stick    = '✅' if chan_list.settings['sticker'] else '❎'
        ad_filt  = '✅' if chan_list.settings['filter']  else '❎'
        chan_str = (chan_str+
                    chan_list.id+' - '+chan_list.name+' - '+
                    'St:'+state+'Txt:'+text+
                    'Stk:'+stick+'adB:'+ad_filt+'\n')
    return chan_str
    
def review_all(app, db):
    chan_str = ""
    #перечислить ленты и их подписки
    for line_in_db in db.values():
        chan_str = (chan_str+'\n>>>>>>>>>>>>>>>>>\n'+review_chan(app, line_in_db))
        sleep(.3)
    return chan_str