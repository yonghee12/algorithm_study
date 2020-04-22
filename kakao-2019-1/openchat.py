def solution(record):
  answer = []
  
  def preprocessing(record):
    messages = []
    users = {}
    for line in record:
      splitted = line.split(" ")
      command = splitted[0]
      if command == 'Enter':
        user_id, user_name = splitted[1], splitted[2]
        users[user_id] = user_name
        messages.append((command, user_id))
      elif command == "Leave":
        user_id = splitted[1]
        messages.append((command, user_id))
      elif command == "Change":
        user_id, user_name = splitted[1], splitted[2]
        users[user_id] = user_name
      else:
        return 'ERROR'
    return messages, users
  
  def message_processing(line):
    command, user_id = line[0], line[1]
    user_name = users[user_id]
    if command == "Enter":
      return "{}님이 들어왔습니다.".format(user_name)
    elif command == "Leave":
      return "{}님이 나갔습니다.".format(user_name)
    else:
      return "ERROR"

  messages, users = preprocessing(record)
  # print(messages, "\n", users)

  for line in messages:
    answer.append(message_processing(line))
    
  return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record))