def review_chan(app, db, answer, line_list):
    chan_str = ""
    #Перечислить каналы этой ленты
    for chan_id_list in line_list:
        name = (app.get_chat(chan_id_list)).title
        chan_str = chan_str+chan_id_list+' - '+name+'\n'
    return chan_str

def review_line(db, answer):
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
    
def review_all(app, db, answer):
    chan_str = ""
    #перечислить ленты и их подписки
    for chan_list in db.values():
        state    = '✅' if chan_list.settings['state']   else '❎'
        text     = '✅' if chan_list.settings['text']    else '❎'
        stick    = '✅' if chan_list.settings['sticker'] else '❎'
        ad_filt  = '✅' if chan_list.settings['filter']  else '❎'
        chan_str = (chan_str+
                    '>>>>>>>>>>>>>>>>>\n'+
                    chan_list.id+' - '+chan_list.name+' - '+
                    'St:'+state+'Txt:'+text+
                    'Stk:'+stick+'adB:'+ad_filt+'\n'+
                    'Subscriptions:\n'+review_chan(app, db, answer, chan_list.chan_list)+
                    'Banned:\n'+review_chan(app, db, answer, chan_list.ban_list))
    
    return chan_str