from camera import *

outer_id = 'yfacesy'
csvfilepath = "./faces/face_token.csv"
create_faceset(outer_id, csvfilepath)
print("初始化人脸数据集\n")

cam_addr = ''
outer_id = 'yfacesy'
camera(cam_addr, outer_id)

os.remove("./faces/face_token.csv")
os.remove('./faces/body_rect.csv')
result = delete_set(outer_id)
print("\n\n\nfaceset "+result['outer_id']+" 已删除")

