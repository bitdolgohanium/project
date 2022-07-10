################################################
# 0. imported library and global value
# 1. main function
# 2. process_level1_arragne_algorithm
# 3. process_level2_led_manipulation
# 4. process_level2_motor_manipulation
# 5. process_level0_camera
# 6. enroll 
# 7. allocate_parkinglot
# 8. LED_code_run
# 9. Motor_code_run_set
# 10. Motor_code_run_reset
# 11. camera_code_run
# 12. init (initial setting)
# 13. store_db
#     main()
#     should fix list & change log
################################################

#   <0. imported library and global value>
#
import time
from multiprocessing import Process

#   <1. main function>
#   
def main():
    init()
    while (1): #main function (loop)
        if (full == 1):
            print("system : parking lot full") 
        else:
            car_info = enroll(); # 1. # get car_num, time_out and give inner_num
            car_info.inner_num = ++count_car 
            car_info.car_arrange = 0
            process_level1_arragne_algorithm(car_info)     

#   <2. process_level1_arragne_algorithm>
#   process that allocates each car parking lot 
def process_level1_arragne_algorithm(car_info):
    car_info.car_arrange = allocate_parkinglot(car_info)
    store_db(car_info)
    process_level0_camera()
    process_level2_led_manipulation(car_info)
    process_level2_motor_manipulation(car_info)


#   <3. process_level2_led_manipulation>
#   make LED system run   
def process_level2_led_manipulation(car_info):
    proc = Process(target=LED_code_run, args=(car_info)) 
    procs.append(proc)
    proc.start()

#   <4. process_level2_motor_manipulation>
#   make motor system run 
def process_level2_motor_manipulation(car_info):
    proc = Process(target=Motor_code_run_set, args=(car_info)) 
    procs.append(proc)
    proc.start()

#   <5. process_level0_camera>
#   make camera run dependetly
def process_level0_camera(car_info):
    proc = Process(target=camera_code_run, args=()) 
    procs.append(proc)
    proc.start()

#   <6. enroll>
#
def enroll():
    print("f>> get car_info.car_num and return")
    print("f>> get car_info.time_out and return")
    return car_info

#   <7. allocate_parkinglot>
#
def allocate_parkinglot(car_info):
    print("f>> allocate car, refer car_info return car_arrange")
    return car_arrange

#   <8. LED_code_run>
#
def LED_code_run(car_info):
    print("f>> run LEDprogram") 

#   <9. Motor_code_run_set>
#
def Motor_code_run_set(car_info):
    print("f>> run Motor_setprogram") 

#   <10. Motor_code_run_reset>
#
def Motor_code_run_reset():
    print("f>> run Motor_resetprogram") 

#   <11. camera_code_run>
#
def camera_code_run():
    print("f>> run Cameraprogram, return : done") 
    if (done == 1):
        Motor_code_run_reset()
        proc.join()

#   <12. init>
#
def init():
    count_car = 0 #when program starts sumnum reset
    procs = [] #make space for new processes 
    full = 0

#   <13. store_db>
#
def store_db():
    print("f>> store_db") 


#   <   main()>
#
if __name__ == '__main__':
    main()

#//////////////////////////////////////////////////////need to fix
# 1. car_info에 car_num과 time_out을 담고 싶다.
# . excl() 공부해서 각자 프로세스 돌릴 준비해야함
# . done 시그널 받으면 프로세스 모두 종료해야함  
# . 차마다 car_info를 따로 해줘야함 
# . 차마다의 proc를 분리해주어야 한번에 안꺼질 것 같음

#//////////////////////////////////////////////////////change log 
# .
# .