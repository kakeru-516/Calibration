import numpy as np
k_filename = 'K_fisheye.csv'
d_filename = 'd_fisheye.csv'
camera_mat = np.loadtxt(k_filename, delimiter=',')
dist_coef = np.loadtxt(d_filename, delimiter=',')
print(dist_coef)
print(dist_coef.shape)
m = np.zeros(shape=(3, 1))
m[0, 0] = 893.1
m[1, 0] = 394.3
m[2, 0] = 1
print(m)
prime = np.matmul(np.linalg.inv(camera_mat), m)
print(prime)
r_prime = np.sqrt(prime[0]**2 + prime[1]**2)

#ans = np.roots([dist_coef[3], 0, dist_coef[2], 0, dist_coef[1], 0, dist_coef[0], 0, -r_prime])
print(dist_coef[0])
ans = np.roots([dist_coef[0], 0, dist_coef[1], 0, dist_coef[2], 0, dist_coef[3], 0, 1, -r_prime])
print(ans)
print(r_prime)
print(np.rad2deg(0.74778424))
print(np.tan(0.74778424)*70-2.6)
print(np.rad2deg(1.4087595775048))