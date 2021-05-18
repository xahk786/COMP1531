def notifications_get_v1(token):
    """
    Returns the users most recent 20 notifications 

    Arguments:
        token (str) - the user's token
    
    Exceptions:
        N/A
    
    Return Value:
        notifications (list of dict) - each dictionary contains: 
            - channel_id, 
            - dm_id, 
            - notification_message
    """
    data = getData()
    user_valid = False
    adder = False
    joiner = False
    auth_user_id = find_user_id(token)
    # If token is invalid raise an Accesserror
    user_valid = check_valid_info(data["users"], auth_user_id)

    if user_valid == False:
        raise AccessError('User is not a registered user')

    user_handle = data["users"][auth_user_id - 1]["handle_str"]
    mentioned_handle = "@" + user_handle
    notifications = []
    
    
    if "channels" in data:
        for channel in data["channels"]:
            for membs in channel['all_members']:
                if auth_user_id == membs["u_id"] and auth_user_id != channel["creator"]:
                    #need to find out the adder of the token user
                    for reg in data["added_info"]["channels"]:
                        if reg["u_id"] == auth_user_id and reg["channel_id"] == channel["channel_id"]:
                            if reg.get('adder'):
                                adder_handle = reg["adder"]
                                adder = True
                            if reg.get('joiner'):
                                joiner_handle = reg['joiner']
                                joiner = True
                                
                    if adder:        
                        channel_name = channel["name"] 
                        
                        notification_added_channel = {"channel_id": channel["channel_id"],
                                                    "dm_id": -1,
                                                    "notification_message": f"{adder_handle} added you to {channel_name}"   
                                                    }  
                        notifications.append(notification_added_channel)  
                    if joiner:
                        channel_name = channel["name"] 
                    
                        notification_added_channel = {"channel_id": channel["channel_id"],
                                                    "dm_id": -1,
                                                    "notification_message": f"{joiner_handle} joined {channel_name}"   
                                                    }  
                        notifications.append(notification_added_channel)  
       
        
    if "dm" in data:
        for dm in data["dm"]:
            for membs in dm['all_members']:
                if auth_user_id == membs["u_id"] and auth_user_id != dm["creator"]:        
                    #need to find the adder of the token user
                    for reg in data["added_info"]["dms"]:
                        if reg["u_id"] == auth_user_id and reg["dm_id"] == dm["dm_id"]:
                            adder_handle = reg["adder"]
                                        
                    dm_name = dm["dm_name"]
                    
                    notification_added_dm = {"channel_id": -1,
                                             "dm_id": dm["dm_id"],
                                             "notification_message": f"{adder_handle} added you to {dm_name}"   
                                            }  
                    notifications.append(notification_added_dm)


    if "messages" in data:
        for msg in data["messages"]:
            #check every single message output and check if user was @userhandle was mentioned in any of those messages 
            if mentioned_handle in msg["message"]:
                if "dm_id" in msg:                                
                    dm_name = data["dm"][msg["dm_id"] - 1]["dm_name"]
                    sender_handle = data["users"][msg["sender"] - 1]["handle_str"]            
                    message = msg["message"]

                    notification_mentioned = {"channel_id": -1,
                                              "dm_id": msg["dm_id"],
                                              "notification_message": f"{sender_handle} tagged you in {dm_name} : {message[0:20]}"   
                                             }  
                    notifications.append(notification_mentioned)
                
                if "channel_id" in msg:
                    channel_name = data["channels"][msg["channel_id"] - 1]["name"]
                    sender_handle = data["users"][msg["sender"] - 1]["handle_str"] 
                    message = msg["message"]
                   
                    notification_mentioned = {"channel_id": msg["channel_id"],
                                              "dm_id": -1,
                                              "notification_message": f"{sender_handle} tagged you in {channel_name} : {message[0:20]}"   
                                             }
                    notifications.append(notification_mentioned)
            #check every single message output ahd check if there are reacts in that message
            #for msg in data["messages"]:
            if bool(msg["reacts"]) and msg["sender"] == auth_user_id: 
                #for reg_react in msg["reacts"]:
                    #if auth_user_id not in reg_react["u_ids"]:
                    #so far we have checked that IF there are reacts in a message
                if "dm_id" in msg: 
                    for reg in data["added_info"]["reacts"]:
                        #if someone has reacted to the user token
                        if reg["u_id"] == auth_user_id:
                            reactor_handle = reg["reactor"]
                            platform_name = reg["platform_name"]
                            notification_reacted = {"channel_id": -1,
                                                    "dm_id": msg["dm_id"],
                                                    "notification_message": f"{reactor_handle} reacted to your message in {platform_name}"   
                                                   }
                            notifications.append(notification_reacted)
                    
                if "channel_id" in msg:  
                    for reg in data["added_info"]["reacts"]:
                        if reg["u_id"] == auth_user_id:
                            #reacted message: "{User?s handle} reacted to your message in {channel/DM name}"
                            reactor_handle = reg["reactor"]
                            platform_name = reg["platform_name"]
                            notification_reacted = {"channel_id": msg["channel_id"],
                                                    "dm_id": -1,
                                                    "notification_message": f"{reactor_handle} reacted to your message in {platform_name}"   
                                                   }
                            notifications.append(notification_reacted)

    notifications.reverse()
    
    final_output = []
    index = 0
    
    if len(notifications) <= 20:
        final_output = notifications
    else: #length would be >20 so need to output only first 20
        while index < 20:
            final_output.append(notifications[index])
            index += 1
        

    return { "notifications" : final_output
    }