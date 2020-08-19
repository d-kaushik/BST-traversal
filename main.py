from flask import Flask, redirect, url_for, render_template, request


INT_MIN = -2**31
INT_MAX = 2**31
arr=[]
def in2post(exp):
	arr.clear()
	try:
		pre=exp.split()
		exp1=[]
		for k in pre:
			k=int(k)
			exp1.append(k)
	except:
		print("Enter in correct form")
		return
	n=len(pre)
	preIndex = [0]  
	findPostOrderUtil(exp1, n, INT_MIN, INT_MAX, preIndex)

def findPostOrderUtil(pre, n, minval,  
                      maxval, preIndex): 
  
    if (preIndex[0] == n): 
        return 
    if (pre[preIndex[0] ] < minval or pre[preIndex[0] ] > maxval): 
        return 
    val = pre[preIndex[0]]  
    preIndex[0] += 1  
    findPostOrderUtil(pre, n, minval, val, preIndex)   
    findPostOrderUtil(pre, n, val, maxval, preIndex)
    arr.append(val) 

app= Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
	if request.method =="POST":
		exp=request.form["exp"]
		in2post(exp)
		print(arr)
		
		return render_template("index.html",variable=arr)
	else:
		return render_template("index.html")

@app.route('/test')
def route1():
    return redirect("mailto:kaushik.daspute98@gmail.com")

@app.route('/linkedin')
def route2():
    return redirect("https://www.linkedin.com/in/kaushik98/")
	

if __name__=="__main__":
	app.run(debug=True)

      
     
	
