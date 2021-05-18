def standup_timer(token, channel_id):

    """
    Function is called a during threading,timer, where the time is given as length (x seconds standup period). At the end of length seconds, function will check the 
    biffered list of standup_send messages and packed them into one message. Then the message will be sent via the user in the specified channel_id
    Other features of this function included clearing the ative standup list and removing buffered messages (that were already sent into a packaged message)

    Parameters:
        token (str) : token of the user that has called the standup
        channel_id (int) : the channel_id the packaged message will be sent to

    Returns:
        None
    """
        
    from src.message import message_send_v2
    if "standup_buffer" in data and f"channel {channel_id}" in data["standup_buffer"]:
        size = len(data["standup_buffer"][f"channel {channel_id}"])
        packaged_message = ''
        
        for msg in data["standup_buffer"][f"channel {channel_id}"]:
            if msg == data["standup_buffer"][f"channel {channel_id}"][size-1]:
                packaged_message  = packaged_message  + msg
            else:
                packaged_message  = packaged_message + msg + '\n' 
        del data["standup_buffer"][f"channel {channel_id}"]  
        message_send_v2(token, channel_id, packaged_message)       
    
    if data.get("active_standups") != None:
        for i in data["active_standups"]:
            if i["channel_id"] == channel_id:
                data["active_standups"].remove(i)   