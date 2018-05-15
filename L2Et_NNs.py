from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv1D, GlobalAveragePooling1D, MaxPooling1D
import numpy
import tensorflow as tf
from sklearn.model_selection import KFold
from sklearn.metrics import roc_curve, auc



"""
       File outputs: k flat files of ROC outputs and NN outputs  (k-folding is applied)
                     the k NN outputs still keep multiple variables from the flat training file
                     the k ROC outputs contains useful variables for ROC curves from scikit learn 
       Changed variables: the NN model, string name of dataset, and string name of output folder
                          this example uses a fully connected network with 4 layers
       Environment setting: run in environmnet with tensorflow and keras such as Tier3
                            need a flat file to train the NN as "dataset" 
                            create a folder ("ModelL2300.100.100.50_Et5ViPt0" in this case)
                            to keep the outputs from this NN model as well. 
"""

seed = 7
numpy.random.seed(seed)

dataset = numpy.loadtxt("L2Et_ViEt0Et5Eta1.4_Train.data", delimiter=",")
numpy.random.shuffle(dataset)

def KF_validation_print(dataset):
	kf = KFold(5,False,False)
	
	for train_index, test_index in kf.split(dataset):
		print("Train:", train_index, "Test:", test_index)


def model(dataset,train_index,test_index,name):
	fname = open("ModelL2300.100.100.50_Et5ViPt0/ROC_outputs"+name+".txt","w")
	fname2 = open("ModelL2300.100.100.50_Et5ViPt0/NNs_outputs"+name+".txt","w")	
	X_train, X_test = dataset[train_index,0:85], dataset[test_index,0:85]
	Y_train, Y_test = dataset[train_index,85], dataset[test_index,85]

	Pt = dataset[test_index,86]
	Obsv_Pt = dataset[test_index,87]
	bcid = dataset[test_index,88]
	trk = dataset[test_index,89]
        eta = dataset[test_index,90]
        phi = dataset[test_index,91]
	pi0 = dataset[test_index,92]
	model = Sequential()
        #model.add(Conv1D(64, 3, activation='relu', input_shape=(425,100)))
        #model.add(Conv1D(64, 3, activation='relu'))
        #model.add(MaxPooling1D(3))
        #model.add(Conv1D(128, 3, activation='relu'))
        #model.add(Conv1D(128, 3, activation='relu'))
        #model.add(GlobalAveragePooling1D())
        #model.add(Dropout(0.5))

	model.add(Dense(300, input_dim=85, init='uniform', activation='relu'))
	model.add(Dense(100, init='uniform', activation='relu'))
        model.add(Dense(100,init='uniform', activation='relu'))
        model.add(Dense(50, init='uniform', activation='relu'))
	model.add(Dense(1, init='uniform', activation='sigmoid'))

	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	model.fit(X_train,Y_train, epochs=100, batch_size=40, verbose=2)
	predictions = model.predict(X_test)
	fpr, tpr, thresholds = roc_curve(Y_test,predictions)
	roc_auc = auc(fpr, tpr)
	
	for i in range(len(predictions)):
		fname2.write(str(predictions[i])[1:-1]+","+str(Y_test[i])+","+str(Pt[i])+","+str(Obsv_Pt[i])+","+str(bcid[i])+","+str(trk[i])+","+str(eta[i])+","+str(phi[i])+","+str(pi0[i]))     
        for i in range(len(fpr)):
		fname.write(str(fpr[i])+","+str(tpr[i])+","+str(thresholds[i])+","+str(roc_auc)+":")
	fname2.close()
	fname.close()
	

def normal_validation(dataset):
	kf = KFold(4,False,False)
	i = 0
	for train_index, test_index in kf.split(dataset):
		i+=1
		if i == 4:
			train_index4 = train_index
			test_index4 = test_index
	model(dataset,train_index4,test_index4,"norm")

def KF_validation(dataset):
	kf = KFold(5,False,False)
	i = 0
	for train_index, test_index in kf.split(dataset):
		i+=1
		model(dataset,train_index,test_index,"KF"+str(i))


#normal_validation(dataset)
KF_validation(dataset)


