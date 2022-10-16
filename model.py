import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

x = []
y = []

def getinput(xinput, yinput):

  global x, y

  x = [int(i) for i in xinput.split()]
  y = [int(i) for i in yinput.split()]


def plotgraph():

  global x, y

  #Default values 
  if len(x) == 0 or len(y) == 0:
    x = [1,10,20,30,40,60]
    y = [25,27,23,25,23,27]
  
  slope, intercept, r, p, std_err = stats.linregress(x,y)

  def myfunc(x):
    return slope*x + intercept

  model = list(map(myfunc,x))

  plt.title("Regression")
  plt.scatter(x,y)
  plt.plot(x, model)
  plt.savefig("static/figure.png")
  plt.close()
