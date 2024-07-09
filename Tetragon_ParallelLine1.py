import math
import numpy as np
import json

def distance_3d(x1, y1, z1, x2, y2, z2):
    """
    计算三维空间中两点之间的距离
    """
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def is_point_on_segment_3d(px, py, pz, ax, ay, az, bx, by, bz):
    """
    判断点 (px, py, pz) 是否在线段 (ax, ay, az) - (bx, by, bz) 上
    使用向量法判断
    """
    ap = np.array([px - ax, py - ay, pz - az])
    ab = np.array([bx - ax, by - ay, bz - az])
    cross_product = np.cross(ap, ab)
    return np.all(cross_product == 0) and 0 <= np.dot(ap, ab) <= np.dot(ab, ab)

def point_segment_ratio(px, py, pz, ax, ay, az, bx, by, bz):
    """
    计算点 (px, py, pz) 到线段 (ax, ay, az) - (bx, by, bz) 的比例
    """
    if is_point_on_segment_3d(px, py, pz, ax, ay, az, bx, by, bz):
        segment_length = distance_3d(ax, ay, az, bx, by, bz)
        ap_length = distance_3d(ax, ay, az, px, py, pz)
        return ap_length / segment_length
    else:
        return None

def output():
    # 示例用点
    a = (0, 2, 1)
    b = (3, 2, 1)
    c = (4, 6, 1)
    d = (1, 6, 1)
    e = (0.5, 2, 1)
    f = (3.5, 6, 1)

    segments = [(a, b), (a, c), (a, d)]

    e_found = False
    f_found = False

    outputcontent = {}

    # 创建点字典
    points = {'b': b, 'c': c, 'd': d}

    # 判断点 e 是否在任何一条边上
    for j, segment in enumerate(segments):
        result = point_segment_ratio(e[0], e[1], e[2],
                                     segment[0][0], segment[0][1], segment[0][2], segment[1][0], segment[1][1], segment[1][2])
        if result is not None:
            output_char = chr(98 + j)
            remaining_chars = [char for char in points.keys() if char != output_char]
            outputcontent = {
                'e': e,
                f'a{output_char}': [a, points[output_char]],
                'f': f,
                f'{remaining_chars[0]}{remaining_chars[1]}': [points[remaining_chars[0]], points[remaining_chars[1]]],
                'k': result
            }
            print(f"Point e is on segment a{output_char}, ratio: {result:.2f}")
            e_found = True
            break

    if not e_found:
        # 判断点 f 是否在任何一条边上
        for j, segment in enumerate(segments):
            result = point_segment_ratio(f[0], f[1], f[2],
                                         segment[0][0], segment[0][1], segment[0][2], segment[1][0], segment[1][1], segment[1][2])
            if result is not None:
                output_char = chr(98 + j)
                remaining_chars = [char for char in points.keys() if char != output_char]
                outputcontent = {
                    'f': f,
                    f'a{output_char}': [a, points[output_char]],
                    'e': e,
                    f'{remaining_chars[0]}{remaining_chars[1]}': [points[remaining_chars[0]], points[remaining_chars[1]]],
                    'k': result
                }
                print(f"Point f is on segment a{output_char}, ratio: {result:.2f}")
                f_found = True
                break

        if not f_found:
            print("Point e and f are not on any segment a-b, a-c, or a-d")

    return outputcontent

def main():
    obtained_dictionary = output()
    print(obtained_dictionary)

    with open("output.json", "w") as json_file:
        json.dump(obtained_dictionary, json_file)

if __name__ == "__main__":
    main()