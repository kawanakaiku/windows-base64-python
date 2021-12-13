import sys, os, base64


def main():

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
      try:
         output = base64.b64decode( input )

      except base64.binascii.Error:
         sys.stdout.write("binascii.Error: invalid input")
         sys.exit(1)

   else:
      output = base64.b64encode( input )
   
   try:
      sys.stdout.buffer.write( output )
      
   except BrokenPipeError:
      sys.stdout.write("BrokenPipeError: pipe broken")
      sys.exit(1)

   sys.exit(0)


try:
   main()

except KeyboardInterrupt:
   sys.stdout.write("KeyboardInterrupt: exitting.")
   sys.exit(1)
