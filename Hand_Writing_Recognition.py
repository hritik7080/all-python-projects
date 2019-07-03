# If you have any problem regarding the output of this program please go through the Hand_Writing_Recognition_readme.txt in the repository.

import warnings

warnings.filterwarnings("ignore")
from sklearn import datasets, svm
import matplotlib.pyplot as plt

digits = datasets.load_digits()
n_sample = len(digits.images)
img_data = digits.images.reshape(n_sample, -1)  # beacuse we have to fit data to the svm in vector format
# ------------------------------------------------------------------------------------
print(digits.keys())
images_n_labels = list(zip(digits.images, digits.target))
for index, [image, label] in list(enumerate(images_n_labels[:5])):
    plt.subplot(2, 5, index + 1)
    plt.imshow(image, cmap=plt.cm.gray_r)
    plt.title(f'training {label}')

# print(len(digits.images))

classifier = svm.SVC(gamma=0.001)
classifier.fit(img_data[:n_sample // 2], digits.target[:n_sample // 2])
pred_y = classifier.predict(img_data[n_sample // 2:])
img_n_pred = list(zip(digits.images[n_sample // 2:], pred_y))
for index, [image, prediction] in enumerate(img_n_pred[:5]):
    plt.subplot(2, 5, index + 6)
    plt.imshow(image, cmap=plt.cm.gray_r)
    plt.title(f'prediction {prediction}')
print("original vslues: ", digits.target[n_sample // 2:(n_sample // 2) + 5])
plt.show()
# ---------------------------------------------------------------------------------------

from scipy.misc import imread, imresize, bytescale

image = input("Enter the name/path of the image of a digit :")
img = imread(image)
img = imresize(img, (8, 8))
classifier = svm.SVC(gamma=0.001)
classifier.fit(img_data[:], digits.target[:])
img = img.astype(digits.images.dtype)
img = bytescale(img, high=16.0, low=0)
x_testdata = []
for i in img:
    for c in i:
        x_testdata.append(sum(c) / 3.0)   # because we need to take a 1D array of the averages of RGB of every pixel in the image.
        
answer = classifier.predict([x_testdata])
print("Machine's Answer is :", answer[0])
