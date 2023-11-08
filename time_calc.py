def add_time(start_time, duration, start_day=None):
 
  days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  
  start_time = start_time.split()
  start_hour, start_minute = map(int, start_time[0].split(':'))
  start_period = start_time[1]

  duration = duration.split(':')
  duration_hour, duration_minute = int(duration[0]), int(duration[1])

  total_minutes = (start_hour % 12) * 60 + start_minute

  if start_period == 'PM':
      total_minutes += 12 * 60

  total_minutes += duration_hour * 60 + duration_minute


  days_passed = total_minutes // (24 * 60)
  remaining_minutes = total_minutes % (24 * 60)

  
  new_period = 'AM' if (remaining_minutes < 12 * 60) else 'PM'


  final_hour = (remaining_minutes // 60) % 12
  final_minute = remaining_minutes % 60

 
  if final_hour == 0:
      final_hour = 12

 
  if start_day is not None:
      start_day = start_day.capitalize()
      start_index = days_of_week.index(start_day)
      new_index = (start_index + days_passed) % 7
      new_day = days_of_week[new_index]
  else:
      new_day = None

  
  result = f"{final_hour}:{final_minute:02} {new_period}"

  if new_day:
      result += f", {new_day}"

  if days_passed == 1:
      result += " (next day)"
  elif days_passed > 1:
      result += f" ({days_passed} days later)"

  return result

