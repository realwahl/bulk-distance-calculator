import sys, urllib.parse, urllib.request, json, base64, hashlib, hmac, time

# define input and output files
inputfile = r"data\sample_input_file.txt"
outputfile = r"data\sample_output_file.txt"
# define fields position
idx_uniq_id = 0
idx_origin = 2
idx_destination = 4
#API key from Google Maps API Premium
key = "Enter-Your-Key"
#specifies the mode of transport to use when calculating directions. Valid values are: driving, walking, transit, or bicycling
mode = "driving"


google_url = "https://maps.googleapis.com"
distance_endpoint = "/maps/api/distancematrix/json?"
#sample API call that works
#https://maps.googleapis.com/maps/api/distancematrix/json?origins=Eiffel+Tower,+Paris,+France&destinations=51.5031897,-0.1220941&key=Enter-Your-Key 

field1 = "ID"
field2 = "origin"
field3 = "destination"
field4 = "distance_meters"
field5 = "duration_seconds"

f_in = open(inputfile, 'r')
f_out = open(outputfile, 'w')
f_out.write("%s\t%s\t%s\t%s\t%s\n" % (field1, field2, field3, field4, field5))
f_in_line = f_in.readlines()

for line in f_in_line:
   fields = line.strip().replace("\"", "").split('\t')
   uniq_id = fields[idx_uniq_id]
   origin = fields[idx_origin]
   destination = fields[idx_destination]
   #Generate valid signature
   encodedParams = urllib.parse.urlencode({"origins":origin,"destinations":destination,"mode":mode,"sensor":"false","key":key})
   #decode the private key into its binary format
   url = google_url + distance_endpoint + encodedParams
   result = urllib.request.urlopen(url)

   result_json = json.loads(result.read())
   try:
       check_status = result_json["rows"][0]["elements"][0]["status"]
   except:
       print (result_json["error_message"])
       quit()

   print ("Processing ID: " + uniq_id)
   try:
      f_out.write("%s\t%s\t%s\t%s\t%s\n" % (uniq_id, origin, destination, result_json["rows"][0]["elements"][0]["distance"]["value"], result_json["rows"][0]["elements"][0]["duration"]["value"]))
   except:
      f_out.write("%s\t%s\t%s\t%s\n" % (uniq_id, origin, destination, result_json["rows"][0]["elements"][0]["status"]))

print ("Finished!")
f_in.close()
f_out.close()
