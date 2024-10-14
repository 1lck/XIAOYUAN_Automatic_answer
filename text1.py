import time

import pyautogui
import pyautogui as pya
import pygetwindow as gw
import pytesseract
from PIL import Image, ImageEnhance
while(1):
    # 设置 Tesseract 的路径
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    def find_windows_position():
        # 获取名为“雷电模拟器”的窗口
        note_pad_windows = gw.getWindowsWithTitle('雷电模拟器')
        if note_pad_windows:
            note_pad_window = note_pad_windows[0]
            x, y = note_pad_window.left, note_pad_window.top
            z, d = x + note_pad_window.width, y + note_pad_window.height
            return x, y, z, d, note_pad_window.width, note_pad_window.height
        else:
            return None


    window_pos = find_windows_position()

    if window_pos is not None:
        x, y, z, d, width, height = window_pos

        # 打印窗口位置和大小，以确认是否正确
        print(f"Window Position: ({x}, {y}), Size: ({width}, {height})")

        # 调整截取区域
        adjusted_x = x  # 不需要额外的偏移
        adjusted_y = y  # 不需要额外的偏移
        adjusted_width = width  # 使用总窗口的宽度
        adjusted_height = height  # 使用总窗口的高度

        # 使用调整后的坐标进行截取
        region = (adjusted_x, adjusted_y, adjusted_x + adjusted_width, adjusted_y + adjusted_height)
        screenshot = pya.screenshot(region=region)


        def recognize_number(img):
            config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
            bottom_text = pytesseract.image_to_string(img, config=config)
            return bottom_text.strip()


        def preprocess_image(img):
            # 转换为灰度图像
            img_gray = img.convert('L')
            # 增强对比度
            enhancer = ImageEnhance.Contrast(img_gray)
            img_enhanced = enhancer.enhance(2)  # 可以尝试调整增强因子
            # 二值化
            img_binarized = img_enhanced.point(lambda x: 0 if x < 128 else 255, '1')
            return img_binarized


        def more():
            # 限定在左上角坐标为 (58, 622)，左下角坐标为 (500, 874) 的矩形区域内
            region_left = 58
            region_top = 622
            region_right = 500
            region_bottom = 874

            # 计算偏移量
            offset_x = (region_right - region_left) / 5
            offset_y = (region_bottom - region_top) / 5

            # 大于号的绘制路径
            def draw_greater():
                # 计算起始点
                #start_x = region_left + offset_x
                #start_y = region_top + offset_y
                start_x =220
                start_y = 730

                # 计算第二点
                #mid_x1 = region_left + 2 * offset_x
                #mid_y1 = region_top + offset_y
                mid_x1 =273
                mid_y1 =781

                # 计算第三点
                #end_x = region_left + 3 * offset_x
                #end_y = region_top + offset_y
                end_x =200
                end_y =800

                # 移动到起始位置并按下鼠标左键
                pya.moveTo(start_x, start_y)
                pya.mouseDown()

                # 第一条斜线
                pya.moveTo(mid_x1, mid_y1, duration=0.12)

                # 第二条水平线
                pya.moveTo(end_x, end_y, duration=0.12)

                # 释放鼠标左键
                pya.mouseUp()

            # 调用绘制大于号的方法
            draw_greater()
        def dianji1():
            x, y = 410, 973

            # 移动鼠标到指定位置
            pyautogui.moveTo(x, y)

            # 暂停一段时间（可选）
            time.sleep(1)

            # 在当前位置执行左键点击
            pyautogui.click()


        def dianji2():
            x, y = 270, 910

            # 移动鼠标到指定位置
            pyautogui.moveTo(x, y)

            # 暂停一段时间（可选）
            time.sleep(1)

            # 在当前位置执行左键点击
            pyautogui.click()
        def dianji3():
            x, y = 280,830

            # 移动鼠标到指定位置
            pyautogui.moveTo(x, y)

            # 暂停一段时间（可选）
            time.sleep(1)

            # 在当前位置执行左键点击
            pyautogui.click()

        def less():
            # 限定在左上角坐标为 (58, 622)，左下角坐标为 (500, 874) 的矩形区域内
            region_left = 58
            region_top = 622
            region_right = 500
            region_bottom = 874

            # 计算偏移量
            offset_x = (region_right - region_left) / 5
            offset_y = (region_bottom - region_top) / 5

            # 小于号的绘制路径
            def draw_less():
                # 计算起始点
                start_x = 330
                start_y = 635

                # 计算第二点
                mid_x1 = 273
                mid_y1 = 781

                # 计算第三点
                end_x = 335
                end_y = 850

                # 移动到起始位置并按下鼠标左键
                pya.moveTo(start_x, start_y)
                pya.mouseDown()

                # 第一条斜线
                pya.moveTo(mid_x1, mid_y1, duration=0.12)

                # 第二条水平线
                pya.moveTo(end_x, end_y, duration=0.12)

                # 释放鼠标左键
                pya.mouseUp()

            # 调用绘制小于号的方法
            draw_less()


        for i in range(10):
            # 使用调整后的坐标进行截取
            region = (adjusted_x, adjusted_y, adjusted_x + adjusted_width, adjusted_y + adjusted_height)
            screenshot = pya.screenshot(region=region)

            # 根据子窗口的坐标和尺寸裁剪子图
            first_subwindow_left = 110
            first_subwindow_top = 330
            first_subwindow_width = 120
            first_subwindow_height = 60
            left_img = screenshot.crop((first_subwindow_left, first_subwindow_top,
                                        first_subwindow_left + first_subwindow_width,
                                        first_subwindow_top + first_subwindow_height))

            second_subwindow_left = 340
            second_subwindow_top = 330
            second_subwindow_width = 80
            second_subwindow_height = 60
            right_img = screenshot.crop((second_subwindow_left, second_subwindow_top,
                                         second_subwindow_left + second_subwindow_width,
                                         second_subwindow_top + second_subwindow_height))

            # 预处理图像
            left_img_preprocessed = preprocess_image(left_img)
            right_img_preprocessed = preprocess_image(right_img)

            # 保存图像以便检查
            left_img_preprocessed.save("left_preprocessed.png")
            right_img_preprocessed.save("right_preprocessed.png")

            left_num_str = recognize_number(left_img_preprocessed)
            right_num_str = recognize_number(right_img_preprocessed)

            try:
                left_num = int(left_num_str)
                right_num = int(right_num_str)
                print(left_num, right_num)
            except ValueError:
                print(f"Failed to parse numbers from images: '{left_num_str}' and '{right_num_str}'")
                continue

            if left_num > right_num:
                more()
            else:
                less()

            time.sleep(0.5)
        time.sleep(4)
        dianji3()
        time.sleep(3)
        dianji1()
        time.sleep(3)
        dianji2()
        time.sleep(15)
    else:
        print("没有找到指定的窗口，请检查窗口标题是否正确以及窗口是否已经打开。")
