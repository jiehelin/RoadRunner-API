import os
import subprocess

pathToClient = r"C:\Users\admin\Desktop\RoadRunner_API"
pathToProtos = r"C:\Users\admin\Desktop\RoadRunner_API"

# Get list of all protobuf files
protoFiles = list()
for root, dirs, files in os.walk(pathToProtos):
    for file in files:
        if file.endswith(".proto"):
            protoFiles.append(os.path.join(root,file))

# Generate protobuf compiler command
command = ('python -m grpc.tools.protoc --proto_path="' + pathToProtos + \
'" --python_out="' + pathToClient + '" --grpc_python_out="' + pathToClient + '"')
 
for file in protoFiles:
    command += ' "' + file + '"'
 
print("Compiling protobuf files...")
print("Executing command:\n\n" + command + "\n")
 
out = subprocess.run(command, check=True)
 
print("Successfully compiled protobuf files. Generated Python files are located in '"
+ pathToClient + "'")