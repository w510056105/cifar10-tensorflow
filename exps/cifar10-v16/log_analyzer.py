# -*- encoding: utf-8 -*-
# author: ronniecao
import os
import re
import matplotlib.pyplot as plt
import numpy


def load_log(path):
	with open(path, 'r') as fo:
		loss_list, train_precision_list, valid_precision_list = [], [], []
		for line in fo:
			line = line.strip()
			pattern = re.compile(r'epoch\{([\d]+)\}, iter\[([\d]+)\], train loss: ([\d\.]+), valid precision: ([\d\.]+)')
			res = pattern.findall(line)
			if res:
				loss_list.append(float(res[0][2]))
				valid_precision_list.append(float(res[0][3]))
	return loss_list, valid_precision_list

def curve_smooth(data_list, batch_size=100):
	new_data_list, idx_list = [], []
	for i in range(int(len(data_list) / batch_size)):
		batch = data_list[i*batch_size: (i+1)*batch_size]
		new_data_list.append(1.0 * sum(batch) / len(batch))
		idx_list.append(i*batch_size)

	return new_data_list, idx_list

def plot_curve(loss_list1, loss_idxs1, valid_precision_list1, valid_precision_idxs1):
	fig = plt.figure(figsize=(10, 5))
	
	plt.subplot(121)
	p1 = plt.plot(loss_idxs1, loss_list1, '.--', color='#6495ED')
	# plt.legend((p1[0]), ('lr = 0.01'))
	plt.grid(True)
	plt.title('cifar10 image classification loss')
	plt.xlabel('# of epoch')
	plt.ylabel('loss')
	plt.axis([0, 500, 0, 300])
	"""
	plt.subplot(132)
	p4 = plt.plot(train_precision_idxs1, train_precision_list1, '.--', color='#66CDAA')
	p5 = plt.plot(train_precision_idxs2, train_precision_list2, '.--', color='#FF6347')
	p6 = plt.plot(train_precision_idxs3, train_precision_list3, '.--', color='#4EEE94')
	plt.legend((p4[0], p5[0], p6[0]), ('only flip', 'only crop', 'only whiten'))
	plt.grid(True)
	plt.title('cifar10 image classification train precision')
	plt.xlabel('# of epoch')
	plt.ylabel('accuracy')
	"""
	plt.subplot(122)
	p1 = plt.plot(valid_precision_idxs1, valid_precision_list1, '.--', color='#6495ED')
	# plt.legend((p1[0]), ('lr = 0.01'))
	plt.grid(True)
	plt.title('cifar10 image classification valid precision')
	plt.xlabel('# of epoch')
	plt.ylabel('accuracy')
	plt.axis([0, 500, 0.7, 0.9])

	plt.show()
	# plt.savefig('E:\\Github\cifar10-tensorflow\\exps\cifar10-v16\cifar10-v16.png', dpi=72, format='png')


loss_list1, valid_precision_list1 = load_log('E:\\Github\cifar10-tensorflow\\exps\cifar10-v16\cifar10-v16.txt')

# print(numpy.array(loss_list[-100:]).mean(), numpy.array(train_precision_list[-100:]).mean())
loss_list1, loss_idxs1 = curve_smooth(loss_list1, batch_size=1)
valid_precision_list1, valid_precision_idxs1 = curve_smooth(valid_precision_list1, batch_size=1)

plot_curve(loss_list1, loss_idxs1, valid_precision_list1, valid_precision_idxs1)