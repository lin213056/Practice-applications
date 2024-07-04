def cross_product(vector1, vector2):
    """
    计算两个三维向量的叉积

    参数:
    vector1 (list or tuple): 第一个三维向量
    vector2 (list or tuple): 第二个三维向量

    返回:
    list: 叉积结果向量
    """
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("输入的向量必须是三维向量")

    # 计算叉积
    result = [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]

    return result

def get_coordinate_input():
    """
    从键盘获取一个三维坐标的输入

    返回:
    list: 包含三个浮点数的三维向量
    """
    while True:
        try:
            coordinate = input("请输入一个三维坐标（格式: x y z）：")
            coordinate = [float(x) for x in coordinate.split()]
            if len(coordinate) != 3:
                raise ValueError("输入的向量必须是三维坐标")
            return coordinate
        except ValueError as e:
            print(f"输入格式错误: {e} 请确保输入三个浮点数，并用空格分隔。")

def generating_vectors(coordinate0,coordinate1):
    """
    输入两个三维坐标相减生成一个向量

    返回：一个三维向量
    """
    results = []
    for i in range(3):
        result = float(coordinate0[i] - coordinate1[i])
        results.append(result)
    return results

"""
获取abcd+ef，以及向量ab,ac,ad,ef
"""
coordinates_abcd = []
coordinates_ef = []
for i in range(4):
    print(f"请输入abcd组中第 {i+1} 个三维坐标：")
    coordinate = get_coordinate_input()
    coordinates_abcd.append(coordinate)
print(f"请输入第二组三维坐标：")
for i in range(2):
    print(f"请输入ef组中第 {i+1} 个三维坐标：")
    coordinate = get_coordinate_input()
    coordinates_ef.append(coordinate)

ax_vector = []
ef_vector = []
for i in range(3):
    ax_vector[i] = generating_vectors(coordinates_abcd[0],coordinates_abcd[i+1])
ef_vector.append(generating_vectors(coordinates_ef[0],coordinates_ef[1]))

"""
向量ax与向量ef叉积
"""
cross_product_result = []
for i in range[3]:
    result = cross_product(ef_vector[0],ax_vector[i])
    cross_product_result.append(result)