def message_senddm_v1(token, dm_id, message):
    """
    Send a message from authorised_user to the DM specified by dm_id.
    Note: Each message should have it's own unique ID.
    I.E. No messages should share an ID with another message,
    even if that other message is in a different channel or DM.
    
    Arguments:
        token (str) - the user's token
        dm_id (int) - the dm's id
        message (str) - the message being sent
    
    Exceptions:
        InputError - Message is more than 1000 characters
        AccessError - the authorised user is not a member of the DM they are trying to post to
    
    Return Value:
        message_id (int) - the message's id
    """
    data = getData()
    
    user_valid = False
    auth_user_id = find_user_id(token)
    # If token is invalid raise an Accesserror
    user_valid = check_valid_info(data["users"], auth_user_id)

    if user_valid == False:
        raise AccessError(description = 'User is not a registered user')

    membs_list = []
    for membs in data["dm"][dm_id - 1]['all_members']:
        membs_list.append(membs["u_id"])
 
    if auth_user_id not in membs_list:
        raise AccessError(description = "Authorised user is not a member of the DM they are trying to post to") 
        
            
    if data.get('messages') == None:
        data['messages'] = []

    
    #raise input error 
    if len(message) > 1000:
        raise InputError(description= "Message is more than 1000 characters")
       
    message_id = len(data["messages"]) + 1

 
    for msg in data["messages"]:
        if "dm_message_index" in msg:
            msg["dm_message_index"] += 1
    
    time_created = get_timestamp()
    
    new_message_reg = { "message": message,
                        'message_id': len(data['messages']) + 1,
                        'reacts' : [],
                        "sender": auth_user_id,
                        'dm_id': dm_id,
                        'message_index': len(data['messages']) + 1,
                        "dm_message_index": 0,
                        'time_created' : time_created,  
                        'is_pinned': False,
                        }

    data["messages"].append(new_message_reg)
    
    return {
            'message_id': message_id,
    }