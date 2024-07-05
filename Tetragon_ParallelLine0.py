import json
import numpy as np

#临时使用
[x1,y1,z1] = [0,0,0]
[x2,y2,z2] = [2,0,0]
[x3,y3,z3] = [0,2,0]
[x4,y4,z4] = [2,2,0]
[u1, v1, w1] = [1,0,0]
[u2, v2, w2] = [1,2,0]
coordinate_abcd = np.array([[x1, y1, z1],[x2, y2, z2],[x3, y3, z3],[x4, y4, z4]])
coordinate_ef = np.array([[u1, v1, w1],[u2, v2, w2]])
points_name = ['a', 'b', 'c', 'd']

def vector_AtoB(A, B):
    AB = np.array(B) - np.array(A)
    return AB

def boole_computation(AB, CD):
    is_cross_zero = np.all(np.cross(AB, CD) == 0)
    return is_cross_zero

def find_scalar_multiple(A, B):
    k_values = []
    if A[0] != 0:
        k_values.append(B[0] / A[0])
    if A[1] != 0:
        k_values.append(B[1] / A[1])
    if A[2] != 0:
        k_values.append(B[2] / A[2])
    if len(set(k_values)) == 1:
        return k_values[0]
    else:
        return None

"""
计算两组向量：[ab,ac,ad],ef,ae
"""
vectors_ax = []

for i in range(3):
    result_vax = np.array(coordinate_abcd[i + 1]) - np.array(coordinate_abcd[0])
    vectors_ax.append(result_vax)
ef = np.array(coordinate_ef[1]) - np.array(coordinate_ef[0])

"""
计算ef与ax的差值
"""
cross_mults = []
boole0 = []

for i in range(3):
    result_c = np.cross(vectors_ax[i], ef)
    cross_mults.append (result_c)
for i in range(3):
    boole0.append(np.all(cross_mults[i] == 0))

"""
判断ef与ax是否平行
平行-->导出这组点与四边形上另外两个点的坐标、名称,写入文件
"""
parallel_edges = {"parallel_to": "ef"}

for i in range (3):
    if boole0[i]:
        serial_of_x = int((-3 / 2) * ((i + 1) ** 2) + (11 / 2) * (i + 1) - 2)
        serial_of_x_ = int((3 / 2) * ((i + 1) ** 2) - (13 / 2) * (i + 1) + 8)

        a = coordinate_abcd[0].tolist()
        a_ = coordinate_abcd[i+1].tolist()
        x = coordinate_abcd[serial_of_x].tolist()
        x_ = coordinate_abcd[serial_of_x_].tolist()

        aname = points_name[0]
        a_name = points_name[i + 1]
        xname = points_name[serial_of_x]
        x_name = points_name[serial_of_x_]

        parallel_edges[f"a{points_name[i + 1]}"] = [a, a_]
        parallel_edges[f"{points_name[serial_of_x]}{points_name[serial_of_x_]}"] = [x, x_]

with open('data.json', 'w') as json_file:
    json.dump(parallel_edges, json_file)

"""
判断e与ax,ax_,a_x,a_x_的关系
"""
ax = vector_AtoB(a, x)
ax_ = vector_AtoB(a, x_)
a_x = vector_AtoB(a_, x)
a_x_ = vector_AtoB(a_, x_)
ae = vector_AtoB(a, coordinate_ef[0])
a_e = vector_AtoB(a_, coordinate_ef[0])

if not (boole_computation(ae,ax) and boole_computation(ae,ax_)):
    if not (boole_computation(a_e,a_x)):
        k = find_scalar_multiple(a_x,a_e)
        print(f"e在{a_name}{xname}上,{a_name}e = {k}{a_name}{xname}")
    else:
        k = find_scalar_multiple(a_e,a_x_)
        print(f"e在{a_name}{x_name}上,{a_name}e = {k}{a_name}{x_name}")
else:
    if not (boole_computation(ae,ax)):
        k = find_scalar_multiple(ax,ae)
        print(f"e在{aname}{xname}上,{aname}e = {k}{aname}{xname}")
    else:
        k = find_scalar_multiple(ax_,ae)
        print(f"e在{aname}{x_name}上,{aname}e = {k}{aname}{x_name}")