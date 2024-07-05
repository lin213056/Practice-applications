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
coordinate_name = ['a','b','c','d']

#计算向量ab,ac,ad,ef
def vector_computation(x,y):
    result = x - y
    return result

def vector_computation_name(x,y):
    result = np.array(y)-np.array(x)
    return result

def boole_computation(x,y):
    result = np.all(np.cross(x,y) == 0)
    return result

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

vectors_ax = []
vectors___ = []
cross_mults = []
parallel_edges = {"parallel_to": "ef"}
boole0 = []
boole1 = True
cross_result0 = float(0)
cross_result1 = []
cross_result2 = []

"""
计算两组向量：[ab,ac,ad],ef,ae
"""
for i in range(3):
    vector_c = np.array(coordinate_abcd[i+1])-np.array(coordinate_abcd[0])
    vectors_ax.append(vector_c)
ef = np.array(coordinate_ef[1]) - np.array(coordinate_ef[0])

"""
判断与ef平行的线，写入json
"""
for i in range(3):
    cross_result0 = np.cross(vectors_ax[i],ef)
    cross_mults.append (cross_result0)
for i in range(3):
    boole0.append(np.all(cross_mults[i] == 0))
for i in range (3):
    if boole0[i]:
        serial0 = int((-3/2)*((i+1)**2)+(11/2)*(i+1)-2)
        serial1 = int((3/2)*((i+1)**2)-(13/2)*(i+1)+8)
        a = coordinate_abcd[0].tolist()
        a_ = coordinate_abcd[i+1].tolist()
        x = coordinate_abcd[serial0].tolist()
        x_ = coordinate_abcd[serial1].tolist()
        aname = coordinate_name[0]
        a_name = coordinate_name[i+1]
        xname = coordinate_name[serial0]
        x_name = coordinate_name[serial1]
        parallel_edges[f"a{coordinate_name[i+1]}"] = [a,a_]
        parallel_edges[f"{coordinate_name[serial0]}{coordinate_name[serial1]}"] = [x,x_]

with open('data.json', 'w') as json_file:
    json.dump(parallel_edges, json_file)

"""
判断e与ax,ax_,a_x,a_x_的关系
"""
ax = vector_computation_name(a,x)
ax_ = vector_computation_name(a,x_)
a_x = vector_computation_name(a_,x)
a_x_ = vector_computation_name(a_,x_)
ae = vector_computation_name(a,coordinate_ef[0])
a_e = vector_computation_name(a_,coordinate_ef[0])

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