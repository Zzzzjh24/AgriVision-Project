# AgriVision Project - Corn Disease Detector v1.0
# 农业视觉项目 - 玉米病害检测器 v1.0

import cv2
import numpy as np

def simple_color_analysis(image_path):
    """
    简单的颜色分析：识别图像中可能的病害黄色区域
    """
    # 读取图像
    img = cv2.imread(image_path)
    
    # 转换到HSV颜色空间（更适合颜色分析）
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 定义黄色的HSV范围（玉米霉变常呈现黄色）
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    # 创建黄色区域的掩码
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # 计算黄色像素比例
    total_pixels = img.shape[0] * img.shape[1]
    yellow_ratio = np.sum(mask > 0) / total_pixels
    
    print(f"图像分析完成: {image_path}")
    print(f"疑似病害区域(黄色)占比: {yellow_ratio:.2%}")
    
    # 简单的判断逻辑
    if yellow_ratio > 0.1:  # 如果黄色区域超过10%
        print("警告: 检测到显著病害风险！")
    else:
        print("状态: 作物表现正常")
    
    return yellow_ratio

# 测试代码
if __name__ == "__main__":
    print("=== AgriVision 玉米病害检测系统启动 ===")
    print("版本: v1.0 | 开发者: [你的名字]")
    print("=====================================")
    
    # 这里未来可以改成你的图片路径
    test_image = "sample_corn.jpg"  
    
    try:
        result = simple_color_analysis(test_image)
        print(f"\n分析结果已生成，病害风险系数: {result:.4f}")
    except Exception as e:
        print(f"分析过程中出现错误: {e}")
        print("请确保图片路径正确，且已安装OpenCV库")
