################################
# 1. car_entered
# 2. car_count
# 3. enter_ui
# 4. save_db
# 5. car_arr
# 6. manipulating_p
# 7. cam_p
# 8. led_p
# 9. motor_p
# 10. erase_p0
# 11. erase_p1
################################

import multiprocessing
import os

# 1. car_entered
def car_entered(car_info, car_count_val):
  if (1): # 1. UI에서 입차신호를 받음
    if (car_count_val < 32): # 2. 주차장이 찼는지 확인
     car_count_val = car_count(car_count_val) # 주차장 내 차량 카운트
     save_db(car_info) # 3. db에 저장
     car_info = car_arr(car_info) # 4. 주차장에 배정 (위치 .arr으로 반환)
     manip_p_id = manipulating_p(car_info) # 5. mani_p 실행 나머지는 mani_p에서 이어짐 # 상위 프로세스에서 종료위해 반환
     erase_p1(manip_p_id) # 11. mani_p를 다 지운다.
    else: print("parkinglot full") # 주차장이 꽉찬 경우
  else: print("error, input doesnt comes from ") # 입차신호를 받지 않을시

# 2. car_count
def car_count(car_count_val):
  car_count_val = ++car_count_val
  print("car counted")

# 3. enter_ui
def enter_ui(): #UI에서 data를 받아옴
  return 0 ## UI에서 어떤값 반환 (INT 3)

# 4. save_db
def save_db(car_info):
  print("info saved")

# 5. car_arr
def car_arr(car_info):
  print("allocate car to empty lot")
  return car_info

# 6. manipulating_p
def manipulating_p(car_info):
  print("manipulating process made")
  cam_p() # 6. 캠돌아가기 시작함. 주차상태 확인 끝나면 1반환
  led_p(car_info) # 7. led 밝혀줌
  motor_p(car_info) # 8. 모터 구동시킴
  p_id = os.getpid() # 현재 프로세스 id반환함 상위프로세스에서 지우기위해
  while (1):
    if (cam_p() == 1):
      erase_p0() # 9. 주차가 완료되면 제일 아래쪽 프로세스 모두 종료
      break
    else:
      print("waiting...")
  return p_id

# 7. cam_p
def cam_p(): #cam_p를 실행시키기 위한 함수를 포함함
  print("cam_p process made")
  return 1

# 8. led_p
def led_p(car_info): #led_p를 실행시키기 위한 함수를 포함함 #위치 받아야함
  print("led_p process made")

# 9. motor_p
def motor_p(car_info): #motor_p를 실행시키기 위한 함수를 포함함 #위치 받아야함
  print("motor_p process made")

# 10. erase_p0
def erase_p0():
  print("exit all process in manipulating_p")

# 11. erase_p1
def erase_p1(manip_p_id):
  os.kill(manip_p_id,)
  print("exit manipulating_p")

# main
def main():
  car_count_val = 0 #프로그램 시작시 개수는 0으로 초기화
#원랜 반복되게 짜야하지만 확인을 위해 루프깸@@@@
#  while(1): #프로그램이 실행된 이후 계속 반복
#    car_info = enter_ui() #UI에서 받은 값 car_info (INT 3)으로 저장
#    car_entered(car_info, car_count_val) #차량수 카운트와 인차차량 정보 입력
  car_info = enter_ui() #UI에서 받은 값 car_info (INT 3)으로 저장
  car_entered(car_info, car_count_val) #차량수 카운트와 인차차량 정보 입력


if __name__ == '__main__':
  main()

################################
# 1. 프로세스를 생성하고 실행할 수 있는 코드 추가
# 2. UI입력 추가
# 3. DB저장 추가

