def settings(line, setting, cond):
    if 'state'    in setting:
        if  'off' in cond: line.settings['state']   = False
        elif 'on' in cond: line.settings['state']   = True
    elif 'text'   in setting:
        if  'off' in cond: line.settings['text']    = False
        elif 'on' in cond: line.settings['text']    = True
    elif 'sticker'in setting:
        if  'off' in cond: line.settings['sticker'] = False
        elif 'on' in cond: line.settings['sticker'] = True
    elif 'filter' in setting:
        if  'off' in cond: line.settings['filter'] = False
        elif 'on' in cond: line.settings['filter'] = True
    if  'off' in cond: 
        cond = '❎'
    elif 'on' in cond: 
        cond = '✅'
        
    return cond