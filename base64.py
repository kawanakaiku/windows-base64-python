import sys, os, base64

decode = False
file = ""

for arg in sys.argv[1:]:
   if arg == "-d":
      decode = True
   elif file == "" and os.path.isfile(arg):
      file = arg
   else:
      if not os.path.exists(arg):
         sys.stdout.write("%s: no such file or directory.\n" % arg)
         sys.exit(1)

      elif os.path.isdir(arg):
         sys.stdout.write("%s: a directory.\n" % arg)
         sys.exit(1)

      elif file:
         sys.stdout.write("%s: more than two files specified.\n" % arg)
         sys.exit(1)

      else:
         sys.stdout.write("%s: error.\n" % arg)
         sys.exit(1)


if file == "":
   input = sys.stdin.buffer.read()
else:
   input = open(file, "rb").read()

if decode:
   output = base64.b64decode( input )
else:
   output = base64.b64encode( input )

sys.stdout.buffer.write( output )

sys.exit(0)
