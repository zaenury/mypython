import time
start_time = time.time()

print("hello world")
print("Test Python")

a = 10
print(a)
for i in range(1,10000):
  a = 10

print(time.time() - start_time, "detik")


# To run python with interpreter, the command is: python3 namefile.py
# To run python with compiler, the command is: python3 -m py_compile namefile.py. cd __pycache__ namefile.cpython-310.pyc
# Or after creating __pycache__ folder. We can use: pyhton3 __pycache__/namefile.cpython_310.pyc
# Default python using intrerpreter. But we can use compiler which the compiler is faster than interpreter