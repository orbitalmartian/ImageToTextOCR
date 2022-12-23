P='results.html'
O='home'
N='No file part'
L='POST'
G='home.html'
F='image'
D='/tmp'
import os as A
from flask import Flask,request as C,render_template as B,redirect as H,url_for as I
from PIL import Image as J
import pytesseract as K
E=Flask(__name__)
@E.route('/',methods=['GET',L])
def Q():
	if C.method==L:
		if F not in C.files:return B(G,error=N)
		E=C.files[F]
		if E.filename=='':return H(I(O))
		E.save(A.path.join(D,E.filename));M=J.open(A.path.join(D,E.filename));Q=K.image_to_string(M);A.remove(A.path.join(D,E.filename));return B(P,text=Q)
	return B(G)
@E.route('/process',methods=[L])
def R():
	if F not in C.files:return B(G,error=N)
	E=C.files[F]
	if E.filename=='':return H(I(O))
	E.save(A.path.join(D,E.filename));L=J.open(A.path.join(D,E.filename));M=K.image_to_string(L);A.remove(A.path.join(D,E.filename));return B(P,text=M);return B(G)
if __name__=='__main__':M=int(A.environ.get('PORT',5000));E.run(host='0.0.0.0',port=M)