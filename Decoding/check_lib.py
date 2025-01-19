import ctypes

try:
    ctypes.cdll.LoadLibrary('/opt/homebrew/lib/libdmtx.dylib')
    print("libdmtx loaded successfully!")
except OSError as e:
    print(f"Failed to load libdmtx: {e}")