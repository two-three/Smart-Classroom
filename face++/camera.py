from calculate import *
import threading

def camera(cam_addr, outer_id):
    global flag
    sign = False
    while True:
        if flag == 0:
            cap.release()
            cv2.destroyAllWindows()
            i = 0
            while True:
                if flag == 1:
                    cap = cv2.VideoCapture(cam_addr)
                    break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ret, frame = cap.read()
        if ret == False:
            break

        if i >= 40:  # 25帧=1s 基础用时10s 每个功能平均5s
            savepath = "./data/cap.jpg"
            cv2.imwrite(savepath, frame)

            if sign == False:
                print("\n签到\n")
                is_signing(savepath, outer_id)
                sign = True

            print("\n抬头低头\n")
            is_pitch(savepath, outer_id)

            print("\n玩手机\n")
            is_playing_phone(savepath, outer_id)

            print("\n睡觉\n")
            is_sleeping(savepath, outer_id)

            print("\n发言\n")
            is_standing(savepath, outer_id)

            print('\n####################################################\n')
            i = 0
            os.remove(savepath)
        else:
            i += 1


#######################################################################


def listen():
    global flag
    while True:
        flag = int(input())


#######################################################################


def thread(cam_addr, outer_id):
    th1 = threading.Thread(target=camera,args=(cam_addr, outer_id))
    th2 = threading.Thread(target=listen)
    threads = [th1, th2]

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
