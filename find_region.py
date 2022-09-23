import numpy as np
x, y = np.meshgrid(np.linspace(-np.pi/2, np.pi/2, 30), np.linspace(-np.pi/2, np.pi/2, 30))
image = (np.sin(x**2+y**2)[1:-1,1:-2] > 0.9).astype(int) #boolean image

def get_img():
    x, y = np.meshgrid(np.linspace(-np.pi / 2, np.pi / 2, 30), np.linspace(-np.pi / 2, np.pi / 2, 30))
    image = (np.sin(x ** 2 + y ** 2)[1:-1, 1:-2] > 0.9).astype(int)
    return image


def neighbors(row_number, column_number,img,radius = 1):
    a = img
    return [[a[i][j] if i >= 0 and i < len(a) and j >= 0 and j < len(a[0]) else 0
             for j in range(column_number - 1 - radius, column_number + radius)]
            for i in range(row_number - 1 - radius, row_number + radius)]

if __name__ == "__main__":

    img = get_img()
    print(img)
    x = neighbors(2,15,img)
    print(x)