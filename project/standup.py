from src.data import getData 
from src.error import AccessError, InputError
from src.message import message_send_v2   
from src.helper import check_valid_info, check_members, find_user_id, get_timestamp, check_membership, check_msg_in, check_react, remove_react, react_check, standup_timer
import datetime
from datetime import datetime, timezone
from datetime import timedelta 
import threading
from threading import Timer
import time

def standup_start_v1(token, channel_id, length):
    """
    A user starts the startup period which lasts for the next length seconds. If any startup_send messages are sent during this perios, those messages which 
    have been buffered are packaged into one messaged and outputted by the user whomst has called trhe standup_start function

    Parameters: 
        token(str): the user's token
        channel_id(int): the channel's id
        length(int) : the X second period for which the standup lasts
    Returns: 
       dict containing time_finish key (integer value): returns a dict with a key 'time_finish' with value integer which is the unix timestamp 
    """

    data = getData()
    auth_user_id = find_user_id(token)
    if auth_user_id == False:
        raise AccessError(description = 'User is not a registered user')
    
    timestamp_finish = int(((datetime.now()) + timedelta(seconds=length)).replace(tzinfo=timezone.utc).timestamp())    
    
    #input error if channel id not a valid channel 
    channel_found = False
    if bool(data["channels"]): 
        for channel in data["channels"]:
            if channel["channel_id"] == channel_id:
                channel_found = True
    
    if channel_found == False:
        raise InputError(description = 'Channel ID is not a valid channel')
        
    #access error if auth_user is not in the channel
    user_found = False
    for memb in data["channels"][channel_id - 1]['all_members']:
        if memb["u_id"] == auth_user_id:
            user_found = True
    
    if user_found == False:
        raise AccessError(description = 'Authorised user is not in the channel')
    
    #input error when an active standup is already running in this channel
    
    if data.get("active_standups") != None: 
        for i in data["active_standups"]:
            if i["channel_id"] == channel_id:
                raise InputError(description = 'Active standup already running in this channel')  
    
   
    if data.get("active_standups") == None:
        data["active_standups"] = []
    

    info_dict = {'channel_id': channel_id,
                 'time_finish': timestamp_finish  
                 }  
                 
    data["active_standups"].append(info_dict)
    
    timestamp_finish = int(((datetime.now()) + timedelta(seconds=length)).replace(tzinfo=timezone.utc).timestamp())    

    t = threading.Timer(length, standup_timer, [token,channel_id])
    t.start()   
    
    return {'time_finish': timestamp_finish}

def standup_active_v1(token, channel_id):
    """
    For a given channel which the user is a part of, return whether or not there is an active standup running

    Parameters: 
        token(str): the user's token
        channel_id(int): the channel_id that is being checked for an active standup
    Returns: 
        dict with keys is_active (boolean), time_finish (int):
            -is_active: True or False based on whether or not there is a standup active
            -time_finish: If no standup running, key value would be None, else returns the unix timestamp of when the standup finishes
    """
    
    data = getData()
    auth_user_id = find_user_id(token)

    if auth_user_id == False:
        raise AccessError(description = 'User is not a registered user')

    channel_id = int(channel_id)
    #input error if channel id not a valid channel 
    channel_found = False

    if data.get("channels") != None: 
        for channel in data["channels"]:
            if channel["channel_id"] == channel_id:
                channel_found = True

    if channel_found == False:
        raise InputError(description = 'Channel ID is not a valid channel')
        
    #assumes that only a user in the channel can check if a standup is running 
    user_found = False
    for memb in data["channels"][channel_id - 1]['all_members']:
        if memb["u_id"] == auth_user_id:
            user_found = True
    
    if user_found == False:
        raise AccessError(description = 'User not in channel')
            
    time_finish = None
    is_active = False
    
    if data.get("active_standups") == None:
        time_finish = None
        is_active = False
        
    else:
        for i in data["active_standups"]:
            if i["channel_id"] == channel_id:
                time_finish = i["time_finish"]
                is_active = True
                           
    return {'is_active': is_active,
            'time_finish': time_finish
            }   


def standup_send_v1(token, channel_id, message):
    
    """
    Sending a message to get buffered in the standup queue, assuming a standup is currently active

    Parameters: 
        token(str): the user's token
        channel_id(int): the channel id
        message(str): the message being sent by user 
    
    Returns: 
        {} (dict): An empty dictionary 
    """
    
    data = getData()
    auth_user_id = find_user_id(token)
    if auth_user_id == False:
        raise AccessError(description = 'User is not a registered user')

    handle = data["users"][auth_user_id - 1]["handle_str"]
    
    final_message = handle + ': ' + '' + message
    
    #input error for invalid channel 
    if data.get("channels") == None:
        raise InputError(description = 'Channel ID is not a valid channel')
    
    chan_found = False
    
    for channel in data["channels"]:
        if channel["channel_id"] == channel_id:
            chan_found = True
    
    if chan_found == False:
        raise InputError(description = 'Channel ID is not a valid channel')
        
    
    #access error if user is not in channel 
    user_found = False
    for memb in data["channels"][channel_id - 1]['all_members']:
        if memb["u_id"] == auth_user_id:
            user_found = True
    
    if user_found == False:
        raise AccessError(description ='Authorised user is not in the channel')
    
    #input error if message character_count > 1000
    
    if len(message) > 1000:
        raise InputError(description = 'Message is over 1000 characters long')
        
    
    #input error if an active standup is not currently running in this channel  
    active_running = False
    if data.get("active_standups") == None:
        raise InputError(description = 'An active standup is not currently running in this channel')
    else:
        for i in data["active_standups"]:
            if i["channel_id"] == channel_id:
                active_running = True
            
    if active_running == False:
        raise InputError(description = 'An active standup is not currently running in this channel')
         
    #The way the buffering works:
    #Creates a buffering dict, which contains dicts of channels and their corresponding messages as in those specific channels being buffered 
          
    if data.get("standup_buffer") == None:
        data["standup_buffer"] = {}


    if data["standup_buffer"].get(f"channel {channel_id}") == None:
        data["standup_buffer"][f"channel {channel_id}"] = []  
        
    if f"channel {channel_id}" in data["standup_buffer"]:
        data["standup_buffer"][f"channel {channel_id}"].append(final_message)       
    
    return { }
