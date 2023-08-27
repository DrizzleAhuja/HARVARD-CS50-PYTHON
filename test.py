import os
import sys
 extensions = [".jpg", ".jpeg", ".png"]
    extension1 = os.path.splitext(sys.argv[1])
    extension2 = os.path.splitext(sys.argv[2])
print(extension1)
print(extension2)