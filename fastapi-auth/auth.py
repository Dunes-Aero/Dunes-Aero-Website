from db.crud import searchUser
def login(email,password):
    try:
        res = searchUser(email,password)
        if (res == None):
            return {'status':400, 'msg':'Invlaid email or password'}
        else:
            return {'status':200, 'data':res}
    except:
        return {'status':500, 'msg':'Invlaid email or password'}
    pass

