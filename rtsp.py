import cv2

# 输入RTSP URL
# 账户：admin 密码：UCTEAD ip：10.61.248.10:30301 （萤石摄像头）
rtsp_url = "rtsp://admin:UCTEAD@10.61.248.10:30301"

# 打开RTSP流
cap = cv2.VideoCapture(rtsp_url)

# 进入循环，直至opencv读不到信号或按下“q”键
while True:
    # 按帧读取视频
    ret, frame = cap.read()

    # 判断是否有视频
    if not ret:
        print("无法读取视频流，退出循环。")
        break

    # 展示视频
    cv2.imshow("RTSP Stream", frame)

    # 保存图像或视频
    # 在这里可以选择保存图像或视频，例：
    # cv2.imwrite("frame.jpg", frame)  # 保存当前帧为图像
    # 如果需要保存视频，可以使用 VideoWriter

    # 检测按键，按下“q”键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理资源
cap.release()
cv2.destroyAllWindows()